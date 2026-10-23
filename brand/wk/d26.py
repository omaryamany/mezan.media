from lib import *
import json
M=[];D8='2026-10-26'
TAGS='\n\n#ميزان_برو #محاماة'
# ---------- POST 10:00 — client tip: one documents list
post('p26_1000','''
<div class="box" style="top:165px;left:420px"><div class="h1" style="font-size:66px">اطلب ورق موكلك<br>في <span class="gold">قايمة واحدة</span></div>
<div class="lead" style="font-size:28px;margin-top:18px">بدل ما تطلب ورقة كل شوية…<br>ويتوه بين «فاضل إيه؟» و«بعته قبل كده»</div></div>
<div class="paper" style="position:absolute;left:66px;top:175px;width:350px;padding:26px 26px;transform:rotate(-3deg)">
 <div style="font-size:25px;font-weight:900;color:#8a6a2c;white-space:nowrap;border-bottom:2px dashed #c9c3b2;padding-bottom:12px;margin-bottom:14px">📋 المستندات المطلوبة</div>
 <div style="font-size:24px;font-weight:700;line-height:2">☑️ صورة البطاقة<br>☑️ صورة العقد<br>⬜ إيصالات السداد<br>⬜ أي مراسلات<br>⬜ أي إنذارات وصلته</div>
</div>
<div class="box row" style="top:670px;gap:20px">
 <div class="glass card" style="flex:1"><div style="font-size:44px">🗒️</div><div style="font-size:28px;font-weight:800;margin-top:8px">قايمة مكتوبة</div><div class="small">من أول مقابلة</div></div>
 <div class="glass card" style="flex:1"><div style="font-size:44px">✔️</div><div style="font-size:28px;font-weight:800;margin-top:8px">علّم اللي وصل</div><div class="small">أول بأول</div></div>
 <div class="glass card" style="flex:1"><div style="font-size:44px">📤</div><div style="font-size:28px;font-weight:800;margin-top:8px">ابعتله الباقي</div><div class="small">في رسالة واحدة</div></div>
</div>''',pill='مع الموكلين 🤝',foot='موكل فاهم المطلوب = شغل أسرع')
M.append(dict(date=D8,time='10:00',kind='post',media=['p26_1000.png'],
 text='اطلب ورق موكلك في قايمة واحدة 📋\n\nبدل ما تطلب ورقة كل شوية والموكل يتوه بين «فاضل إيه؟» و«بعته قبل كده»:\n🗒️ اكتب قايمة المستندات المطلوبة من أول مقابلة\n✔️ علّم على اللي وصل أول بأول\n📤 وابعتله الباقي في رسالة واحدة واضحة\n\nموكل فاهم المطلوب = شغل أسرع.\nإيه أكتر ورقة بتتأخر عليك؟ قولنا 👇\nmezan.pro'+TAGS,
 idea='نصيحة تعامل مع الموكلين: اطلب المستندات في قايمة واحدة مكتوبة'))

# ---------- POST 12:00 — VIDEO before/after
video('v26_1200','''
<div class="sc" data-a="0" data-b="3.2">
 <div style="font-size:120px" data-fx="pop" data-at=".1">⏰</div>
 <div class="h1" data-fx="rise" data-at=".5" style="font-size:96px;margin-top:20px">ساعة<br><span class="gold">قبل الجلسة</span></div>
 <div class="lead" data-fx="rise" data-at="1" style="font-size:40px;margin-top:16px">نفس الساعة… بطريقتين</div>
</div>
<div class="sc" data-a="3" data-b="7.4">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:34px;padding:10px 30px;background:rgba(252,165,165,.15);color:#fca5a5">بالورق</div>
 <div class="col" style="margin-top:40px;width:760px;gap:20px">
  <div class="glass li" data-fx="left" data-at=".4" style="padding:22px 30px"><div class="ic">📚</div><div class="t" style="font-size:38px">تقلّب في الدوسيه من الأول</div></div>
  <div class="glass li" data-fx="left" data-at=".75" style="padding:22px 30px"><div class="ic">🔍</div><div class="t" style="font-size:38px">تدوّر على الورقة المهمة</div></div>
  <div class="glass li" data-fx="left" data-at="1.1" style="padding:22px 30px"><div class="ic">😓</div><div class="t" style="font-size:38px">وتدخل الجلسة متوتر</div></div>
 </div>
</div>
<div class="sc" data-a="7.2" data-b="11.6">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:34px;padding:10px 30px">مع ميزان برو</div>
 <div class="col" style="margin-top:40px;width:760px;gap:20px">
  <div class="glass li" data-fx="right" data-at=".4" style="padding:22px 30px;border-color:rgba(217,178,95,.5)"><div class="ic">⚖️</div><div class="t" style="font-size:38px">تفتح ملف القضية</div></div>
  <div class="glass li" data-fx="right" data-at=".75" style="padding:22px 30px;border-color:rgba(217,178,95,.5)"><div class="ic">🤖</div><div class="t" style="font-size:38px">الملخص قدامك</div></div>
  <div class="glass li" data-fx="right" data-at="1.1" style="padding:22px 30px;border-color:rgba(217,178,95,.5)"><div class="ic">☕</div><div class="t" style="font-size:38px">وتراجع على رواقة</div></div>
 </div>
</div>
<div class="sc" data-a="11.4" data-b="16.4">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:80px">إنت تختار<br><span class="gold">أنهي ساعة؟</span></div>
 <div class="btn" data-fx="pulse" data-at=".9" style="margin-top:40px;font-size:44px;padding:16px 50px">جرّب مجانًا 14 يوم</div>
 <div class="url" data-fx="rise" data-at="1.3" style="margin-top:30px;font-size:54px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
M.append(dict(date=D8,time='12:00',kind='post',video=dict(src='v26_1200',D=16,preset='c',seed=26,bpm=114,trans='3,7.2,11.4',pat=2),media=['v26_1200.mp4'],title='ساعة قبل الجلسة | ميزان برو',
 text='ساعة قبل الجلسة… نفس الساعة بطريقتين ⏰\n\nبالورق: تقلّب في الدوسيه من الأول وتدوّر على الورقة المهمة.\nمع ميزان برو: تفتح ملف القضية، والملخص اللي عمله الذكاء الاصطناعي قدامك.\n\nإنت تختار أنهي ساعة؟\nجرّب مجانًا 14 يوم 👈 mezan.pro'+TAGS,
 idea='فيديو موشن قبل/بعد: «ساعة قبل الجلسة» بالورق ضد مع ميزان برو'))

# ---------- POST 18:00 — poll: case types
post('p26_1800','''
<div class="box center" style="top:160px"><div class="lead" style="font-size:30px;color:var(--gold2)">سؤال للزملاء 👇</div><div class="h1" style="font-size:72px;margin-top:4px">أكتر قضايا <span class="gold">بتشتغل فيها؟</span></div></div>
<div class="box" style="top:400px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num">أ</div><div><div style="font-size:40px;font-weight:900">مدني</div><div class="small">عقود · إيجارات · تعويضات</div></div></div>
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num">ب</div><div><div style="font-size:40px;font-weight:900">أسرة</div><div class="small">أحوال شخصية</div></div></div>
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num">ج</div><div><div style="font-size:40px;font-weight:900">جنائي</div><div class="small">جنح · جنايات</div></div></div>
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num">د</div><div><div style="font-size:40px;font-weight:900">عمالي/إداري</div><div class="small">ولا حاجة تانية؟</div></div></div>
</div>
<div class="box center" style="top:820px"><span style="font-size:34px;font-weight:800">اكتب الحرف في الكومنتات ✍️</span></div>''',pill='شاركنا 💬',foot='كل الآراء تهمنا')
M.append(dict(date=D8,time='18:00',kind='post',media=['p26_1800.png'],
 text='سؤال للزملاء المحامين 👇\n\nأكتر قضايا بتشتغل فيها؟\nأ) مدني\nب) أسرة\nج) جنائي\nد) عمالي/إداري… ولا حاجة تانية؟\n\nاكتب الحرف في الكومنتات ✍️'+TAGS,
 idea='سؤال تفاعلي: أكتر نوع قضايا بتشتغل فيه؟ (أ/ب/ج/د)'))

# ---------- STORY 11:00 — AI: summarizes, you decide
story('s26_1100','''
<div style="position:absolute;top:400px;left:0;right:0;height:560px;display:flex">
 <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(217,178,95,.08);border-left:2px solid rgba(217,178,95,.35)">
  <div style="font-size:150px">🤖</div><div style="font-size:52px;font-weight:900;margin-top:20px">بيلخّص</div><div style="font-size:34px;color:var(--mute);margin-top:8px">أوراق القضية</div>
 </div>
 <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center">
  <div style="font-size:150px">🧑‍⚖️</div><div class="gold" style="font-size:52px;font-weight:900;margin-top:20px">إنت بتقرر</div><div style="font-size:34px;color:var(--mute);margin-top:8px">الرأي والقرار</div>
 </div>
</div>
<div class="center" style="position:absolute;top:1060px;left:60px;right:60px">
 <div style="font-size:80px;font-weight:900;line-height:1.35">الذكاء الاصطناعي<br><span class="gold">بيوفّر وقتك</span></div>
 <div style="font-size:44px;color:#c9d4ea;font-weight:700;margin-top:24px">والخبرة… خبرتك إنت</div>
</div>
<div class="url center" style="position:absolute;top:1540px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='11:00',kind='story',media=['s26_1100.png'],idea='قصة ذكاء اصطناعي: «هو بيلخّص… إنت بتقرر»'))

# ---------- STORY 15:00 — trial ticket
story('s26_1500','''
<div class="center" style="position:absolute;top:420px;left:60px;right:60px"><div style="font-size:84px;font-weight:900;line-height:1.3">تذكرة دخول<br><span class="gold">مجانية</span> 🎟️</div></div>
<div style="position:absolute;top:760px;left:110px;right:110px;height:560px;border-radius:40px;background:linear-gradient(160deg,var(--gold2),var(--gold) 60%,#b88d3a);color:var(--navy);box-shadow:0 30px 90px rgba(217,178,95,.35);display:flex;flex-direction:column;align-items:center;justify-content:center">
 <div style="position:absolute;top:50%;right:-40px;width:80px;height:80px;border-radius:50%;background:#0a1530;transform:translateY(-50%)"></div>
 <div style="position:absolute;top:50%;left:-40px;width:80px;height:80px;border-radius:50%;background:#0a1530;transform:translateY(-50%)"></div>
 <div style="font-size:44px;font-weight:800">ميزان برو</div>
 <div style="font-family:CairoL;font-size:220px;font-weight:700;line-height:1">14</div>
 <div style="font-size:64px;font-weight:900">يوم تجربة</div>
 <div style="width:70%;border-top:4px dashed rgba(11,22,48,.35);margin:24px 0"></div>
 <div style="font-size:38px;font-weight:800">من غير ما تدفع حاجة</div>
</div>
<div class="url center" style="position:absolute;top:1450px;left:0;right:0;font-size:70px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='15:00',kind='story',media=['s26_1500.png'],idea='قصة: «تذكرة دخول مجانية» — 14 يوم تجربة'))

# ---------- STORY 20:30 — VIDEO org: priorities
video('sv26_2030','''
<div class="sc" data-a="0" data-b="3.8">
 <div style="font-size:96px;font-weight:900;line-height:1.3" data-fx="rise" data-at=".2">مش كل حاجة<br><span class="gold">عاجلة</span> 🚨</div>
 <div style="font-size:46px;color:#c9d4ea;font-weight:700;margin-top:30px" data-fx="rise" data-at=".8">قسّم مهام بكرة لـ 3</div>
</div>
<div class="sc" data-a="3.6" data-b="8.4">
 <div class="col" style="width:100%;gap:30px">
  <div class="glass" data-fx="right" data-at=".2" style="padding:34px 40px;display:flex;align-items:center;gap:30px;border-color:rgba(252,165,165,.5)"><div style="font-size:80px">🔴</div><div style="text-align:right"><div style="font-size:58px;font-weight:900">عاجل</div><div style="font-size:36px;color:var(--mute)">له ميعاد قريب… أول حاجة</div></div></div>
  <div class="glass" data-fx="right" data-at=".7" style="padding:34px 40px;display:flex;align-items:center;gap:30px;border-color:rgba(217,178,95,.6)"><div style="font-size:80px">🟡</div><div style="text-align:right"><div style="font-size:58px;font-weight:900">مهم</div><div style="font-size:36px;color:var(--mute)">حدّد له وقت ثابت</div></div></div>
  <div class="glass" data-fx="right" data-at="1.2" style="padding:34px 40px;display:flex;align-items:center;gap:30px;border-color:rgba(134,239,172,.5)"><div style="font-size:80px">🟢</div><div style="text-align:right"><div style="font-size:58px;font-weight:900">يستنى</div><div style="font-size:36px;color:var(--mute)">اكتبه ومتشيلش همّه</div></div></div>
 </div>
</div>
<div class="sc" data-a="8.2" data-b="12.3">
 <div style="font-size:84px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">ونام وإنت<br><span class="gold">عارف بكرة هيبدأ بإيه</span> 🌙</div>
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".7" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
M.append(dict(date=D8,time='20:30',kind='story',video=dict(src='sv26_2030',D=12,preset='fm',seed=262,bpm=100,trans='3.6,8.2',pat=4),media=['sv26_2030.mp4'],idea='قصة فيديو تنظيم: قسّم مهام بكرة لـ عاجل / مهم / يستنى'))
json.dump(M,open('m26.json','w'),ensure_ascii=False,indent=1);print('ok')
