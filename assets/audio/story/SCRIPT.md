# Season 2 story: voice-over script

Make each line in ElevenLabs, download it as MP3, and save it in this folder with the exact file name shown.
The game plays a recording if it finds the file here. Otherwise it uses the computer's built-in voice.
Each scene waits until its line has finished, so the length of a line doesn't matter.

Optional: put a music track here named `music.mp3`. It replaces the game's built-in score.

## Voices

| Role | Suggested ElevenLabs voice | Settings |
|---|---|---|
| Narrator | **George** (warm British storyteller). Alternatives: **Brian** (deep American) or **Daniel** (steady British) | Stability 40%, Similarity 75%, Style 35%, Speaker boost on |
| Stormkeeper | **Callum** (husky, menacing). Alternative: **Clyde** (gravelly) | Stability 30%, Similarity 80%, Style 55%, Speaker boost on |

Model: Eleven Multilingual v2, or Eleven v3 if you want to add audio tags such as `[whispers]` or `[slowly]`.
Pace: slow and cinematic, like a movie trailer. Leave the pauses where the punctuation is.

## Quick way: two recordings

Paste each block below into ElevenLabs (model **Eleven Multilingual v2**), download the MP3s, then run:

```
python3 tools/split_story.py ~/Downloads/narrator.mp3 ~/Downloads/stormkeeper.mp3
```

The splitter cuts the narrator recording at the long pauses, the 2.5-second breaks, and saves all 10 files here.
Keep the `<break>` tags exactly as written. Pauses inside a line must stay short, about 1 second, so a line isn't split in two.

**Recording 1: narrator.mp3** (Narrator voice, 9 lines)

```
Fifty of us dropped onto Stormfall Island. One walked out. That was you... the champion of Season One.
<break time="2.5s" />
But a crown was not enough. Everyone said the storm was just weather. You knew better. So you followed the lightning... to the edge of the world.
<break time="2.5s" />
There it was. The Storm Engine. The machine that built every storm... and kept every one of us trapped inside the circle.
<break time="2.5s" />
One swing to set everyone free. That was the plan.
<break time="2.5s" />
The Engine cracked, and the ocean came pouring through. By sunrise, the old shores were gone. The Deep Tide had arrived.
<break time="2.5s" />
They came before the water settled. The Stormkeepers.
<break time="2.5s" />
Back onto the flying ship, with forty-nine others who broke the rules. Every match is another round in the storm you shattered.
<break time="2.5s" />
So jump when you're ready. Glide in with your squad, or go it alone. Loot fast. Build faster.
<break time="2.5s" />
Stay inside the circle. Outlast them all. Because the last one standing... walks free. <break time="1.0s" /> Stormfall. Season Two. Deep Tide.
```

**Recording 2: stormkeeper.mp3** (Stormkeeper voice, 1 line)

```
You broke the storm, champion. So now... you will live inside it.
```

## Script (one file per line)

| File | Scene | Voice | Line |
|---|---|---|---|
| `01_narrator.mp3` | The final circle (the champion on the hill) | Narrator | Fifty of us dropped onto Stormfall Island. One walked out. That was you... the champion of Season One. |
| `02_narrator.mp3` | Walking to the cliffs | Narrator | But a crown was not enough. Everyone said the storm was just weather. You knew better. So you followed the lightning... to the edge of the world. |
| `03_narrator.mp3` | The Storm Engine | Narrator (quiet, in awe) | There it was. The Storm Engine. The machine that built every storm... and kept every one of us trapped inside the circle. |
| `04_narrator.mp3` | The swing | Narrator (calm, then heavy) | One swing to set everyone free. That was the plan. |
| `05_narrator.mp3` | The Deep Tide (the flood) | Narrator (grave) | The Engine cracked, and the ocean came pouring through. By sunrise, the old shores were gone. The Deep Tide had arrived. |
| `06a_narrator.mp3` | The Stormkeepers arrive | Narrator (tense) | They came before the water settled. The Stormkeepers. |
| `06b_stormkeeper.mp3` | The sentence is spoken | Stormkeeper (cold, slow) | You broke the storm, champion. So now... you will live inside it. |
| `07_narrator.mp3` | The flying ship | Narrator | Back onto the flying ship, with forty-nine others who broke the rules. Every match is another round in the storm you shattered. |
| `08_narrator.mp3` | The drop (gliding in with the squad) | Narrator (building energy) | So jump when you're ready. Glide in with your squad, or go it alone. Loot fast. Build faster. |
| `09_narrator.mp3` | Title: Season 2, Deep Tide | Narrator (big trailer finish) | Stay inside the circle. Outlast them all. Because the last one standing... walks free. [pause] Stormfall. Season Two. Deep Tide. |
