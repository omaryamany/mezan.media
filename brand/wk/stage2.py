import json,shutil,os
R='/home/claude/mezan.media';BASE='https://raw.githubusercontent.com/omaryamany/mezan.media/main/'
allm=[]
for f in ['mw1.json','mw2.json']:
    for m in json.load(open(f)):
        date=m['date'];hhmm=m['time'].replace(':','');urls=[]
        for i,fn in enumerate(m['media']):
            ext=fn.split('.')[-1]
            if m['kind']=='post':
                suf=f'_{i+1}' if len(m['media'])>1 else ''
                rel=f'{date}/mizan_{date[5:]}_{hhmm}{suf}.{ext}'
            else: rel=f'{date}/stories/story_{hhmm}.{ext}'
            os.makedirs(os.path.dirname(f'{R}/{rel}'),exist_ok=True)
            shutil.copy(f'out/{fn}',f'{R}/{rel}');urls.append(BASE+rel)
        m['urls']=urls;allm.append(m)
json.dump(allm,open('final2.json','w'),ensure_ascii=False,indent=1);print(len(allm))
