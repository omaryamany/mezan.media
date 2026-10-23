from lib import *
import json
M=[];D8='2026-10-30'
TAGS='\n\n#ميزان_برو #محاماة'
# ---------- POST 10:00 — carousel: Friday review
post('p30_1000_1','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:200px"></div>
<div class="center" style="position:absolute;top:210px;left:60px;right:60px">
 <div style="display:inline-grid;place-items:center;width:200px;height:200px;border-radius:40px;background:rgba(217,178,95,.12);border:2px solid rgba(217,178,95,.5);font-size:110px">🪞</div>
 <div class="h1" style="font-size:82px;margin-top:30px">مراجعة <span class="gold">الجمعة</span></div>
 <div class="lead" style="margin-top:14px;font-size:34px">3 أسئلة لنفسك… في 10 دقايق</div>
</div>''',pill='نصيحة تنظيم 🗓️',foot='اسحب ← للأسئلة',dots=(1,3))
post('p30_1000_2','''
<div class="box col" style="top:215px;gap:50px">
 <div class="glass" style="padding:56px 44px"><div class="row" style="align-items:center"><div class="num" style="width:70px;height:70px;font-size:38px">1</div><div style="font-size:46px;font-weight:900">إيه اللي <span class="gold">خلص</span> الأسبوع ده؟ ✅</div></div><div class="lead" style="font-size:28px;margin-top:14px">اكتبه… علشان تشوف إنك اتحركت فعلًا.</div></div>
 <div class="glass" style="padding:56px 44px"><div class="row" style="align-items:center"><div class="num" style="width:70px;height:70px;font-size:38px">2</div><div style="font-size:46px;font-weight:900">إيه اللي <span class="gold">اتأخر</span>… وليه؟ ⏳</div></div><div class="lead" style="font-size:28px;margin-top:14px">مستني حد؟ ولا محتاج وقت أكتر من المتوقع؟</div></div>
</div>''',foot='اسحب ←',dots=(2,3))
post('p30_1000_3','''
<div class="box" style="top:200px">
 <div class="glass" style="padding:50px 44px;border-color:rgba(217,178,95,.6)"><div class="row" style="align-items:center"><div class="num" style="width:70px;height:70px;font-size:38px">3</div><div style="font-size:46px;font-weight:900">إيه أهم <span class="gold">3 حاجات</span><br>في الأسبوع الجاي؟ 🎯</div></div>
 <div class="col" style="margin-top:26px;gap:22px;font-size:36px;font-weight:700"><div>☐ ……………………</div><div>☐ ……………………</div><div>☐ ……………………</div></div></div>
</div>
<div class="box center" style="top:810px"><div style="font-size:34px;font-weight:800">وتبدأ الأسبوع <span class="gold">عارف رايح فين</span> 💪</div><div class="small" style="margin-top:8px;font-size:26px">احفظ البوست 🔖 · <span class="url">mezan.pro</span></div></div>''',foot='',dots=(3,3))
M.append(dict(date=D8,time='10:00',kind='post',media=['p30_1000_1.png','p30_1000_2.png','p30_1000_3.png'],
 text='مراجعة الجمعة 🪞 — 3 أسئلة لنفسك في 10 دقايق:\n\n1️⃣ إيه اللي خلص الأسبوع ده؟ ✅\n2️⃣ إيه اللي اتأخر… وليه؟ ⏳\n3️⃣ إيه أهم 3 حاجات في الأسبوع الجاي؟ 🎯\n\nوتبدأ الأسبوع عارف رايح فين 💪\nاحفظ البوست 🔖 وجرّبها النهارده.\nmezan.pro'+TAGS,
 idea='كاروسيل 3 صور: «مراجعة الجمعة» 3 أسئلة لتنظيم الأسبوع'))

# ---------- POST 12:00 — VIDEO quotes
video('v30_1200','''
<div class="sc" data-a="0" data-b="3">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:30px">جُمل للمحامي ✨</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:96px;margin-top:30px">3 جمل<br><span class="gold">للأسبوع الجاي</span></div>
</div>
<div class="sc" data-a="2.8" data-b="6.4">
 <div class="gold" style="font-family:Messiri;font-size:200px;line-height:.8;height:120px" data-fx="fade" data-at=".1">“</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:74px">اقرا القضية كأنك <span class="gold">الخصم</span>…<br>وحضّرها كأنك <span class="gold">القاضي</span></div>
</div>
<div class="sc" data-a="6.2" data-b="9.8">
 <div class="gold" style="font-family:Messiri;font-size:200px;line-height:.8;height:120px" data-fx="fade" data-at=".1">“</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:74px">المحامي المنظّم<br><span class="gold">بيكسب وقت</span>…<br>والوقت <span class="gold">بيكسب قضايا</span></div>
</div>
<div class="sc" data-a="9.6" data-b="13.2">
 <div class="gold" style="font-family:Messiri;font-size:200px;line-height:.8;height:120px" data-fx="fade" data-at=".1">“</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:74px">كل ملف مترتّب…<br><span class="gold">رسالة احترام لموكلك</span></div>
</div>
<div class="sc" data-a="13" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:90px;margin-top:16px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px">جمعة هادية يا متر 🤍</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
M.append(dict(date=D8,time='12:00',kind='post',video=dict(src='v30_1200',D=16,preset='a',seed=30,bpm=92,trans='2.8,6.2,9.6,13',pat=0),media=['v30_1200.mp4'],title='3 جمل للمحامي | ميزان برو',
 text='3 جمل للأسبوع الجاي ✨\n\n«اقرا القضية كأنك الخصم… وحضّرها كأنك القاضي»\n«المحامي المنظّم بيكسب وقت… والوقت بيكسب قضايا»\n«كل ملف مترتّب… رسالة احترام لموكلك»\n\nأنهي جملة فيهم أقرب لك؟ قولنا في الكومنتات 👇\nجمعة هادية يا متر 🤍\nmezan.pro'+TAGS,
 idea='فيديو موشن: 3 جمل تحفيزية للمحامي للأسبوع الجاي'))

# ---------- POST 18:00 — client tip: call notes
post('p30_1800','''
<div class="box" style="top:170px"><div class="h1" style="font-size:66px">خلصت مكالمة مع موكلك؟</div><div class="h1" style="font-size:66px"><span class="gold">اكتبها في ملف قضيته فورًا</span> ✍️</div></div>
<div class="box row" style="top:430px;gap:26px;align-items:center">
 <div class="glass" style="flex:none;width:300px;padding:30px;text-align:center"><div style="font-size:90px">📞</div><div style="font-size:30px;font-weight:800;margin-top:8px">مكالمة 5 دقايق</div></div>
 <div style="font-size:60px;color:var(--gold2);font-family:CairoL">←</div>
 <div class="paper" style="flex:1;padding:28px 30px">
  <div style="font-size:26px;font-weight:900;color:#8a6a2c;margin-bottom:10px">📝 ملاحظة مكالمة</div>
  <div style="font-size:26px;font-weight:700;line-height:1.85">• التاريخ: …<br>• قال إيه باختصار: …<br>• اتفقنا على إيه: …<br>• المطلوب ومين هيعمله: …</div>
 </div>
</div>
<div class="box center" style="top:850px;font-size:30px;font-weight:800">اللي مش مكتوب… <span class="gold">كأنه محصلش</span></div>''',pill='مع الموكلين 🤝',foot='احفظ القالب 🔖')
M.append(dict(date=D8,time='18:00',kind='post',media=['p30_1800.png'],
 text='خلصت مكالمة مع موكلك؟ اكتبها في ملف قضيته فورًا ✍️\n\nقالب سريع:\n• التاريخ\n• قال إيه باختصار\n• اتفقنا على إيه\n• المطلوب ومين هيعمله\n\nلأن اللي مش مكتوب… كأنه محصلش.\nاحفظ القالب 🔖\nmezan.pro'+TAGS,
 idea='نصيحة تعامل مع الموكلين: اكتب ملاحظات المكالمة في ملف القضية (قالب 4 سطور)'))

# ---------- STORY 11:00 — Friday greeting
story('s30_1100','''
<div class="glowc" style="width:1200px;height:1200px;left:-60px;top:300px"></div>
<div class="center" style="position:absolute;top:420px;left:0;right:0;font-size:220px">🤍</div>
<div class="center" style="position:absolute;top:760px;left:60px;right:60px">
 <div style="font-size:110px;font-weight:900;line-height:1.3">جمعة هادية<br><span class="gold">يا متر</span></div>
 <div class="line" style="width:300px;margin:50px auto"></div>
 <div style="font-size:50px;color:#c9d4ea;font-weight:700;line-height:1.6">ريّح دماغك النهارده…<br>والشغل يستناك بكرة</div>
</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:58px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='11:00',kind='story',media=['s30_1100.png'],idea='قصة مناسبة: «جمعة هادية يا متر… ريّح دماغك النهارده»'))

# ---------- STORY 15:00 — VIDEO poll
video('sv30_1500','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🪄</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">لو تقدر تخفي<br><span class="gold">حاجة واحدة</span><br>من مكتبك…</div>
</div>
<div class="sc" data-a="3.4" data-b="8.6">
 <div style="font-size:64px;font-weight:900" data-fx="rise" data-at=".1">هتختار إيه؟</div>
 <div class="col" style="width:100%;gap:30px;margin-top:50px">
  <div class="glass li" data-fx="right" data-at=".5" style="padding:34px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">1</div><div class="t" style="font-size:52px">كوم الورق 🗄️</div></div>
  <div class="glass li" data-fx="right" data-at="1" style="padding:34px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">2</div><div class="t" style="font-size:52px">التدوير على المستندات 🔍</div></div>
  <div class="glass li" data-fx="right" data-at="1.5" style="padding:34px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">3</div><div class="t" style="font-size:52px">نسيان المواعيد ⏰</div></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:80px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">ابعتلنا <span class="gold">رقمك</span><br>في رسالة 📩</div>
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
M.append(dict(date=D8,time='15:00',kind='story',video=dict(src='sv30_1500',D=12,preset='dm',seed=301,bpm=108,trans='3.4,8.4',pat=1),media=['sv30_1500.mp4'],idea='قصة فيديو تفاعلية: لو تقدر تخفي حاجة واحدة من مكتبك… هتختار إيه؟'))

# ---------- STORY 20:30 — feature in 3 words
story('s30_2030','''
<div class="center" style="position:absolute;top:400px;left:60px;right:60px"><div style="font-size:76px;font-weight:900;line-height:1.3">ميزان برو<br>في <span class="gold">3 كلمات</span></div></div>
<div style="position:absolute;top:700px;left:110px;right:110px" class="col">
 <div class="glass" style="padding:28px 40px;display:flex;align-items:center;gap:34px"><div class="ic" style="width:110px;height:110px;font-size:60px">🗂️</div><div><div class="gold" style="font-size:64px;font-weight:900">ينظّم</div><div style="font-size:34px;color:var(--mute)">مكتبك في نظام واحد</div></div></div>
 <div class="glass" style="padding:28px 40px;display:flex;align-items:center;gap:34px"><div class="ic" style="width:110px;height:110px;font-size:60px">🤖</div><div><div class="gold" style="font-size:64px;font-weight:900">يلخّص</div><div style="font-size:34px;color:var(--mute)">أوراق القضية بالذكاء الاصطناعي</div></div></div>
 <div class="glass" style="padding:28px 40px;display:flex;align-items:center;gap:34px"><div class="ic" style="width:110px;height:110px;font-size:60px">🔒</div><div><div class="gold" style="font-size:64px;font-weight:900">يحمي</div><div style="font-size:34px;color:var(--mute)">سرية بياناتك أولوية</div></div></div>
</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='20:30',kind='story',media=['s30_2030.png'],idea='قصة مزايا: ميزان برو في 3 كلمات — ينظّم · يلخّص · يحمي'))
json.dump(M,open('m30.json','w'),ensure_ascii=False,indent=1);print('ok')
