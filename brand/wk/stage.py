import json,shutil,os
R='/home/claude/mezan.media';BASE='https://raw.githubusercontent.com/omaryamany/mezan.media/main/'
allm=[]
for d in range(24,31):
    for m in json.load(open(f'm{d}.json')):
        date=m['date'];mmdd=date[5:].replace('-','-');hhmm=m['time'].replace(':','')
        urls=[]
        for i,f in enumerate(m['media']):
            ext=f.split('.')[-1]
            if m['kind']=='post':
                suf=f'_{i+1}' if len(m['media'])>1 else ''
                rel=f'{date}/mizan_{date[5:]}_{hhmm}{suf}.{ext}'
            else:
                rel=f'{date}/stories/story_{hhmm}.{ext}'
            os.makedirs(os.path.dirname(f'{R}/{rel}'),exist_ok=True)
            shutil.copy(f'out/{f}',f'{R}/{rel}');urls.append(BASE+rel)
        m['urls']=urls;allm.append(m)
json.dump(allm,open('final.json','w'),ensure_ascii=False,indent=1);print(len(allm))
