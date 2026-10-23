#!/bin/bash
# usage: mkvid.sh mfile.json  -> renders all videos in manifest
cd "$(dirname "$0")"
python3 - "$1" <<'PY' | while read n D preset seed bpm trans pat; do
import json,sys
for m in json.load(open(sys.argv[1])):
  v=m.get('video')
  if v: print(v['src'],v['D'],v['preset'],v['seed'],v['bpm'],v['trans'],v['pat'])
PY
  [ -f out/$n.mp4 ] || { python3 music_gen.py out/$n.wav $D $preset $seed $bpm "$trans" $pat >/dev/null </dev/null && python3 rend.py vid $n $D </dev/null; }
done
