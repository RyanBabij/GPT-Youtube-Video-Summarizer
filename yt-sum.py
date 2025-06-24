import os
import re
import time
import glob
import uuid
import textwrap
import subprocess
import concurrent.futures

from urllib.parse import urlparse, parse_qs
from openai import OpenAI
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR
import tiktoken

# ========== Utility Functions ==========

def print_wrapped(title, text, width=120):
    divider = "=" * width
    print(f"\n{divider}\n{title.center(width)}\n{divider}\n")
    for line in text.splitlines():
        wrapped = textwrap.fill(line, width=width)
        print(wrapped)
    print()

def get_youtube_url():
    return input("Enter the YouTube URL: ").strip()

def clean_youtube_url(url):
    """Strip everything after the first ampersand (&) to get the raw YouTube URL."""
    return url.split('&')[0]

def extract_video_id(url):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    return qs['v'][0] if 'v' in qs else "unknown_id"

# ========== YouTube Metadata & Subtitles ==========

def get_video_title(url):
    result = subprocess.run(
        ["yt-dlp", "--no-playlist", "--quiet", "--no-warnings", "--print", "%(title)s", url],
        capture_output=True, text=True
    )
    return result.stdout.strip() if result.returncode == 0 else None

def get_channel_name(url):
    result = subprocess.run(
        ["yt-dlp", "--no-playlist", "--quiet", "--no-warnings", "--print", "%(channel)s", url],
        capture_output=True, text=True
    )
    return result.stdout.strip() if result.returncode == 0 else "Unknown Channel"

def download_subtitles(url, video_id):
    output_base = f"video_{video_id}_{uuid.uuid4().hex[:6]}"
    command = [
        "yt-dlp",
        "--cookies-from-browser", "firefox",
        "--no-playlist",
        "--write-auto-sub",
        "--convert-subs", "srt",
        "--skip-download",
        "-o", f"{output_base}.%(ext)s",
        url
    ]
    subprocess.run(command, check=True)
    return output_base, output_base

def find_srt_file(base):
    files = glob.glob(f"{base}*.srt")
    return files[0] if files else None

def clean_subtitles(filename):
    bad_words = ('-->', '</c>')
    prefix = re.compile(r"^>> ")
    new_lines = []

    with open(filename, encoding='utf-8') as f:
        for line in f:
            if any(bad in line for bad in bad_words):
                continue
            line = line.strip()
            if not line or re.match(r'^\d+$', line):
                continue
            line = re.sub(prefix, "", line)
            if new_lines and line.startswith(new_lines[-1]):
                new_lines.pop()
            new_lines.append(line)
    return '\n'.join(new_lines)

# ========== Comments ==========

def download_comments(video_id, max_comments=100):
    downloader = YoutubeCommentDownloader()
    comments = []
    try:
        for comment in downloader.get_comments_from_url(
            f"https://www.youtube.com/watch?v={video_id}",
            sort_by=SORT_BY_POPULAR
        ):
            text = comment.get("text", "")
            if isinstance(text, str) and text.strip():
                comments.append(text.strip())
                if len(comments) >= max_comments:
                    break
    except Exception as e:
        print(f"Error downloading comments: {e}")
    return comments

# ========== Text Processing ==========

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

# ========== AI Summarization ==========

def summarize_text(text, video_title, channel_name, comments=None):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY environment variable not set.")
        return

    client = OpenAI(api_key=api_key)
    chunks = split_text_into_chunks(text)
    partial_summaries = []

    for i, chunk in enumerate(chunks):
        print(f"\nSummarizing chunk {i+1}/{len(chunks)}...\n")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant summarizing a YouTube video titled: '{video_title}' by the channel '{channel_name}'. Provide a clear, structured summary of the following section. Mention key events, arguments, or topics. Provide it in a chronological style. If the title of the video is a question with a fairly simple answer, please provide it at the beginning. If it's clickbait please mention this. If it proposes some kind of interesting idea or discusses a concept which is then summarized in the video, please provide that summary. If the video is a list of things, provide the list. If the title is vague, please give a less vague version based on the content of the video if possible. If you think the video isn't worth watching or lacks interest, please mention this. At the beginning please provide a clickbait rating of none, partial, or yes. None means it is definitely not clickbait, and yes means it's complete clickbait with no value. Provide 1 sentence explaining your decision. If the video is intended to be humorous or satirical, it is not clickbait. If the video pretends to have interesting information but does not, it is clickbait. If the video does what it says in the title, then it's not clickbait. If the video takes a long time to discuss something with a simple answer, it is clickbait. Do not use markdown. Use ALL CAPS for headings."
                },
                {
                    "role": "user", 
                    "content": f"Summarize this portion of the subtitles:\n\n{chunk}"
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )

        summary = response.choices[0].message.content
        partial_summaries.append(summary)
        print_wrapped(f"Chunk {i+1} Summary", summary)

        if i < len(chunks) - 1:
            cont = input("Continue to next chunk? (y/n): ").strip().lower()
            if cont != 'y':
                print("\nStopping early.\n")
                break

    full_summary = "\n\n".join(partial_summaries)
    comment_analysis = ""
    
    if comments:
        comment_text = "\n".join(comments[:50])
        print("\nAnalyzing top comments...\n")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant summarizing a YouTube video's comment section for the video titled '{video_title}' by '{channel_name}'."
                               " Look for common themes, praise, criticism, jokes, or controversy. Point out whether the video was well-received or not. At the beginning, provide a reception rating of positive, mixed, or negative. Do not use markdown. Use ALL CAPS for headings."
                },
                {
                    "role": "user",
                    "content": f"Here are the top comments:\n\n{comment_text}"
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )
        comment_analysis = response.choices[0].message.content
        print_wrapped("Comment Analysis", comment_analysis)
        
    duration = time.time() - start_time
    print(f"\n⏳ Total runtime: {duration:.2f} seconds\n")

    # ==== Follow-up Q&A ====
    # print_wrapped("Summary", full_summary)
    print("\nYou can now ask follow-up questions about the video. Type 'exit' to quit.\n")

    while True:
        question = input("❓ Ask a question: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Exiting Q&A.\n")
            break

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant answering questions about a YouTube video titled '{video_title}' by '{channel_name}'."},
                {"role": "user", "content": f"Here is a summary of the video:\n{full_summary}"},
                {"role": "user", "content": f"Here is the comment analysis:\n{comment_analysis}"},
                {"role": "user", "content": f"User question: {question}"}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        answer = response.choices[0].message.content
        print_wrapped("Answer", answer)


# ========== Threaded Fetch Wrappers ==========

def fetch_title(url): return get_video_title(url)
def fetch_channel(url): return get_channel_name(url)
def fetch_subtitles(url, video_id): return download_subtitles(url, video_id)
def fetch_comments(video_id): return download_comments(video_id)

# ========== Main Entry ==========

if __name__ == "__main__":
    start_time = time.time()
    raw_url = get_youtube_url()
    cleaned_url = clean_youtube_url(raw_url)
    video_id = extract_video_id(cleaned_url)

    if video_id == "unknown_id":
        print("Could not extract video ID from the URL.")
        exit(1)

    print("\nStarting metadata and subtitle downloads in parallel...\n")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_title = executor.submit(fetch_title, cleaned_url)
        future_channel = executor.submit(fetch_channel, cleaned_url)
        future_subs = executor.submit(fetch_subtitles, cleaned_url, video_id)
        future_comments = executor.submit(fetch_comments, video_id)

        title = future_title.result()
        channel = future_channel.result()
        output_base, _ = future_subs.result()
        comments = future_comments.result()

    srt_file = find_srt_file(output_base)

    if not srt_file:
        print("No subtitle file found.")
    else:
        print(f"Using video title: {title}")
        cleaned_text = clean_subtitles(srt_file)
        summarize_text(cleaned_text, title, channel, comments=comments)

