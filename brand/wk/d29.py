from lib import *
import json
M=[];D8='2026-10-29'
TAGS='\n\n#ميزان_برو #محاماة'
# ---------- POST 10:00 — AI safety: upload only what you need
post('p29_1000','''
<div class="box" style="top:160px"><div class="h1" style="font-size:70px">ارفع <span class="gold">اللي محتاجه</span><br>بس ✂️</div>
<div class="lead" style="font-size:29px;margin-top:16px">قبل ما تستخدم أي أداة ذكاء اصطناعي عامة:</div></div>
<div class="box row" style="top:480px;gap:22px;align-items:stretch">
 <div class="glass" style="flex:1;padding:28px;border-color:rgba(252,165,165,.45)">
  <div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5">بدل كده ✗</div>
  <div style="font-size:60px;margin-top:14px">🗂️</div>
  <div style="font-size:30px;font-weight:800;margin-top:8px;line-height:1.5">ترفع ملف القضية كله<br>علشان سؤال في عقد واحد</div>
 </div>
 <div class="glass" style="flex:1;padding:28px;border-color:rgba(134,239,172,.45)">
  <div class="tag" style="background:rgba(134,239,172,.15);color:#86efac">اعمل كده ✓</div>
  <div style="font-size:60px;margin-top:14px">📄</div>
  <div style="font-size:30px;font-weight:800;margin-top:8px;line-height:1.5">الجزء المطلوب بس…<br>ومن غير بيانات شخصية</div>
 </div>
</div>
<div class="box center" style="top:850px;font-size:30px;font-weight:800">بيانات موكلك <span class="gold">أمانة</span> 🔒</div>''',pill='الذكاء الاصطناعي بأمان 🤖',foot='احفظ النصيحة 🔖')
M.append(dict(date=D8,time='10:00',kind='post',media=['p29_1000.png'],
 text='ارفع اللي محتاجه بس ✂️\n\nقبل ما تستخدم أي أداة ذكاء اصطناعي عامة في شغلك:\n✗ متدّيهاش ملف القضية كله علشان سؤال في عقد واحد\n✓ اديها الجزء المطلوب بس… ومن غير البيانات الشخصية\n\nبيانات موكلك أمانة 🔒\nاحفظ النصيحة وشاركها مع زميلك.\nmezan.pro'+TAGS,
 idea='نصيحة ذكاء اصطناعي بأمان: ارفع الجزء اللي محتاجه بس ومن غير بيانات شخصية'))

# ---------- POST 12:00 — VIDEO feature: whole office in one system
video('v29_1200','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="position:relative;width:560px;height:400px">
  <div class="glass" data-fx="pop" data-at=".1" style="position:absolute;right:0;top:0;padding:18px 26px;font-size:34px;font-weight:800">⚖️ قضايا</div>
  <div class="glass" data-fx="pop" data-at=".35" style="position:absolute;left:0;top:40px;padding:18px 26px;font-size:34px;font-weight:800">📄 مستندات</div>
  <div class="glass" data-fx="pop" data-at=".6" style="position:absolute;right:60px;top:170px;padding:18px 26px;font-size:34px;font-weight:800">📝 ملخصات</div>
  <div class="glass" data-fx="pop" data-at=".85" style="position:absolute;left:40px;top:260px;padding:18px 26px;font-size:34px;font-weight:800">👥 موكلين</div>
 </div>
 <div class="h1" data-fx="rise" data-at="1.3" style="font-size:76px;margin-top:20px">كل ده… <span class="gold">فين؟</span></div>
</div>
<div class="sc" data-a="3.4" data-b="7.2">
 <img src="../logo.svg" width="200" data-fx="spin" data-at=".1">
 <div class="h1" data-fx="rise" data-at=".5" style="font-size:84px;margin-top:24px">في <span class="gold">نظام واحد</span></div>
 <div class="lead" data-fx="rise" data-at="1" style="font-size:40px;margin-top:14px">نظام إدارة متكامل (ERP) لمكاتب المحاماة</div>
</div>
<div class="sc" data-a="7" data-b="13">
 <div class="col" style="width:820px;gap:24px">
  <div class="glass li" data-fx="left" data-at=".2" style="padding:26px 32px"><div class="ic">🤖</div><div style="text-align:right"><div class="t" style="font-size:40px">تلخيص بالذكاء الاصطناعي</div><div class="d" style="font-size:28px">لأوراق ومستندات القضايا</div></div></div>
  <div class="glass li" data-fx="left" data-at="1.4" style="padding:26px 32px"><div class="ic">🔗</div><div style="text-align:right"><div class="t" style="font-size:40px">الملخص مربوط بالقضية</div><div class="d" style="font-size:28px">بيتربط بملف القضية نفسها</div></div></div>
  <div class="glass li" data-fx="left" data-at="2.6" style="padding:26px 32px"><div class="ic">🔒</div><div style="text-align:right"><div class="t" style="font-size:40px">سرية البيانات أولوية</div><div class="d" style="font-size:28px">بياناتك وبيانات موكلينك</div></div></div>
 </div>
</div>
<div class="sc" data-a="12.8" data-b="16.4">
 <div class="gold" style="font-family:Messiri;font-size:100px" data-fx="rise" data-at=".1">ميزان برو</div>
 <div class="btn" data-fx="pulse" data-at=".6" style="margin-top:30px;font-size:44px;padding:16px 50px">جرّب مجانًا 14 يوم</div>
 <div class="url" data-fx="rise" data-at="1" style="margin-top:32px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
M.append(dict(date=D8,time='12:00',kind='post',video=dict(src='v29_1200',D=16,preset='g',seed=29,bpm=124,trans='3.4,7,12.8',pat=3),media=['v29_1200.mp4'],title='مكتبك في نظام واحد | ميزان برو',
 text='قضايا، مستندات، ملخصات، موكلين… كل ده فين؟ 🤔\n\nفي ميزان برو: نظام إدارة متكامل (ERP) لمكاتب المحاماة.\n🤖 تلخيص أوراق ومستندات القضايا بالذكاء الاصطناعي\n🔗 الملخص بيتربط بملف القضية\n🔒 سرية بياناتك وبيانات موكلينك أولوية\n\nجرّب مجانًا 14 يوم 👈 mezan.pro'+TAGS,
 idea='فيديو موشن: مزايا النظام — مكتبك كله في نظام واحد (ERP + تلخيص + سرية)'))

# ---------- POST 18:00 — poll: first step on new case
post('p29_1800','''
<div class="box" style="top:160px"><div class="lead" style="font-size:30px;color:var(--gold2)">يا متر… 👇</div><div class="h1" style="font-size:66px;margin-top:4px">قضية جديدة وصلتك،<br><span class="gold">أول حاجة</span> بتعملها؟</div></div>
<div class="box col" style="top:440px;gap:16px">
 <div class="glass li" style="padding:18px 26px"><div class="num">أ</div><div class="t">تقرا الورق كله من الأول</div><div style="margin-right:auto;font-size:38px">📚</div></div>
 <div class="glass li" style="padding:18px 26px"><div class="num">ب</div><div class="t">تقعد مع الموكل تسمع منه</div><div style="margin-right:auto;font-size:38px">🗣️</div></div>
 <div class="glass li" style="padding:18px 26px"><div class="num">ج</div><div class="t">تفتح لها ملف وترتّب الورق</div><div style="margin-right:auto;font-size:38px">📂</div></div>
 <div class="glass li" style="padding:18px 26px"><div class="num">د</div><div class="t">تحدد المواعيد المهمة</div><div style="margin-right:auto;font-size:38px">📅</div></div>
</div>''',pill='شاركنا 💬',foot='اكتب الحرف في الكومنتات ✍️')
M.append(dict(date=D8,time='18:00',kind='post',media=['p29_1800.png'],
 text='يا متر… قضية جديدة وصلتك، أول حاجة بتعملها؟ 👇\n\nأ) تقرا الورق كله من الأول 📚\nب) تقعد مع الموكل تسمع منه 🗣️\nج) تفتح لها ملف وترتّب الورق 📂\nد) تحدد المواعيد المهمة 📅\n\nاكتب الحرف في الكومنتات ✍️'+TAGS,
 idea='سؤال تفاعلي: قضية جديدة وصلتك… أول حاجة بتعملها؟'))

# ---------- STORY 11:00 — VIDEO trial countdown
video('sv29_1100','''
<div class="sc" data-a="0" data-b="4.4">
 <div style="font-size:60px;font-weight:800;color:#c9d4ea" data-fx="rise" data-at=".1">جرّب ميزان برو</div>
 <div style="width:560px;height:560px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;margin-top:50px;border:5px solid rgba(217,178,95,.75);background:radial-gradient(circle at 50% 35%,rgba(243,217,152,.22),rgba(217,178,95,.05) 65%);box-shadow:0 0 0 26px rgba(217,178,95,.07),0 0 140px rgba(217,178,95,.35)" data-fx="pop" data-at=".3">
  <div class="gold" style="font-family:CairoL;font-size:270px;font-weight:700;line-height:1" data-fx="count" data-to="14" data-at=".5" data-d="1.6">0</div>
  <div style="font-size:76px;font-weight:900;margin-top:-10px">يوم</div>
 </div>
 <div class="gold" style="font-size:96px;font-weight:900;margin-top:50px" data-fx="stamp" data-at="2.2">مجانًا</div>
</div>
<div class="sc" data-a="4.2" data-b="8.4">
 <div style="font-size:64px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">وبعدها اختار<br>اللي يناسبك</div>
 <div class="col" style="width:100%;gap:30px;margin-top:60px">
  <div class="glass" data-fx="right" data-at=".5" style="padding:34px 50px;display:flex;justify-content:space-between;align-items:center"><span style="font-size:52px;font-weight:800">شهري</span><span class="gold" style="font-family:CairoL;font-size:100px;font-weight:700">200<small style="font-family:Cairo;font-size:44px"> ج</small></span></div>
  <div class="glass" data-fx="right" data-at=".9" style="padding:34px 50px;display:flex;justify-content:space-between;align-items:center;border-color:rgba(217,178,95,.7)"><span style="font-size:52px;font-weight:800">سنوي</span><span class="gold" style="font-family:CairoL;font-size:100px;font-weight:700">2000<small style="font-family:Cairo;font-size:44px"> ج</small></span></div>
 </div>
</div>
<div class="sc" data-a="8.2" data-b="12.3">
 <img src="../logo.svg" width="190" data-fx="spin" data-at=".1">
 <div style="font-size:80px;font-weight:900;margin-top:40px" data-fx="rise" data-at=".4">ابدأ <span class="gold">النهارده</span></div>
 <div class="btn url" data-fx="pulse" data-at=".9" style="margin-top:60px;font-size:72px;padding:24px 70px">mezan.pro</div>
</div>''',D=12,story=True)
M.append(dict(date=D8,time='11:00',kind='story',video=dict(src='sv29_1100',D=12,preset='em',seed=291,bpm=128,trans='4.2,8.2',pat=2),media=['sv29_1100.mp4'],idea='قصة فيديو: عدّاد 14 يوم تجربة مجانية + الأسعار'))

# ---------- STORY 15:00 — quote
story('s29_1500','''
<div class="glowc" style="width:1100px;height:1100px;left:-10px;top:400px"></div>
<div style="position:absolute;top:430px;left:0;right:0;display:flex;justify-content:center;gap:40px;font-size:150px"><span>🗂️</span><span style="opacity:.6;color:var(--gold2);font-family:CairoL">←</span><span>😌</span></div>
<div class="center" style="position:absolute;top:760px;left:60px;right:60px">
 <div style="font-size:96px;font-weight:900;line-height:1.35">اللي بيرتّب<br>النهارده…</div>
 <div class="line" style="width:300px;margin:44px auto"></div>
 <div class="gold" style="font-size:110px;font-weight:900;line-height:1.3">بيرتاح بكرة</div>
</div>
<div class="url center" style="position:absolute;top:1530px;left:0;right:0;font-size:60px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='15:00',kind='story',media=['s29_1500.png'],idea='قصة اقتباس: «اللي بيرتّب النهارده… بيرتاح بكرة»'))

# ---------- STORY 20:30 — occasion: winter time tonight
story('s29_2030','''
<div class="pill" style="position:absolute;top:390px;left:50%;transform:translateX(-50%);font-size:32px">تنبيه الليلة ⏰</div>
<div style="position:absolute;top:500px;left:0;right:0;display:flex;justify-content:center">
 <svg width="420" height="420" viewBox="0 0 300 300"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3d998"/><stop offset="1" stop-color="#b88d3a"/></linearGradient></defs>
  <circle cx="150" cy="150" r="130" fill="rgba(217,178,95,.08)" stroke="url(#g)" stroke-width="10"/>
  <g stroke="#9fb0cf" stroke-width="5" stroke-linecap="round"><line x1="150" y1="32" x2="150" y2="50"/><line x1="268" y1="150" x2="250" y2="150"/><line x1="150" y1="268" x2="150" y2="250"/><line x1="32" y1="150" x2="50" y2="150"/></g>
  <line x1="150" y1="150" x2="98" y2="120" stroke="url(#g)" stroke-width="14" stroke-linecap="round"/>
  <line x1="150" y1="150" x2="150" y2="50" stroke="#eef2fa" stroke-width="8" stroke-linecap="round"/>
  <path d="M220 70 A110 110 0 0 0 150 40" fill="none" stroke="#f3d998" stroke-width="6" stroke-dasharray="10 8"/>
  <circle cx="150" cy="150" r="12" fill="url(#g)"/></svg>
</div>
<div class="center" style="position:absolute;top:960px;left:60px;right:60px">
 <div style="font-size:66px;font-weight:900;line-height:1.35">الليلة الساعة <span class="gold">12</span><br>هترجع <span class="gold">11</span> 🌙</div>
 <div style="font-size:46px;color:#c9d4ea;font-weight:700;margin-top:24px;line-height:1.5">نهاية التوقيت الصيفي<br>وبداية التوقيت الشتوي</div>
 <div class="glass" style="margin:40px 40px 0;padding:26px 30px;font-size:40px;font-weight:800">⏰ اتأكد من منبّه جلسة بكرة</div>
</div>
<div class="url center" style="position:absolute;top:1580px;left:0;right:0;font-size:58px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='20:30',kind='story',media=['s29_2030.png'],idea='قصة مناسبة: الليلة نهاية التوقيت الصيفي — الساعة 12 ترجع 11، اتأكد من منبّه جلسة بكرة'))
json.dump(M,open('m29.json','w'),ensure_ascii=False,indent=1);print('ok')
