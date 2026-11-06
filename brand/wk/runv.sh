#!/bin/bash
cd "$(dirname "$0")"
read n D preset seed bpm trans pat <<< "$1"
[ -f out/$n.mp4 ] || { python3 music_gen.py out/$n.wav $D $preset $seed $bpm "$trans" $pat >/dev/null && python3 rend.py vid $n $D; }
