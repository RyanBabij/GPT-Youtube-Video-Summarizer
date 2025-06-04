# AI-Youtube-Video-Summarizer

Uses yt-dlp and GPT to summarize Youtube videos by reading the subtitles.

You must have yt-dlp installed and accessible from the terminal.

You must also have an OpenAI API key, and have it set as a system variable: OPENAI_API_KEY.

Dependencies:

`pip install openai tiktoken yt-dlp`

Call it by using:

`python yt-sum.py`

It will then ask you for the URL. I designed it like this because it's easier to paste in the URL like this rather than constantly changing the terminal command.

The script will download the subtitles using yt-dlp, clean it, and then pass it to GPT along with the title of the video. GPT will then attempt to summarize the key points of the video. If the subtitle file is too long, it will be broken into chunks and each chunk will be summarized individually.

Unfortunately because of all the steps, it takes about 20-30 seconds to return the result. However it is much easier than skimming through a video manually.

Sample output:

```
================================================================================
                                Chunk 1 Summary
================================================================================

The video titled "Ocarina of Time Master Quest 01" features a group of friends,
Maxwell Adams, Fair, and Pipes, embarking on a gaming challenge. They plan to
play "The Legend of Zelda: Ocarina of Time Master Quest" in one sitting while
simultaneously watching the "Lord of the Rings" movies. The players introduce
themselves and set humorous personal challenges for each other, such as avoiding
making certain sounds or composing a poem.

Throughout the gameplay, the friends engage in light-hearted banter, discussing
various aspects of the game and the movies. They make jokes about the
differences between the original and GameCube versions of the game, such as the
color-coded buttons and the game's slower start. They also humorously compare
the game to elements of "Lord of the Rings," noting how the cinematic style
differs.

The players frequently break into comedic commentary, making references to pop
culture and other games, while also discussing game mechanics and features. They
note changes in dialogue and graphics between different versions of the game and
share insights into speedrunning tactics.

Overall, the video is characterized by its humorous and casual tone, with the
friends making jokes, setting challenges, and engaging in playful discussions
about the game and movies they are experiencing together.
```

If anyone comes up with some better prompts I would love to see them.

This project was created using GPT.
