# AI YouTube Video Summarizer

A Python script that uses yt-dlp, GPT and youtube-comment-downloader to summarize YouTube videos by analyzing their subtitles and comments.

```bash
pip install openai tiktoken yt-dlp youtube-comment-downloader
```

Run the script with:

```bash
python yt-sum.py
```

You’ll be prompted to paste a YouTube video URL. This way you can easily keep calling it and just paste in the URLs.

- Takes about 30-60 seconds per video, but you can run it in the background easily.
- Obviously it won't work well on videos without much talking.
- The clickbait detector needs improvement.

If you come up with interesting prompts feel free to share them.

This project was created using GPT.

## Sample output 1

```
python yt-sum.py
Enter the YouTube URL: www.youtube.com/watch?v=T1w2Z4owDqQ

Starting metadata and subtitle downloads in parallel...

[generic] Extracting URL: www.youtube.com/watch?v=T1w2Z4owDqQ
WARNING: [generic] The url doesn't specify the protocol, trying with http
[youtube] Extracting URL: http://www.youtube.com/watch?v=T1w2Z4owDqQ
[youtube] T1w2Z4owDqQ: Downloading webpage
[youtube] T1w2Z4owDqQ: Downloading tv client config
[youtube] T1w2Z4owDqQ: Downloading tv player API JSON
[youtube] T1w2Z4owDqQ: Downloading ios player API JSON
[youtube] T1w2Z4owDqQ: Downloading m3u8 information
[info] T1w2Z4owDqQ: Downloading subtitles: en
[info] T1w2Z4owDqQ: Downloading 1 format(s): 18
[info] Writing video subtitles to: video_T1w2Z4owDqQ_5b6e1f.en.vtt
[download] Destination: video_T1w2Z4owDqQ_5b6e1f.en.vtt
[download] 100% of  130.98KiB in 00:00:01 at 102.41KiB/s
[SubtitlesConvertor] Converting subtitles
Deleting original file video_T1w2Z4owDqQ_5b6e1f.en.vtt (pass -k to keep)
Using video title: Ocarina of Time Master Quest   01

Summarizing chunk 1/1...


========================================================================================================================
                                                    Chunk 1 Summary
========================================================================================================================

**Clickbait Rating: None**

**Summary:**

The video "Ocarina of Time Master Quest 01" by Maxwell Adams is a humorous playthrough of the game "The Legend of Zelda:
Ocarina of Time Master Quest." The video is not clickbait as it delivers exactly what the title suggests: a gameplay
session of the game.

- **Introduction:** The video begins with Maxwell Adams and his friends, Fair and Pipes, setting up to play "Ocarina of
Time Master Quest" in one sitting. They introduce a humorous twist by simultaneously watching the "Lord of the Rings:
Fellowship of the Ring" extended edition, treating it as an "Epic Fantasy Race."

- **Gameplay Start:** The game begins with Link sleeping in a Zen-like rock garden. The humor kicks in with a challenge
for one of the participants, IC, to comment without asking questions, likened to a backward Jeopardy game. Another
challenge involves refraining from making fart noises when using the horse's carrots in the game.

- **Humor and Commentary:** The participants engage in light-hearted banter, making jokes about the game and the movie.
They point out differences in game versions, such as the change in the color of the arrow from blue to green to match
the GameCube controller.

- **Observations and Jokes:** The group makes observations about the game's start being slow, poking fun at Link's lack
of a fairy, and the cinematic style of the opening. They humorously compare getting a fairy to events like a first
period or circumcision.

- **Technical and Gameplay Notes:** They note the differences in controls and graphics between the original N64 version
and the GameCube version, including the frame rate running at 50 frames per second due to the PAL ROM used for hacking.

- **Challenges and Tasks:** The players discuss their objectives, like collecting rupees, and make jokes about the
game's mechanics, such as Link's method of walking being faster when Z-targeting and walking backward.

- **Continued Banter:** The humor continues with jokes about the Lord of the Rings scenes, the game's dialogue, and
Link's equipment. They make playful references to other media, such as "Pulp Fiction" and "Big."

- **Conclusion of Section:** The section concludes with the group entering the first dungeon, the Deku Tree, and
encountering the first enemies. They continue to joke about the game's mechanics and the challenges they set for
themselves, including enforcing the "no questions" rule.

Overall, the video is a mix of gameplay, humorous commentary, and pop culture references, providing entertainment for
fans of both the game and the "Lord of the Rings" series.


Analyzing top comments...


========================================================================================================================
                                                    Comment Analysis
========================================================================================================================

**Reception Rating: Positive**

The video "Ocarina of Time Master Quest 01" by Maxwell Adams was well-received by viewers, as indicated by the comments.
Several themes and sentiments emerge from the comment section:

1. **Nostalgia and Comfort**: Many commenters express nostalgia, recalling fond memories of watching the Freelance
Astronauts' videos during various life events, such as cleaning, studying, or during long gaming sessions. The videos
are often described as comforting background noise, creating a relaxing atmosphere.

2. **Praise for Content**: The content is praised for its quality and entertainment value. Viewers appreciate the
camaraderie among the creators and the fun, laid-back style of the videos. The series is described as "quality content
in a sea of mediocrity," highlighting its enduring appeal.

3. **Community and Shared Experiences**: Commenters share personal anecdotes about how they discovered the Freelance
Astronauts and the impact the videos had on their lives. There is a sense of community among viewers who have followed
the series for years.

4. **Criticism of Past Humor**: Some viewers reflect on the humor used in the videos, particularly the prevalence of gay
jokes, which were more common in the early 2000s. While some find these jokes dated and insensitive, others argue that
they were not intended to be hateful. This reflects broader discussions about changing social norms and the evolution of
humor.

5. **Engagement with Other Media**: Comments mention how the video inspires viewers to engage with other games or media,
such as playing Disgaea or rewatching "The Lord of the Rings."

Overall, the video is positively received, with viewers expressing appreciation for its nostalgic value and the sense of
community it fosters, despite some critical reflections on past humor.


⏳ Total runtime: 40.94 seconds
```

## Sample output 2

```
python yt-sum.py
Enter the YouTube URL: https://www.youtube.com/watch?v=Pwk5MPE_6zE&t=2241s

Starting metadata and subtitle downloads in parallel...

[youtube] Extracting URL: https://www.youtube.com/watch?v=Pwk5MPE_6zE
[youtube] Pwk5MPE_6zE: Downloading webpage
[youtube] Pwk5MPE_6zE: Downloading tv client config
[youtube] Pwk5MPE_6zE: Downloading tv player API JSON
[youtube] Pwk5MPE_6zE: Downloading ios player API JSON
[youtube] Pwk5MPE_6zE: Downloading m3u8 information
[info] Pwk5MPE_6zE: Downloading subtitles: en
[info] Pwk5MPE_6zE: Downloading 1 format(s): 616+251
[info] Writing video subtitles to: video_Pwk5MPE_6zE_585380.en.vtt
[download] Destination: video_Pwk5MPE_6zE_585380.en.vtt
[download] 100% of  854.32KiB in 00:00:02 at 378.97KiB/s
[SubtitlesConvertor] Converting subtitles
Deleting original file video_Pwk5MPE_6zE_585380.en.vtt (pass -k to keep)
Using video title: Jordan Peterson vs 20 Atheists | Surrounded

Summarizing chunk 1/1...


========================================================================================================================
                                                    Chunk 1 Summary
========================================================================================================================

**Clickbait Rating: Partial**

The video titled "Jordan Peterson vs 20 Atheists | Surrounded" by Jubilee is partially clickbait. While the title
suggests a confrontational debate between Jordan Peterson and a large group of atheists, which does occur, the video
primarily focuses on discussions rather than a heated debate. The title may imply a more aggressive confrontation than
what actually takes place, as the conversations are structured and aim to explore philosophical and theological ideas
rather than simply argue.

**Summary:**

1. **Introduction and Setup:**
   - The video begins with a participant questioning Jordan Peterson's religious beliefs, highlighting a
misunderstanding about his stance as a Christian.
   - Peterson introduces himself and states his claim that atheists reject God without understanding what they're
rejecting.

2. **First Interaction:**
   - A participant with a background in Catholicism challenges Peterson on his claim, arguing that he has a deep
understanding of what he's rejecting.
   - Peterson suggests that atheists have a reductive notion of God and that their rejection often stems from personal
hurt or negative experiences with religion.

3. **Discussion on Definitions:**
   - The conversation shifts to defining God, with Peterson asking how the participant defines the God they reject.
   - The participant argues that Peterson's definition of religion is too broad and that his view of atheism is
reductive.

4. **Biblical Interpretation:**
   - Peterson discusses the complexity of interpreting biblical stories, using the story of Moses as an example.
   - The participant argues about the multiple interpretations of biblical texts and questions Peterson's approach to
defining God.

5. **Morality and Science:**
   - Peterson claims that morality and purpose cannot be found within science, prompting discussions on morality's
origins and its relation to social animals.
   - Participants argue that morality has evolutionary roots and does not necessarily require religious foundations.

6. **Concept of Worship:**
   - Peterson claims that everyone, including atheists, worships something, defined as what they prioritize and
sacrifice for.
   - Participants challenge this definition, arguing that it dilutes the traditional understanding of worship.

7. **Christian Morality and Atheism:**
   - Peterson argues that atheists accept Christian morality but deny the religion's foundational stories.
   - Discussions ensue about the nature of Christian ethics and the historical context of biblical commands.

8. **Final Reflections:**
   - Peterson reflects on the conversations, emphasizing the importance of dialogue aimed at understanding rather than
winning.
   - Participants express mixed feelings about Peterson's approach, noting his tendency to redefine terms and concepts.

Overall, the video explores deep philosophical and theological questions, with Peterson engaging in dialogues that
challenge both his and the participants' viewpoints. While the title suggests a more adversarial setup, the content
focuses on exploring and questioning beliefs rather than outright debate.


Analyzing top comments...


========================================================================================================================
                                                    Comment Analysis
========================================================================================================================

**Reception Rating: Mixed**

The comment section for the video "Jordan Peterson vs 20 Atheists | Surrounded" by Jubilee reveals a mixed reception
from viewers. Here are some common themes and observations:

1. **Title Change and Humor**: Many commenters noted and joked about the title change from “1 Christian vs 20 Atheists”
to “Jordan Peterson vs 20 Atheists.” This change was seen as humorous by some, suggesting it reflects how the narrative
or context of the video was perceived or altered.

2. **Misrepresentation Concerns**: A significant number of comments criticize the choice of Jordan Peterson to represent
Christians, pointing out that he has never explicitly claimed to be one. Viewers expressed that a more traditional
Christian figure, such as a pastor or theologian, would have been more appropriate.

3. **Debate Style and Confusion**: Several comments critique Peterson’s debate style, describing it as evasive and
confusing. There is a sentiment that he doesn’t clearly state his beliefs, making it difficult for others to engage with
him meaningfully.

4. **Praise and Defense**: Some viewers defended Peterson, suggesting he represented Christian values well, despite not
being a traditional Christian. A few commenters appreciated his philosophical approach and honesty regarding his
beliefs.

5. **Criticism of Jubilee's Format**: The format of the video itself was criticized, with some viewers feeling it was
more of an ambush than a fair debate. There were calls for more structured and meaningful discussions with experts in
the field.

6. **Humor and Sarcasm**: The comments also include humorous and sarcastic takes on the situation, with jokes about
Peterson’s enigmatic nature and hypothetical debate scenarios.

Overall, the video sparked controversy and debate about representation, debate tactics, and the intentions behind the
format, leading to a mixed reception among viewers.


⏳ Total runtime: 53.26 seconds
```

## Sample output 3

```
python yt-sum.py
Enter the YouTube URL: https://www.youtube.com/watch?v=NRZf5or7u4M

Starting metadata and subtitle downloads in parallel...

[youtube] Extracting URL: https://www.youtube.com/watch?v=NRZf5or7u4M
[youtube] NRZf5or7u4M: Downloading webpage
[youtube] NRZf5or7u4M: Downloading tv client config
[youtube] NRZf5or7u4M: Downloading tv player API JSON
[youtube] NRZf5or7u4M: Downloading ios player API JSON
[youtube] NRZf5or7u4M: Downloading m3u8 information
[info] NRZf5or7u4M: Downloading subtitles: en
[info] NRZf5or7u4M: Downloading 1 format(s): 247+251
[info] Writing video subtitles to: video_NRZf5or7u4M_72e2a5.en.vtt
[download] Destination: video_NRZf5or7u4M_72e2a5.en.vtt
[download] 100% of    8.17KiB in 00:00:00 at 41.34KiB/s
[SubtitlesConvertor] Converting subtitles
Deleting original file video_NRZf5or7u4M_72e2a5.en.vtt (pass -k to keep)
Using video title: LOGAN PAUL FOREST VIDEO *DELETED VIDEO*

Summarizing chunk 1/1...


========================================================================================================================
                                                    Chunk 1 Summary
========================================================================================================================

**Clickbait Rating: Yes**

This section of the video features a controversial and sensitive moment where the speaker, presumably Logan Paul,
encounters a distressing scene in a forest. The speaker initially expresses disbelief and shock upon seeing a person
hanging, which they describe as an unforgettable and life-changing experience. The speaker then reflects on the gravity
of the situation, stating it's one of the craziest things they've ever encountered. Despite the serious nature of the
event, the speaker mentions using humor as a coping mechanism, which may come across as inappropriate given the
circumstances. They acknowledge the sadness of the situation but note their tendency to use humor to manage emotions.
Additionally, the speaker advises viewers against visiting the location, emphasizing the gravity of the situation. The
video, due to its handling of a sensitive topic and the way it was presented, has been widely criticized and is
considered clickbait as it lacks respectful engagement with the subject matter.


Analyzing top comments...


========================================================================================================================
                                                    Comment Analysis
========================================================================================================================

**Reception Rating: Negative**

The comment section of the video "LOGAN PAUL FOREST VIDEO *DELETED VIDEO*" by 'Ant Resto' reveals a predominantly
negative reception. Here are the common themes and sentiments:

1. **Criticism of Logan Paul's Actions**: Many comments express outrage and disappointment over Logan Paul's decision to
film and post a video of a deceased person in a forest. Commenters highlight the disrespectful nature of his actions,
particularly focusing on his use of the video as clickbait and his inappropriate reactions, such as joking and laughing.

2. **Impact on Viewers**: Several comments mention the negative impact the original video had on viewers, especially
younger audiences. One commenter recalls being 12 years old and feeling disturbed by the vivid depiction of the body.

3. **Long-lasting Controversy**: Commenters emphasize that this incident marked a significant low point for YouTube and
express disbelief that Logan Paul and others involved faced little long-term consequences. There is a sense of
frustration that he continues to have a platform despite this controversy.

4. **Coping Mechanisms and Reactions**: Some comments discuss the possibility that Logan Paul's laughter might have been
a nervous reaction, though this is generally met with skepticism. The notion of using humor as a coping mechanism is
mentioned, but many viewers find it an inadequate justification for his behavior.

5. **Continued Distrust**: There is a recurring theme of distrust toward Logan Paul, with viewers expressing concern
that similar incidents could happen again, either with him or other content creators like Mr. Beast.

6. **Jokes and Sarcasm**: While the overall tone is critical, some comments incorporate sarcasm or dark humor,
reflecting disbelief at the situation and its aftermath.

Overall, the comment section reflects a strong consensus that the video and Logan Paul's actions were inappropriate,
highlighting the lasting negative impact on viewers and the YouTube community.


⏳ Total runtime: 31.92 seconds
```