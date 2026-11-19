#!/usr/bin/env python3
"""Split the two Season 2 story recordings into one file per scene line.

Usage: python3 tools/split_story.py NARRATOR.mp3 STORMKEEPER.mp3
       python3 tools/split_story.py BOTH_SPEAKERS.mp3   (all 10 lines in one recording)

The narrator recording must contain the 9 narrator lines in order, with a pause of
at least 1.5 seconds between lines. This script finds those pauses and writes
01_narrator.mp3 ... 09_narrator.mp3 (with 06a for the sixth line) into assets/audio/story/.
The stormkeeper recording is a single line; its silence is trimmed and it is saved as 06b_stormkeeper.mp3.
"""
import os, re, subprocess, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'audio', 'story')
NAMES = ['01_narrator', '02_narrator', '03_narrator', '04_narrator', '05_narrator',
         '06a_narrator', '07_narrator', '08_narrator', '09_narrator']
# one recording with both speakers (narrator + stormkeeper as a second speaker)
NAMES_ALL = NAMES[:6] + ['06b_stormkeeper'] + NAMES[6:]


def duration(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def silences(path, noise, min_len):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', path, '-af', f'silencedetect=noise={noise}dB:d={min_len}', '-f', 'null', '-'],
                       capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r.stderr)]
    ends = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r.stderr)]
    return list(zip(starts, ends))


def cut(src, a, b, dst):
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', src, '-ss', f'{a:.3f}', '-to', f'{b:.3f}',
                    '-af', 'afade=t=in:d=0.03,areverse,afade=t=in:d=0.08,areverse', '-codec:a', 'libmp3lame', '-q:a', '2', dst], check=True)


def split_narrator(src, names=NAMES):
    total = duration(src)
    need = len(names) - 1
    # try stricter or looser settings until exactly 8 pauses separate 9 lines
    for min_len in (1.5, 1.2, 1.0, 0.8, 2.0, 2.5, 0.6):
        for noise in (-40, -35, -45, -30, -50):
            gaps = [(s, e) for s, e in silences(src, noise, min_len) if s > 0.3 and e < total - 0.3]
            if len(gaps) == need:
                bounds, prev = [], 0.0
                for s, e in gaps:
                    bounds.append((prev, s + 0.15))
                    prev = max(s, e - 0.15)
                bounds.append((prev, total))
                for name, (a, b) in zip(names, bounds):
                    cut(src, a, b, os.path.join(OUT, name + '.mp3'))
                    print(f'{name}.mp3  {a:6.2f}s - {b:6.2f}s')
                return True
            print(f'  pauses >= {min_len}s at {noise} dB: found {len(gaps)}, need {need}')
    print(f'Could not find exactly {need} pauses. Re-record with a clear pause (about 2 seconds) between each line.')
    return False


def trim_single(src, name):
    total = duration(src)
    sil = silences(src, -40, 0.3)
    a = sil[0][1] - 0.1 if sil and sil[0][0] < 0.05 else 0.0
    b = sil[-1][0] + 0.15 if sil and sil[-1][1] > total - 0.05 else total
    cut(src, max(0.0, a), min(total, b), os.path.join(OUT, name + '.mp3'))
    print(f'{name}.mp3  {a:6.2f}s - {b:6.2f}s')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    os.makedirs(OUT, exist_ok=True)
    ok = split_narrator(sys.argv[1], NAMES if len(sys.argv) > 2 else NAMES_ALL)
    if len(sys.argv) > 2:
        trim_single(sys.argv[2], '06b_stormkeeper')
    sys.exit(0 if ok else 2)
