from lib import *
import json
M=[]
TAGS='\n\n#ميزان_برو #محاماة'
# ---------- POST 10:00 — quote
post('p24_1000','''
<div class="glowc" style="width:900px;height:900px;left:-250px;top:150px"></div><img src="../logo.svg" style="position:absolute;left:60px;top:430px;width:330px;opacity:.10">
<div class="box" style="top:190px"><div class="gold" style="font-family:Messiri;font-size:220px;line-height:1;height:150px">”</div></div>
<div class="box" style="top:360px">
 <div style="font-size:90px;font-weight:900;line-height:1.28">الذاكرة ممكن<br><span class="gold">تخونك…</span></div>
 <div style="font-size:90px;font-weight:900;line-height:1.28;margin-top:14px">الملف المنظّم<br><span class="gold">لأ.</span></div>
 <div class="line" style="width:220px;margin:40px 0 0"></div>
</div>
''',pill='جملة النهارده',foot='ابعتها لزميل محتاجها')
M.append(dict(date='2026-10-24',time='10:00',kind='post',media=['p24_1000.png'],
 text='صباح الخير يا متر ☀️\n\n«الذاكرة ممكن تخونك… الملف المنظّم لأ.»\n\nكل تفصيلة في القضية تستاهل يكون لها مكان معروف تلاقيها فيه وقت ما تحتاجها.\nلو الجملة عجبتك ابعتها لزميل 🤝\nmezan.pro'+TAGS,
 idea='اقتباس تحفيزي: «الذاكرة ممكن تخونك… الملف المنظّم لأ»'))

# ---------- POST 12:00 — VIDEO problem/solution
video('v24_1200','''
<div class="sc" data-a="0" data-b="3.4">
 <div class="pill" data-fx="rise" data-at=".2" style="font-size:28px;margin-bottom:34px">موقف بيتكرر 😅</div>
 <div class="h1" data-fx="rise" data-at=".45" style="font-size:84px">فاضل ساعة<br>على الجلسة…</div>
 <div class="h1 gold" data-fx="stamp" data-at="1.3" style="font-size:96px;margin-top:10px">والورقة فين؟!</div>
</div>
<div class="sc" data-a="3.2" data-b="7">
 <div class="h2" data-fx="rise" data-at=".2">بتدوّر في…</div>
 <div class="row" style="margin-top:50px;gap:30px">
  <div class="glass card" data-fx="pop" data-at=".5" style="width:280px"><div style="font-size:80px">🗂️</div><div style="font-size:34px;font-weight:800;margin-top:10px">الدوسيهات</div></div>
  <div class="glass card" data-fx="pop" data-at=".8" style="width:280px"><div style="font-size:80px">🗄️</div><div style="font-size:34px;font-weight:800;margin-top:10px">الأدراج</div></div>
  <div class="glass card" data-fx="pop" data-at="1.1" style="width:280px"><div style="font-size:80px">💬</div><div style="font-size:34px;font-weight:800;margin-top:10px">الشات</div></div>
 </div>
 <div class="lead" data-fx="rise" data-at="1.8" style="margin-top:46px;font-size:40px">والوقت بيجري ⏳</div>
</div>
<div class="sc" data-a="6.8" data-b="11">
 <div class="pill" data-fx="rise" data-at=".2" style="font-size:28px;margin-bottom:30px">مع ميزان برو</div>
 <div class="glass" data-fx="pop" data-at=".5" style="width:760px;padding:34px 40px;text-align:right">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px"><span style="font-size:40px;font-weight:900">⚖️ ملف القضية</span><span class="tag">كل حاجة هنا</span></div>
  <div class="li glass" data-fx="left" data-at="1.0" style="padding:20px 24px;margin-bottom:16px"><div class="ic">📄</div><div class="t">مستندات القضية</div></div>
  <div class="li glass" data-fx="left" data-at="1.35" style="padding:20px 24px;margin-bottom:16px"><div class="ic">🤖</div><div class="t">ملخص بالذكاء الاصطناعي</div></div>
  <div class="li glass" data-fx="left" data-at="1.7" style="padding:20px 24px"><div class="ic">🔗</div><div class="t">الملخص مربوط بالملف</div></div>
 </div>
</div>
<div class="sc" data-a="10.8" data-b="13.4">
 <div class="h1" data-fx="rise" data-at=".2" style="font-size:90px">كل قضية…<br><span class="gold">في مكان واحد</span></div>
 <div class="lead" data-fx="rise" data-at=".8" style="margin-top:26px;font-size:38px">نظام إدارة متكامل لمكتب المحاماة</div>
</div>
<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div style="font-family:Messiri;font-size:96px;margin-top:16px" class="gold" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="btn" data-fx="pulse" data-at=".8" style="margin-top:34px;font-size:44px;padding:18px 50px">جرّب مجانًا 14 يوم</div>
 <div class="url" data-fx="rise" data-at="1.2" style="margin-top:34px;font-size:52px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
M.append(dict(date='2026-10-24',time='12:00',kind='post',video=dict(src='v24_1200',D=16,preset='em',seed=24,bpm=118,trans='3.2,6.8,10.8,13.2',pat=1),media=['v24_1200.mp4'],title='والورقة فين؟ | ميزان برو',
 text='فاضل ساعة على الجلسة… والورقة فين؟! 😅\n\nبدل ما تقلّب في الدوسيهات والأدراج والشات، في ميزان برو كل قضية ليها ملف واحد: المستندات، وملخص بالذكاء الاصطناعي مربوط بملف القضية.\n\nجرّب مجانًا 14 يوم 👈 mezan.pro'+TAGS,
 idea='فيديو موشن: مشكلة «الورقة فين قبل الجلسة» وحلها بملف القضية الواحد'))

# ---------- POST 18:00 — legal info: Art 15
post('p24_1800','''
<div class="box" style="top:170px">
 <div class="lead" style="font-size:30px;color:var(--gold2)">بتحسب الميعاد إزاي؟</div>
 <div class="h1" style="font-size:72px;margin-top:6px">يوم الإعلان<br><span class="gold">مبيتحسبش</span> من الميعاد</div>
</div>
<div class="box" style="top:480px">
 <div class="row" style="gap:12px;direction:rtl">
  <div class="glass" style="flex:1;padding:22px 10px;text-align:center;border-color:rgba(252,165,165,.5);background:rgba(252,165,165,.08)"><div style="font-size:24px;color:#fca5a5;font-weight:800">يوم الإعلان</div><div style="font-size:44px;font-weight:900;margin-top:6px">✗</div></div>
  <div class="glass" style="flex:1;padding:22px 10px;text-align:center;border-color:rgba(217,178,95,.7);background:rgba(217,178,95,.12)"><div style="font-size:24px;color:var(--gold2);font-weight:800">اليوم التالي</div><div style="font-size:44px;font-weight:900;margin-top:6px" class="gold">1</div></div>
  <div class="glass" style="flex:1;padding:22px 10px;text-align:center"><div style="font-size:24px;color:var(--mute);font-weight:800">بعده</div><div style="font-size:44px;font-weight:900;margin-top:6px">2</div></div>
  <div class="glass" style="flex:1;padding:22px 10px;text-align:center"><div style="font-size:24px;color:var(--mute);font-weight:800">بعده</div><div style="font-size:44px;font-weight:900;margin-top:6px">3</div></div>
  <div class="glass" style="flex:1;padding:22px 10px;text-align:center"><div style="font-size:24px;color:var(--mute);font-weight:800">…</div><div style="font-size:44px;font-weight:900;margin-top:6px">…</div></div>
 </div>
 <div class="glass" style="margin-top:34px;padding:26px 30px">
  <div style="font-size:27px;line-height:1.7;font-weight:600">📌 «إذا عين القانون للحضور أو لحصول الإجراء ميعادًا مقدرًا بالأيام أو بالشهور أو بالسنين فلا يحسب منه يوم الإعلان أو حدوث الأمر المعتبر في نظر القانون مجريًا للميعاد…»</div>
  <div class="small" style="margin-top:10px">المادة 15 — قانون المرافعات المدنية والتجارية</div>
 </div>
</div>''',pill='معلومة إجرائية ⚖️',foot='احفظها وشاركها مع زمايلك 🔖')
M.append(dict(date='2026-10-24',time='18:00',kind='post',media=['p24_1800.png'],
 text='معلومة إجرائية تهمك ⚖️\n\nلما تحسب ميعاد مقدّر بالأيام أو الشهور أو السنين… يوم الإعلان نفسه مبيتحسبش، العد بيبدأ من اليوم اللي بعده.\n\nالنص: «إذا عين القانون للحضور أو لحصول الإجراء ميعادًا مقدرًا بالأيام أو بالشهور أو بالسنين فلا يحسب منه يوم الإعلان أو حدوث الأمر المعتبر في نظر القانون مجريًا للميعاد» — المادة 15 من قانون المرافعات المدنية والتجارية.\n\nاحفظ البوست وابعته لزميل 🔖'+TAGS,
 idea='معلومة إجرائية: يوم الإعلان لا يُحسب من الميعاد (م.15 مرافعات)'))

# ---------- STORY 11:00 — VIDEO motivational/quote (12s)
video('sv24_1100','''
<div class="sc" data-a="0" data-b="4.2">
 <div style="font-size:150px" data-fx="pop" data-at=".1">☕</div>
 <div style="font-size:96px;font-weight:900;line-height:1.3;margin-top:30px" data-fx="rise" data-at=".5">السبت<br><span class="gold">بداية جديدة</span></div>
</div>
<div class="sc" data-a="4" data-b="8.2">
 <div style="font-size:84px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".2">ابدأ أسبوعك<br>بـ<span class="gold">ملف واحد</span><br>منظّم</div>
 <div class="line" data-fx="bar" data-at=".9" style="width:400px;margin:50px auto"></div>
 <div style="font-size:84px;font-weight:900;line-height:1.35" data-fx="rise" data-at="1.2">والباقي<br><span class="gold">هيمشي وراه</span></div>
</div>
<div class="sc" data-a="8" data-b="12.3">
 <img src="../logo.svg" width="200" data-fx="spin" data-at=".1">
 <div style="font-family:Messiri;font-size:110px;margin-top:20px" class="gold" data-fx="rise" data-at=".4">ميزان برو</div>
 <div style="font-size:48px;color:#c9d4ea;font-weight:700;margin-top:16px" data-fx="rise" data-at=".7">مكتبك كله في نظام واحد</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:60px;font-size:76px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
M.append(dict(date='2026-10-24',time='11:00',kind='story',video=dict(src='sv24_1100',D=12,preset='g',seed=241,bpm=126,trans='4,8',pat=2),media=['sv24_1100.mp4'],idea='قصة فيديو: «السبت بداية جديدة… ابدأ أسبوعك بملف واحد منظّم»'))

# ---------- STORY 15:00 — client tip: acknowledge
story('s24_1500','''
<div class="glowc" style="width:1100px;height:1100px;left:-10px;top:420px"></div>
<div class="pill" style="position:absolute;top:390px;left:50%;transform:translateX(-50%);font-size:30px">مع الموكلين 🤝</div>
<div class="center" style="position:absolute;top:500px;left:60px;right:60px">
 <div style="font-size:84px;font-weight:900;line-height:1.3">موكلك بعت ورقة؟<br>رد بكلمة <span class="gold">«وصلت»</span></div>
</div>
<div style="position:absolute;top:870px;left:120px;right:120px">
 <div style="display:flex;justify-content:flex-end"><div style="background:#22314f;border-radius:30px 30px 30px 6px;padding:26px 34px;font-size:40px;font-weight:700;max-width:640px">📎 صورة عقد الإيجار يا أستاذ</div></div>
 <div style="display:flex;justify-content:flex-start;margin-top:30px"><div style="background:linear-gradient(160deg,var(--gold2),var(--gold));color:var(--navy);border-radius:30px 30px 6px 30px;padding:26px 34px;font-size:40px;font-weight:800;max-width:640px">وصلت 👍 وهراجعها النهارده</div></div>
 <div style="display:flex;justify-content:flex-end;margin-top:30px"><div style="background:#22314f;border-radius:30px 30px 30px 6px;padding:26px 34px;font-size:40px;font-weight:700">🙏 تمام، متشكر</div></div>
</div>
<div class="center" style="position:absolute;top:1380px;left:80px;right:80px;font-size:46px;font-weight:800;color:#c9d4ea">كلمة واحدة… <span class="gold">وموكل مطمّن</span></div>
<div class="url center" style="position:absolute;top:1530px;left:0;right:0;font-size:64px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date='2026-10-24',time='15:00',kind='story',media=['s24_1500.png'],idea='قصة تعامل مع الموكلين: رد بكلمة «وصلت» على أي ورقة يبعتها الموكل'))

# ---------- STORY 20:30 — price
story('s24_2030','''
<div class="center" style="position:absolute;top:420px;left:60px;right:60px">
 <div style="font-size:92px;font-weight:900;line-height:1.3">ميزان برو<br><span class="gold">بكام؟</span></div>
</div>
<div style="position:absolute;top:720px;left:110px;right:110px">
 <div class="glass" style="padding:26px 50px;display:flex;justify-content:space-between;align-items:center"><span style="font-size:52px;font-weight:800">في الشهر</span><span class="gold" style="font-size:120px;font-weight:900;font-family:CairoL">200<small style="font-size:50px;font-family:Cairo"> ج</small></span></div>
 <div class="glass" style="margin-top:34px;padding:26px 50px;display:flex;justify-content:space-between;align-items:center;border-color:rgba(217,178,95,.7);background:linear-gradient(160deg,rgba(217,178,95,.2),rgba(217,178,95,.05))"><span style="font-size:52px;font-weight:800">في السنة</span><span class="gold" style="font-size:120px;font-weight:900;font-family:CairoL">2000<small style="font-size:50px;font-family:Cairo"> ج</small></span></div>
 <div class="center" style="margin-top:50px;font-size:48px;font-weight:800;color:#c9d4ea">وقبلها <span class="gold">14 يوم تجربة مجانية</span></div>
</div>
<div class="center" style="position:absolute;top:1490px;left:0;right:0"><span class="btn url" style="font-size:62px;padding:22px 64px">mezan.pro</span></div>''')
M.append(dict(date='2026-10-24',time='20:30',kind='story',media=['s24_2030.png'],idea='قصة أسعار: 200 ج شهري / 2000 ج سنوي + 14 يوم مجانًا'))
json.dump(M,open('m24.json','w'),ensure_ascii=False,indent=1)
print('ok')
