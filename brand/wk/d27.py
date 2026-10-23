from lib import *
import json
M=[];D8='2026-10-27'
TAGS='\n\n#ميزان_برو #محاماة'
# ---------- POST 10:00 — FAQ
post('p27_1000','''
<div class="box" style="top:170px">
 <div style="display:flex;justify-content:flex-start"><div class="glass" style="max-width:900px;padding:28px 36px;border-radius:34px 34px 34px 8px">
  <div class="tag" style="margin-bottom:12px">سؤال بيوصلنا كتير ❓</div>
  <div style="font-size:46px;font-weight:900;line-height:1.4">هو الذكاء الاصطناعي في ميزان برو<br>هيكتب المذكرة <span class="gold">بدالي؟</span></div>
 </div></div>
 <div style="display:flex;justify-content:flex-end;margin-top:30px"><div style="max-width:900px;padding:30px 38px;border-radius:34px 34px 8px 34px;background:linear-gradient(160deg,rgba(217,178,95,.24),rgba(217,178,95,.07));border:1px solid rgba(217,178,95,.6)">
  <div style="font-size:54px;font-weight:900"><span class="gold">لأ</span> 🙂</div>
  <div style="font-size:32px;line-height:1.65;font-weight:600;margin-top:6px">دوره إنه <b class="gold">يلخّص أوراق ومستندات القضية</b>، والملخص يتربط بملف القضية… علشان توصل للمعلومة أسرع.</div>
  <div style="font-size:32px;line-height:1.65;font-weight:800;margin-top:12px">أما المذكرة والرأي القانوني… <span class="gold">ده شغلك إنت</span> ⚖️</div>
 </div></div>
</div>''',pill='أسئلة شائعة',foot='عندك سؤال؟ اكتبه في الكومنتات')
M.append(dict(date=D8,time='10:00',kind='post',media=['p27_1000.png'],
 text='سؤال بيوصلنا كتير ❓\n«هو الذكاء الاصطناعي في ميزان برو هيكتب المذكرة بدالي؟»\n\nلأ 🙂 دوره إنه يلخّص أوراق ومستندات القضية، والملخص يتربط بملف القضية… علشان توصل للمعلومة أسرع.\nأما المذكرة والرأي القانوني… ده شغلك إنت ⚖️\n\nعندك سؤال تاني عن النظام؟ اكتبه في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='أسئلة شائعة: «هل الذكاء الاصطناعي هيكتب المذكرة بدالي؟» — لأ، بيلخّص والقرار ليك'))

# ---------- POST 12:00 — VIDEO legal: cassation 60 days
video('v27_1200','''
<div class="sc" data-a="0" data-b="3.2">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:28px">معلومة إجرائية ⚖️</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:90px;margin-top:30px">ميعاد الطعن<br><span class="gold">بالنقض</span> كام يوم؟</div>
</div>
<div class="sc" data-a="3" data-b="7">
 <div style="width:440px;height:440px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;border:4px solid rgba(217,178,95,.75);background:radial-gradient(circle at 50% 35%,rgba(243,217,152,.22),rgba(217,178,95,.05) 65%);box-shadow:0 0 0 22px rgba(217,178,95,.07),0 0 120px rgba(217,178,95,.3)" data-fx="pop" data-at=".1">
  <div class="gold" style="font-family:CairoL;font-size:210px;font-weight:700;line-height:1" data-fx="count" data-to="60" data-at=".3" data-d="1.4">0</div>
  <div style="font-size:60px;font-weight:900;margin-top:-6px">يوم</div>
 </div>
</div>
<div class="sc" data-a="6.8" data-b="10.8">
 <div class="glass" data-fx="rise" data-at=".2" style="padding:44px 50px;max-width:860px">
  <div style="font-size:70px" class="gold">“</div>
  <div style="font-size:58px;font-weight:900;line-height:1.4">ميعاد الطعن بطريق النقض<br><span class="gold">ستون يومًا</span></div>
  <div class="small" style="font-size:30px;margin-top:20px">المادة 252 — قانون المرافعات المدنية والتجارية</div>
 </div>
</div>
<div class="sc" data-a="10.6" data-b="13.4">
 <div style="font-size:110px" data-fx="pop" data-at=".1">📌</div>
 <div class="h2" data-fx="rise" data-at=".4" style="font-size:62px;margin-top:20px">أول ما الحكم يصدر…<br><span class="gold">اكتب آخر يوم للطعن</span><br>في ملف القضية</div>
</div>
<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:86px;margin-top:14px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px;margin-top:6px">احفظ المعلومة وشاركها مع زمايلك 🔖</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
M.append(dict(date=D8,time='12:00',kind='post',video=dict(src='v27_1200',D=16,preset='bm',seed=27,bpm=104,trans='3,6.8,10.6,13.2',pat=3),media=['v27_1200.mp4'],title='ميعاد الطعن بالنقض | ميزان برو',
 text='معلومة إجرائية ⚖️\n\nميعاد الطعن بالنقض كام يوم؟\n«ميعاد الطعن بطريق النقض ستون يومًا» — المادة 252 من قانون المرافعات المدنية والتجارية.\n\n📌 نصيحة: أول ما الحكم يصدر، اكتب آخر يوم للطعن في ملف القضية علشان ميفوتكش.\n\nاحفظ البوست وشاركه مع زمايلك 🔖\nmezan.pro'+TAGS,
 idea='فيديو موشن معلومة إجرائية: ميعاد الطعن بالنقض 60 يوم (م.252 مرافعات)'))

# ---------- POST 18:00 — ORG: case timeline
post('p27_1800','''
<div class="box" style="top:160px;left:470px"><div class="h1" style="font-size:62px">لكل قضية<br><span class="gold">خط زمني</span><br>في صفحة واحدة</div>
<div class="lead" style="font-size:27px;margin-top:20px">الوقائع بترتيب حصولها،<br>كل سطر: تاريخ + حدث + المستند.<br>وأي حد يمسك القضية يفهمها <span class="gold">في دقايق</span>.</div></div>
<div style="position:absolute;top:175px;left:66px;width:370px">
 <div style="position:absolute;right:23px;top:20px;bottom:20px;width:4px;background:linear-gradient(var(--gold),rgba(217,178,95,.15));border-radius:4px"></div>
 <div class="col" style="gap:22px">
  <div style="display:flex;gap:18px;align-items:flex-start"><div style="flex:none;width:50px;height:50px;border-radius:50%;background:var(--gold);display:grid;place-items:center;font-size:24px;position:relative">📝</div><div class="glass" style="padding:14px 18px;flex:1"><div class="small" style="font-size:20px">التاريخ</div><div style="font-size:24px;font-weight:800">توقيع العقد</div></div></div>
  <div style="display:flex;gap:18px;align-items:flex-start"><div style="flex:none;width:50px;height:50px;border-radius:50%;background:var(--gold);display:grid;place-items:center;font-size:24px">✉️</div><div class="glass" style="padding:14px 18px;flex:1"><div class="small" style="font-size:20px">التاريخ</div><div style="font-size:24px;font-weight:800">الإنذار</div></div></div>
  <div style="display:flex;gap:18px;align-items:flex-start"><div style="flex:none;width:50px;height:50px;border-radius:50%;background:var(--gold);display:grid;place-items:center;font-size:24px">📂</div><div class="glass" style="padding:14px 18px;flex:1"><div class="small" style="font-size:20px">التاريخ</div><div style="font-size:24px;font-weight:800">رفع الدعوى</div></div></div>
  <div style="display:flex;gap:18px;align-items:flex-start"><div style="flex:none;width:50px;height:50px;border-radius:50%;background:var(--gold);display:grid;place-items:center;font-size:24px">🏛️</div><div class="glass" style="padding:14px 18px;flex:1"><div class="small" style="font-size:20px">التاريخ</div><div style="font-size:24px;font-weight:800">أول جلسة</div></div></div>
  <div style="display:flex;gap:18px;align-items:flex-start"><div style="flex:none;width:50px;height:50px;border-radius:50%;border:3px dashed var(--gold);display:grid;place-items:center;font-size:24px">…</div><div class="glass" style="padding:14px 18px;flex:1;opacity:.7"><div style="font-size:24px;font-weight:800">والجاي…</div></div></div>
 </div>
</div>''',pill='نصيحة تنظيم 🗓️',foot='احفظ الفكرة 🔖')
M.append(dict(date=D8,time='18:00',kind='post',media=['p27_1800.png'],
 text='لكل قضية خط زمني في صفحة واحدة 🗓️\n\nاكتب الوقائع بترتيب حصولها، وكل سطر فيه:\n• التاريخ\n• الحدث\n• المستند اللي بيثبته\n\nوقت التحضير هتلاقي الصورة كاملة قدامك، وأي زميل يمسك القضية يفهمها في دقايق.\nاحفظ البوست 🔖 وجرّبها على أول قضية جديدة.\nmezan.pro'+TAGS,
 idea='نصيحة تنظيم: خط زمني للقضية في صفحة واحدة (تاريخ + حدث + مستند)'))

# ---------- STORY 11:00 — quote
story('s27_1100','''
<div style="position:absolute;top:470px;left:120px;right:120px;height:640px">
 <div style="position:absolute;bottom:0;right:0;left:0;display:flex;align-items:flex-end;gap:24px;justify-content:center">
  <div style="width:110px;height:140px;border-radius:18px;background:rgba(217,178,95,.25)"></div>
  <div style="width:110px;height:250px;border-radius:18px;background:rgba(217,178,95,.4)"></div>
  <div style="width:110px;height:360px;border-radius:18px;background:rgba(217,178,95,.6)"></div>
  <div style="width:110px;height:470px;border-radius:18px;background:linear-gradient(var(--gold2),var(--gold))"></div>
 </div>
</div>
<div class="center" style="position:absolute;top:1170px;left:60px;right:60px">
 <div style="font-size:78px;font-weight:900;line-height:1.35">خطوة صغيرة كل يوم…</div>
 <div class="gold" style="font-size:66px;font-weight:900;line-height:1.35;margin-top:10px">أحسن من سهر<br>ليلة الجلسة</div>
</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:58px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='11:00',kind='story',media=['s27_1100.png'],idea='قصة اقتباس: «خطوة صغيرة كل يوم… أحسن من سهر ليلة الجلسة»'))

# ---------- STORY 15:00 — VIDEO problem signs
video('sv27_1500','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:92px;font-weight:900;line-height:1.3" data-fx="rise" data-at=".2">3 علامات<br>إن مكتبك<br><span class="gold">محتاج نظام</span></div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:30px">
  <div class="glass li" data-fx="left" data-at=".2" style="padding:34px 36px"><div class="num" style="width:80px;height:80px;font-size:44px">1</div><div class="t" style="font-size:48px;text-align:right">بتدوّر على المستند<br>أكتر ما بتقراه</div></div>
  <div class="glass li" data-fx="left" data-at="1.3" style="padding:34px 36px"><div class="num" style="width:80px;height:80px;font-size:44px">2</div><div class="t" style="font-size:48px;text-align:right">نفس الورقة<br>عندك منها كذا نسخة</div></div>
  <div class="glass li" data-fx="left" data-at="2.4" style="padding:34px 36px"><div class="num" style="width:80px;height:80px;font-size:44px">3</div><div class="t" style="font-size:48px;text-align:right">المعلومة<br>في دماغك بس</div></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <img src="../logo.svg" width="190" data-fx="spin" data-at=".1">
 <div style="font-size:84px;font-weight:900;line-height:1.3;margin-top:40px" data-fx="rise" data-at=".5">مكتبك كله<br><span class="gold">في نظام واحد</span></div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:60px;font-size:74px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
M.append(dict(date=D8,time='15:00',kind='story',video=dict(src='sv27_1500',D=12,preset='cm',seed=271,bpm=116,trans='3.2,8.4',pat=1),media=['sv27_1500.mp4'],idea='قصة فيديو: 3 علامات إن مكتبك محتاج نظام'))

# ---------- STORY 20:30 — poll
story('s27_2030','''
<div class="pill" style="position:absolute;top:390px;left:50%;transform:translateX(-50%);font-size:30px">سؤال سريع 💬</div>
<div class="center" style="position:absolute;top:500px;left:60px;right:60px"><div style="font-size:84px;font-weight:900;line-height:1.3">بتلخّص أوراق<br>قضاياك <span class="gold">بإيدك؟</span></div></div>
<div style="position:absolute;top:830px;left:130px;right:130px" class="col">
 <div class="glass" style="padding:34px 40px;display:flex;align-items:center;gap:26px"><div style="font-size:64px">✍️</div><div style="font-size:52px;font-weight:900">أيوه، دايمًا</div></div>
 <div class="glass" style="padding:34px 40px;display:flex;align-items:center;gap:26px"><div style="font-size:64px">🤏</div><div style="font-size:52px;font-weight:900">ساعات</div></div>
 <div class="glass" style="padding:34px 40px;display:flex;align-items:center;gap:26px"><div style="font-size:64px">🙅</div><div style="font-size:52px;font-weight:900">لأ، بقرا الكل</div></div>
</div>
<div class="center" style="position:absolute;top:1440px;left:60px;right:60px;font-size:44px;font-weight:800;color:#c9d4ea">ابعتلنا إجابتك في رسالة 📩</div>
<div class="url center" style="position:absolute;top:1550px;left:0;right:0;font-size:58px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='20:30',kind='story',media=['s27_2030.png'],idea='قصة سؤال تفاعلي: بتلخّص أوراق قضاياك بإيدك؟'))
json.dump(M,open('m27.json','w'),ensure_ascii=False,indent=1);print('ok')
