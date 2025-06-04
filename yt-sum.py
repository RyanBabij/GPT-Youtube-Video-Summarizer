import subprocess
import re
import os
import glob
import tiktoken
import textwrap
import uuid
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
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

# ========== Step 2: Clean YouTube URL ==========
def clean_youtube_url(url):
    """Remove playlist and other extraneous parameters from a YouTube URL."""
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    cleaned_qs = {'v': qs['v']} if 'v' in qs else {}
    cleaned_url = parsed._replace(query=urlencode(cleaned_qs, doseq=True))
    return urlunparse(cleaned_url)

# ========== Step 3: Get video title and ID in one call ==========
def get_video_info(url):
    result = subprocess.run(
        ["yt-dlp", "--no-playlist", "--get-id", "--get-title", url],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        return "Untitled Video", "unknown_id"
    lines = result.stdout.strip().splitlines()
    return lines[1], lines[0]  # title, video_id

# ========== Step 4: Download subtitles ==========
def download_subtitles(url, video_id):
    output_base = f"video_{video_id}_{uuid.uuid4().hex[:6]}"
    command = [
        "yt-dlp",
        "--no-playlist",
        "--write-auto-sub",
        "--convert-subs", "srt",
        "--skip-download",
        "-o", f"{output_base}.%(ext)s",
        url
    ]
    subprocess.run(command, check=True)
    return output_base

# ========== Step 5: Find latest .srt file ==========
def find_srt_file(base):
    files = glob.glob(f"{base}*.srt")
    return files[0] if files else None

# ========== Step 6: Clean subtitle file ==========
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

# ========== Step 7: Split into GPT-safe chunks ==========
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

# ========== Step 8: Summarize each chunk ==========
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
                    "content": f"You are a helpful assistant summarizing a YouTube video titled: '{video_title}'. Provide a clear, structured summary of the following section. Mention key events, arguments, or topics. Provide it in a chronological style."
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

# ========== Step 9: Main entry ==========
if __name__ == "__main__":
    raw_url = get_youtube_url()
    cleaned_url = clean_youtube_url(raw_url)
    title, video_id = get_video_info(cleaned_url)

    print(f"\n📥 Downloading subtitles for: {title}\n")
    output_base = download_subtitles(cleaned_url, video_id)
    srt_file = find_srt_file(output_base)

    if not srt_file:
        print("❌ No subtitle file found.")
    else:
        cleaned_text = clean_subtitles(srt_file)
        summarize_text(cleaned_text, title)
