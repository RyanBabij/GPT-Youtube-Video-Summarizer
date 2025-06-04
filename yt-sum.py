import subprocess
import re
import os
import glob
import tiktoken
import textwrap
from openai import OpenAI

# ========== Utility: Wrap and format console output ==========
def print_wrapped(title, text, width=80):
    divider = "=" * width
    print(f"\n{divider}\n{title.center(width)}\n{divider}\n")
    for line in text.splitlines():
        wrapped = textwrap.fill(line, width=width)
        print(wrapped)
    print("\n")


# ========== Step 1: Ask user for YouTube URL ==========
def get_youtube_url():
    return input("📺 Enter the YouTube URL: ").strip()

# ========== Step 2: Get video title using yt-dlp ==========
def get_video_title(url):
    result = subprocess.run(
        ["yt-dlp", "--get-title", url],
        capture_output=True,
        text=True
    )
    return result.stdout.strip() if result.returncode == 0 else "Untitled Video"

# ========== Step 3: Download subtitles ==========
def download_subtitles(url):
    command = [
        "yt-dlp",
        "--write-auto-sub",
        "--convert-subs", "srt",
        "--skip-download",
        url
    ]
    subprocess.run(command, check=True)

# ========== Step 4: Find latest .srt file ==========
def find_srt_file():
    files = glob.glob("*.en.srt") + glob.glob("*.srt")
    return max(files, key=os.path.getctime) if files else None

# ========== Step 5: Clean subtitle file ==========
def clean_subtitles(filename):
    bad_words = ['-->', '</c>']
    prefix = re.compile(r"^>> ")

    new_lines = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line = re.sub(prefix, "", line)
            if any(bad_word in line for bad_word in bad_words):
                if new_lines and re.match(r'^\d+$', new_lines[-1]):
                    new_lines.pop()
                continue
            if new_lines and line.startswith(new_lines[-1]):
                new_lines.pop()
            new_lines.append(line)

    return '\n'.join(new_lines)

# ========== Step 6: Split into large GPT-safe chunks ==========
def split_text_into_chunks(text, max_tokens=22000):
    enc = tiktoken.encoding_for_model("gpt-4o")
    lines = text.split('\n')

    chunks = []
    current_chunk = []
    current_tokens = 0

    for line in lines:
        line_tokens = len(enc.encode(line))
        if current_tokens + line_tokens > max_tokens:
            chunks.append('\n'.join(current_chunk))
            current_chunk = [line]
            current_tokens = line_tokens
        else:
            current_chunk.append(line)
            current_tokens += line_tokens

    if current_chunk:
        chunks.append('\n'.join(current_chunk))

    return chunks

# ========== Step 7: Summarize each chunk interactively ==========
def summarize_text(text, video_title):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY environment variable not set.")
        return

    client = OpenAI(api_key=api_key)
    chunks = split_text_into_chunks(text)
    partial_summaries = []

    for i, chunk in enumerate(chunks):
        print(f"\n📡 Summarizing chunk {i+1}/{len(chunks)}...\n")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant summarizing a YouTube video titled: '{video_title}'. Provide a clear, structured summary of the following section. Mention key events, arguments, or topics."
                },
                {
                    "role": "user",
                    "content": f"Summarize this portion of the subtitles:\n\n{chunk}"
                }
            ],
            temperature=0.5,
            max_tokens=1000
        )

        summary = response.choices[0].message.content
        partial_summaries.append(summary)
        print_wrapped(f"Chunk {i+1} Summary", summary)

        if i < len(chunks) - 1:
            cont = input("👉 Continue to next chunk? (y/n): ").strip().lower()
            if cont != 'y':
                print("\n🛑 Stopping early.\n")
                break


# ========== Step 8: Main entry point ==========
if __name__ == "__main__":
    url = get_youtube_url()
    title = get_video_title(url)
    print(f"\n📥 Downloading subtitles for: {title}\n")
    download_subtitles(url)
    srt_file = find_srt_file()

    if not srt_file:
        print("❌ No subtitle file found.")
    else:
        cleaned_text = clean_subtitles(srt_file)
        summarize_text(cleaned_text, title)
