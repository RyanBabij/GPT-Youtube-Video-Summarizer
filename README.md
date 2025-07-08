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

If the application tells you something about being a bot, you need to add in your browser cookies to the command array:

```"--cookies-from-browser", "firefox",```
```"--cookies-from-browser", "chrome",```

This project was created using GPT.

## Clickbait detection
This has proven difficult to implement but it's somewhat functional. I have found it best to break the rating system into categories which are currently: None, exaggerated, misinformation, clickbait.

## Issues

* The clickbait detector isn't as good as I would like it to be.
* It's great at extracting lists of things from shorter videos but in very long videos it may have difficulty.
* The followup question feature isn't very helpful atm.

## Sample output 1 - My TOP Add-Ons To IMPROVE REALISM in MSFS 2024

```

python yt-sum.py
Enter the YouTube URL: https://www.youtube.com/watch?v=Hr1agJcLO70

Starting metadata and subtitle downloads in parallel...

Extracting cookies from firefox
Extracted 2479 cookies from firefox
[youtube] Extracting URL: https://www.youtube.com/watch?v=Hr1agJcLO70
[youtube] Hr1agJcLO70: Downloading webpage
[youtube] Hr1agJcLO70: Downloading tv client config
[youtube] Hr1agJcLO70: Downloading tv player API JSON
[info] Hr1agJcLO70: Downloading subtitles: en
[info] Hr1agJcLO70: Downloading 1 format(s): 399+251
[info] Writing video subtitles to: video_Hr1agJcLO70_72b577.en.vtt
[download] Destination: video_Hr1agJcLO70_72b577.en.vtt
[download] 100% of  141.61KiB in 00:00:02 at 63.46KiB/s
[SubtitlesConvertor] Converting subtitles
Deleting original file video_Hr1agJcLO70_72b577.en.vtt (pass -k to keep)
Video title: My TOP Add-Ons To IMPROVE REALISM in MSFS 2024

Summarizing chunk 1/1...

                                CHUNK 1 SUMMARY
================================================================================


CLICKBAIT RATING: None. The video delivers on its promise by providing a
detailed list of add-ons to improve realism in Microsoft Flight Simulator 2024.

KEY POINTS:
1. The video discusses various aircraft add-ons, including the Phoenix A320 and
FlyByWire planes, to enhance realism in Microsoft Flight Simulator 2024.
2. It highlights the importance of using VATSIM for realistic air traffic
control and mentions alternative ATC systems like Beyond ATC and Say Intentions.
3. The video emphasizes the significance of accurate scenery, charts, and ground
services, recommending resources like Navigraph, SimBrief, and GSX.

DETAILED SUMMARY:

INTRODUCTION
- The video begins by addressing a common question from viewers about how to
make Microsoft Flight Simulator 2024 more realistic, and the host plans to share
the core add-ons used to enhance the experience.

AIRCRAFT ADD-ONS
- The host praises the default planes in Flight Simulator 2024 but recommends
additional aircraft for enthusiasts, such as the Phoenix A320, which includes an
expansion pack for the A319 and A321.
- For vintage Airbus fans, the AnyBuilds Airbus A300 is recommended, and the
newly launched Airbus A350 is highlighted for its detailed design.
- PMDG Boeings are suggested for serious simmers, though they are still being
adapted for 2024.
- FlyByWire offers free alternatives like the A320 Neo and A380, which can be
transferred from the 2020 version to 2024.

AIR TRAFFIC CONTROL
- VATSIM is recommended as the best way to enhance realism with real pilots and
air traffic controllers, despite requiring a base level of knowledge and a test.
- Alternatives to the default ATC system include Beyond ATC and Say Intentions,
both offering advanced features and different pricing models.

SCENERY AND LIVERIES
- The importance of accurate scenery is discussed, especially for use with
VATSIM, with recommendations for both payware and free options from
FlightSim.to.
- FS LTL is suggested for realistic liveries, enhancing the visual experience
when connected to VATSIM.

CHARTS AND FLIGHT PLANNING
- Navigraph is recommended for comprehensive charts and keeping nav data up to
date, with ChartFox as a free alternative.
- SimBrief is highlighted as a powerful flight planning tool, integrated with
Navigraph for the latest data.

CAREER MODE AND VIRTUAL AIRLINES
- The host mentions the new career mode in Flight Simulator 2024 but prefers
using a virtual airline through New Sky, which offers a dynamic and competitive
experience.

GROUND SERVICES
- GSX is used for loading aircraft and pushback services, despite occasional
issues, and is noted for its integration with some aircraft add-ons.

CONCLUSION
- The video concludes by inviting viewers to share their own add-ons and
experiences in the comments, encouraging community engagement. The host also
promotes their Twitch channel for live streaming sessions.


Analyzing top comments...

                                COMMENT ANALYSIS
================================================================================


RECEPTION RATING: POSITIVE

COMMON THEMES:
1. Vatsim vs. BeyondATC/SayIntentions: Many commenters discuss the use of Vatsim
and alternatives like BeyondATC and SayIntentions, highlighting the benefits of
having AI-controlled ATC available worldwide at any time.
2. Add-ons and Tools: There is a strong interest in various add-ons such as A
Pilot's Life, FSHud, and Volanta, with users sharing their experiences and
preferences.
3. Realism and Immersion: Commenters appreciate tools that enhance realism, such
as traffic injection and ATC communication, which make the simulation feel more
alive.
4. Transition to MSFS 2024: Some users discuss the transition from MSFS 2020 to
2024, with mixed feelings about the availability of add-ons and the stability of
the new version.

PRAISE:
- The video is well-received, with many viewers thanking the creator for the
information and expressing interest in trying out the recommended add-ons.
- Commenters appreciate the detailed descriptions and recommendations provided
in the video.

CRITICISM:
- Some users express frustration with the transition to MSFS 2024, citing issues
with add-on compatibility and stability compared to MSFS 2020.
- A few comments mention dissatisfaction with specific aircraft models or
features within the simulator.

JOKES:
- A light-hearted comment refers to the A318 as the "minibus," adding humor to
the discussion.

CONTROVERSY:
- There is some debate over the effectiveness and preference of different ATC
programs, with users sharing varied experiences and opinions on which is
superior.

Overall, the video is well-received, with viewers finding the content
informative and helpful for enhancing realism in MSFS 2024.


```

## Sample output 2 - Dunkey's Best of 2016

```
python yt-sum.py
Enter the YouTube URL: https://www.youtube.com/watch?v=7y9CLWJvia8

Starting metadata and subtitle downloads in parallel...

Extracting cookies from firefox
Extracted 2499 cookies from firefox
[youtube] Extracting URL: https://www.youtube.com/watch?v=7y9CLWJvia8
[youtube] 7y9CLWJvia8: Downloading webpage
[youtube] 7y9CLWJvia8: Downloading tv client config
[youtube] 7y9CLWJvia8: Downloading tv player API JSON
[info] 7y9CLWJvia8: Downloading subtitles: en
[info] 7y9CLWJvia8: Downloading 1 format(s): 399+251
[info] Writing video subtitles to: video_7y9CLWJvia8_628cd2.en.vtt
[download] Destination: video_7y9CLWJvia8_628cd2.en.vtt
[download] 100% of  101.88KiB in 00:00:01 at 99.60KiB/s
[SubtitlesConvertor] Converting subtitles
Deleting original file video_7y9CLWJvia8_628cd2.en.vtt (pass -k to keep)
Video title: Dunkey's Best of 2016

Summarizing chunk 1/1...

                                CHUNK 1 SUMMARY
================================================================================


CLICKBAIT RATING: None. The video title "Dunkey's Best of 2016" accurately
describes the content, which is a humorous and satirical review of video games
from 2016.

KEY POINTS:
1. Dunkey expresses disappointment with the gaming industry's tendency to
exploit player optimism, citing examples like "Hitman" and contrasting it with
more open-ended games like "Metal Gear Solid V."
2. Despite initial disappointments, Dunkey highlights several games from 2016
that he enjoyed, including "Ultimate Chicken Horse," "Color Splash," and
"Stardew Valley," among others.
3. The video humorously lists and reviews various games, both old and new, with
a comedic twist, ultimately naming "Super Mario Bros. 2" as the game of the year
in a satirical manner.

DETAILED SUMMARY:

INTRODUCTION AND DISAPPOINTMENTS:
Dunkey begins by discussing his high expectations for 2016, which were
ultimately unmet, highlighting how the gaming industry often exploits player
optimism. He mentions "Fable 2" as an example of over-promised features and
expresses disappointment with "Hitman," which started strong but became
restrictive over time, especially when compared to the freedom offered in "Metal
Gear Solid V."

HIGHLIGHTS OF 2016:
Despite initial disappointments, Dunkey reflects on the good games he played in
2016. He mentions "The Witness," "The Last Guardian," and "Ultimate Chicken
Horse," praising the latter for its simple yet competitive gameplay. He also
discusses "Color Splash," which recaptured some of the original "Paper Mario"
magic, and "Stardew Valley," a favorite of his partner Leah.

HUMOROUS REVIEWS AND LIST:
Dunkey humorously reviews several games, both old and new, with exaggerated
praise and comedic commentary. He highlights "Sonic the Hedgehog 3" for its
replayability and unique design, "Abzu" for its relaxing experience, and "Call
of Duty: Modern Warfare 2" for its chaotic multiplayer and engaging single-
player campaign. He also praises "Ratchet & Clank" for its weapons and gameplay,
"Overwatch" for its polish and excitement, and "Inside" for its compelling story
and unique narrative.

CONCLUSION:
The video concludes with a satirical twist, naming "Super Mario Bros. 2" as the
game of the year, humorously dismissing "Knack" and teasing a potential "Knack
3." Throughout, Dunkey maintains a comedic tone, blending genuine critique with
playful exaggeration.


Analyzing top comments...

                                COMMENT ANALYSIS
================================================================================


RECEPTION: POSITIVE

COMMON THEMES
- Nostalgia and re-watchability: Many comments mention that Dunkey's videos,
including his yearly top 10s, are enjoyable and re-watchable even years later.
- Humor and comedic genius: Dunkey is praised for his humor and comedic timing,
with several comments highlighting how funny and entertaining his content is.
- Insightful commentary: Viewers appreciate Dunkey's insightful commentary on
the video game industry, noting his ability to present ideas clearly and
humorously.

PRAISE
- Dunkey is celebrated for his ability to make thoughtful and passionate content
that remains engaging over time.
- His unique style of humor and commentary is consistently praised, with many
viewers expressing their admiration for his work.

CRITICISM
- Some comments jokingly criticize Dunkey for including games that didn't come
out in 2016 in his "Best of 2016" list, though this is mostly in jest.

JOKES
- Several comments contain jokes about Dunkey's recurring inclusion of Super
Mario Bros 2 as his game of the year.
- There are humorous remarks about the Halo music over Donkey Kong and the lack
of a Morgan Freeman voiceover in Abzu.

CONTROVERSY
- There is a minor controversy regarding the inclusion of games not released in
2016, but it is mostly treated humorously by the commenters.

OVERALL
The video was well-received, with viewers expressing enjoyment and appreciation
for Dunkey's humor, insight, and re-watchability of his content.
```

## Sample output 3 - Jordan Peterson vs 20 Atheists | Surrounded

```
python yt-sum.py
Enter the YouTube URL: https://www.youtube.com/watch?v=Pwk5MPE_6zE&t=2241s

Starting metadata and subtitle downloads in parallel...

Extracting cookies from firefox
Extracted 2499 cookies from firefox
[youtube] Extracting URL: https://www.youtube.com/watch?v=Pwk5MPE_6zE
[youtube] Pwk5MPE_6zE: Downloading webpage
[youtube] Pwk5MPE_6zE: Downloading tv client config
[youtube] Pwk5MPE_6zE: Downloading tv player API JSON
[info] Pwk5MPE_6zE: Downloading subtitles: en
[info] Pwk5MPE_6zE: Downloading 1 format(s): 399+251
[info] Writing video subtitles to: video_Pwk5MPE_6zE_55b20c.en.vtt
[download] Destination: video_Pwk5MPE_6zE_55b20c.en.vtt
[download] 100% of  854.32KiB in 00:00:00 at 864.43KiB/s
[SubtitlesConvertor] Converting subtitles
Deleting original file video_Pwk5MPE_6zE_55b20c.en.vtt (pass -k to keep)
Video title: Jordan Peterson vs 20 Atheists | Surrounded

Summarizing chunk 1/1...

                                CHUNK 1 SUMMARY
================================================================================


CLICKBAIT RATING: EXAGGERATED. The title suggests a confrontational debate
between Jordan Peterson and a large group of atheists, which is somewhat
accurate but dramatized for effect.

KEY POINTS:
1. Jordan Peterson argues that atheists reject God without fully understanding
what they are rejecting, leading to a discussion on the nature of God and
atheism.
2. The conversation explores the idea that morality and purpose cannot be
derived solely from science, suggesting that these concepts are inherently tied
to religious or spiritual beliefs.
3. The dialogue touches on the notion that everyone, including atheists,
worships something, as worship is defined as prioritizing and sacrificing for
something of value.

DETAILED SUMMARY:

INTRODUCTION
- The video begins with a heated exchange questioning Jordan Peterson's
religious beliefs, leading to his introduction as a clinical psychologist and
public speaker surrounded by atheists.
- Peterson's first claim is that atheists reject God without understanding what
they are rejecting.

DISCUSSION ON GOD AND ATHEISM
- An atheist with a background in Catholicism challenges Peterson's claim,
arguing that he has a deep understanding of what he left behind.
- Peterson suggests that atheists often have a reductive view of God and may
have been hurt by religious experiences.
- The conversation delves into defining God, with Peterson emphasizing the
complexity and unknowability of the divine.

MORALITY AND PURPOSE
- Peterson claims that morality and purpose cannot be found within science,
sparking a debate on whether moral frameworks can exist independently of
religious beliefs.
- Examples from animal behavior are used to argue that morality is intrinsic to
social animals, but Peterson counters that science must exist within a moral
framework not derived from science itself.

WORSHIP AND PRIORITIZATION
- The concept of worship is discussed, with Peterson defining it as prioritizing
and sacrificing for something, suggesting that everyone worships something.
- The conversation explores whether prioritizing relationships, like marriage,
constitutes worship.

CHRISTIAN MORALITY AND BIBLICAL INTERPRETATION
- The video addresses the interpretation of Christian morality and the Bible,
questioning whether Peterson's framework aligns with traditional Christian
teachings.
- The discussion includes the role of historical events in the Bible and their
significance for faith and morality.

CONCLUSION
- The video concludes with reflections on the nature of productive debate and
the importance of mutual exploration in discussions about faith and belief
systems.
- Participants express mixed feelings about Peterson's approach, noting his
ability to engage thoughtfully while also critiquing his definitional
flexibility.


Analyzing top comments...

                                COMMENT ANALYSIS
================================================================================


RECEPTION RATING: MIXED

COMMON THEMES
- Confusion about Jordan Peterson's religious stance and whether he is a
Christian.
- Criticism of Jubilee for the way the video was set up, with some feeling it
was a setup or ambush.
- Discussion about the title change from "1 Christian vs 20 Atheists" to "Jordan
Peterson vs 20 Atheists."
- Debate over whether Peterson was the right choice to represent Christianity in
this context.

PRAISE
- Some viewers appreciated Peterson's philosophical approach and his ability to
articulate complex ideas.
- A few comments noted that Peterson represented Christians in a way that some
might find favorable.

CRITICISM
- Many viewers criticized the video for not having a clear representation of a
Christian, suggesting that a pastor or theologian would have been more
appropriate.
- There was dissatisfaction with the debate format, as arguments often seemed
unresolved or circular.
- Some felt that the video was more about creating controversy than fostering
meaningful discussion.

JOKES
- Several comments made light of Peterson's debating style, particularly his
focus on definitions.
- Jokes about the title change and Peterson's ambiguous religious stance were
common.

CONTROVERSY
- The setup of the debate was controversial, with accusations that Jubilee set
Peterson up for failure.
- The choice of Peterson to represent Christianity sparked debate, as he has not
explicitly claimed to be a Christian.

OVERALL, the video received mixed reactions, with significant criticism
regarding the setup and execution of the debate, but also some appreciation for
Peterson's intellectual approach.
```

## Sample output 4 - Yandere Simulator Complete Source Code Analysis - Code Review

```
python yt-sum.py
Enter the YouTube URL: https://www.youtube.com/watch?v=LleJbZ3FOPU

Starting metadata and subtitle downloads in parallel...

Extracting cookies from firefox
Extracted 2503 cookies from firefox
[youtube] Extracting URL: https://www.youtube.com/watch?v=LleJbZ3FOPU
[youtube] LleJbZ3FOPU: Downloading webpage
[youtube] LleJbZ3FOPU: Downloading tv client config
[youtube] LleJbZ3FOPU: Downloading tv player API JSON
[info] LleJbZ3FOPU: Downloading subtitles: en
[info] LleJbZ3FOPU: Downloading 1 format(s): 399+251
[info] Writing video subtitles to: video_LleJbZ3FOPU_4e55ab.en.vtt
[download] Destination: video_LleJbZ3FOPU_4e55ab.en.vtt
[download] 100% of  440.83KiB in 00:00:02 at 217.17KiB/s
[SubtitlesConvertor] Converting subtitles
Deleting original file video_LleJbZ3FOPU_4e55ab.en.vtt (pass -k to keep)
Video title: Yandere Simulator Complete Source Code Analysis - Code Review

Summarizing chunk 1/1...

                                CHUNK 1 SUMMARY
================================================================================


CLICKBAIT RATING: None. The video delivers exactly what the title promises: a
comprehensive analysis and review of the Yandere Simulator's source code.

KEY POINTS:
1. The video provides an in-depth analysis of the Yandere Simulator's source
code, focusing on performance and architectural issues.
2. It identifies specific problems with the game's performance, such as
inefficient rendering and excessive use of public booleans, and suggests
potential optimizations.
3. The video discusses architectural concerns, proposing a more structured
approach to handling game logic and state management.

DETAILED SUMMARY:

INTRODUCTION:
- The video begins with the creator announcing the long-awaited code review of
Yandere Simulator, emphasizing the importance of not engaging in bullying.
- The creator explains the process of obtaining and analyzing the game's source
code, noting that they have been in communication with the game's developer,
Yandere Dev, to address some issues.

PERFORMANCE ANALYSIS:
- The creator uses various tools to benchmark the game's performance, noting
that the game struggles to maintain 60 FPS despite not fully utilizing CPU or
GPU resources.
- They identify rendering as a major bottleneck, with excessive geometry on
models and inefficient use of shaders contributing to poor performance.
- The video suggests optimizing assets, implementing proper level of detail
(LOD) systems, and improving occlusion culling to enhance performance.

ARCHITECTURAL ISSUES:
- The video critiques the game's architecture, noting that the code is cluttered
with public booleans and lacks a clear structure for managing game logic.
- The creator proposes a more object-oriented approach, where each character's
behavior is managed through a structured routine and state management system.
- They emphasize the need for refactoring the code to reduce technical debt and
improve maintainability.

IMPLEMENTATION DETAILS:
- The video discusses specific implementation details, such as the inefficient
handling of interaction prompts and the bloated save file format.
- It suggests using more efficient data structures and caching techniques to
reduce memory allocation and improve performance.
- The creator also highlights the potential benefits of using Unity's job system
for multi-threading and performance optimization.

CONCLUSION:
- The video concludes by reflecting on the impact of technical debt on the
game's development, noting that the architecture should have been refactored
years ago.
- The creator expresses hope that the analysis will help improve the game's
development process and encourages viewers to subscribe for more content.


Analyzing top comments...

                                COMMENT ANALYSIS
================================================================================


RECEPTION: POSITIVE

COMMON THEMES:
1. Technical Analysis: Many comments focus on the technical aspects of the
video, discussing draw calls, shaders, and optimization techniques. There is a
lot of engagement with the technical content presented in the video.
2. Educational Value: Viewers appreciate the educational content, with many
expressing that they learned a lot about programming and game development.
3. Criticism of Yandere Simulator: There is criticism of the game's code and
development practices, with some comments humorously pointing out inefficiencies
or poor coding decisions.
4. Praise for the Creator: The creator, dyc3, receives significant praise for
their knowledge, presentation skills, and the quality of the video. Viewers are
impressed by the editing, visuals, and the depth of analysis.
5. Working with Yandere Dev: There is curiosity and some skepticism about the
creator's collaboration with Yandere Dev, with mixed opinions on whether it's
beneficial or not.

PRAISE:
- The video is praised for its high educational value, with viewers appreciating
the deep dive into programming and game development.
- The creator's editing, presentation, and charisma are highlighted as standout
features.
- Many comments express surprise at the creator's relatively low subscriber
count given the quality of the content.

CRITICISM:
- Some technical inaccuracies are pointed out, such as the misunderstanding of
clock cycles and draw calls.
- There are minor criticisms of the video's structure, transitions, and text
usage, though these are generally outweighed by positive feedback.

JOKES:
- Several comments make light-hearted jokes about the inefficiencies in Yandere
Simulator's code, such as the toothbrush model with excessive polygons.
- There are humorous remarks about the creator's decision to analyze the code
despite implied discouragement.

CONTROVERSY:
- The involvement with Yandere Dev is a point of contention, with some viewers
questioning the decision to work with him due to his controversial reputation.

OVERALL, the video is well-received, with viewers appreciating both the
technical insights and the creator's engaging presentation style.
```
