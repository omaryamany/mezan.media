from lib import *
import json
M=[]
TAGS='\n\n#ميزان_برو #محاماة'
def add(**k): M.append(k)

# ======================= SAT 2026-10-31 =======================
D='2026-10-31'
post('p31_1000','''
<div class="box center" style="top:165px"><div class="small" style="font-size:28px">رنّ التليفون… 📞</div></div>
<div class="box" style="top:225px;display:flex;justify-content:flex-start">
 <div class="paper" style="padding:26px 40px;border-radius:30px 30px 30px 6px;font-size:46px;font-weight:900">"يا متر… قضيتي وصلت لفين؟"</div>
</div>
<div class="box row" style="top:430px;gap:28px">
 <div class="glass" style="flex:1;padding:34px 32px;border-color:rgba(252,165,165,.35)">
  <div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5">من غير نظام</div>
  <div style="font-size:72px;margin-top:18px">😅</div>
  <div style="font-size:34px;font-weight:800;line-height:1.5;margin-top:10px">تقلّب في الدوسيهات…<br>و"هكلّمك تاني"</div>
 </div>
 <div class="glass" style="flex:1;padding:34px 32px;border-color:rgba(217,178,95,.6)">
  <div class="tag">مع ميزان برو</div>
  <div style="font-size:72px;margin-top:18px">😌</div>
  <div style="font-size:34px;font-weight:800;line-height:1.5;margin-top:10px">تفتح <span class="gold">ملف القضية</span>…<br>وترد وانت واثق</div>
 </div>
</div>
<div class="box center" style="top:880px;font-size:32px;font-weight:800">موكلك مش محتاج يستنى… <span class="gold">ولا إنت محتاج تدوّر</span></div>''',pill='مشكلة وحلها 💡')
add(date=D,time='10:00',kind='post',media=['p31_1000.png'],
 text='"يا متر… قضيتي وصلت لفين؟" 📞\n\nمن غير نظام: تقلّب في الدوسيهات وتقول "هكلّمك تاني" 😅\nمع ميزان برو: تفتح ملف القضية… وترد وانت واثق 😌\n\nنظام إدارة متكامل لمكتبك، وكل قضية ليها ملفها.\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='مشكلة وحلها: موكل بيتصل «قضيتي وصلت لفين؟» ← تفتح ملف القضية وترد')

video('v31_1200','''
<div class="sc" data-a="0" data-b="3.2">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:30px">نصيحة تنظيم 🗓️</div>
 <div style="font-size:170px;margin-top:20px" data-fx="pop" data-at=".3">⏱️</div>
 <div class="h1" data-fx="rise" data-at=".6" style="font-size:100px">قاعدة <span class="gold">الدقيقتين</span></div>
</div>
<div class="sc" data-a="3" data-b="6.4">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:78px">أي مهمة بتاخد<br><span class="gold">أقل من دقيقتين</span>…</div>
 <div class="h1" data-fx="stamp" data-at=".9" style="font-size:96px;margin-top:40px">اعملها <span class="gold">دلوقتي</span> ✅</div>
</div>
<div class="sc" data-a="6.2" data-b="11.2">
 <div style="font-size:52px;font-weight:900;margin-bottom:40px" data-fx="rise" data-at=".1">زي مثلًا 👇</div>
 <div class="col" style="width:100%;gap:26px">
  <div class="glass li" data-fx="right" data-at=".4" style="padding:28px 36px"><div class="ic">📲</div><div class="t" style="font-size:44px">تأكيد ميعاد مع موكل</div></div>
  <div class="glass li" data-fx="right" data-at=".9" style="padding:28px 36px"><div class="ic">📁</div><div class="t" style="font-size:44px">حفظ مستند في ملف قضيته</div></div>
  <div class="glass li" data-fx="right" data-at="1.4" style="padding:28px 36px"><div class="ic">✍️</div><div class="t" style="font-size:44px">تسجيل قرار الجلسة</div></div>
 </div>
</div>
<div class="sc" data-a="11" data-b="13.4">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:84px">المهام الصغيرة<br>لو اتأجلت… <span class="gold">بتكبر</span></div>
</div>
<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:90px;margin-top:16px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px">نظام إدارة متكامل لمكاتب المحاماة</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
add(date=D,time='12:00',kind='post',video=dict(src='v31_1200',D=16,preset='g',seed=311,bpm=100,trans='3,6.2,11,13.2',pat=2),media=['v31_1200.mp4'],title='قاعدة الدقيقتين | ميزان برو',
 text='قاعدة الدقيقتين ⏱️\n\nأي مهمة بتاخد أقل من دقيقتين… اعملها دلوقتي ✅\n📲 تأكيد ميعاد مع موكل\n📁 حفظ مستند في ملف قضيته\n✍️ تسجيل قرار الجلسة\n\nالمهام الصغيرة لو اتأجلت… بتكبر.\nجرّبها النهارده وقولنا الفرق 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن نصيحة تنظيم: «قاعدة الدقيقتين» للمهام الصغيرة')

post('p31_1800','''
<div class="box center" style="top:160px"><div class="h1" style="font-size:70px">إمتى بتكتب <span class="gold">مذكراتك</span>؟ ✍️</div><div class="lead" style="margin-top:6px">اختار حرف وقولنا في الكومنتات 👇</div></div>
<div class="box" style="top:400px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num" style="width:76px;height:76px;font-size:40px">أ</div><div><div style="font-size:56px">🌅</div><div style="font-size:36px;font-weight:900">الصبح بدري</div></div></div>
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num" style="width:76px;height:76px;font-size:40px">ب</div><div><div style="font-size:56px">⚖️</div><div style="font-size:36px;font-weight:900">بعد المحكمة</div></div></div>
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num" style="width:76px;height:76px;font-size:40px">ج</div><div><div style="font-size:56px">🌙</div><div style="font-size:36px;font-weight:900">بالليل متأخر</div></div></div>
 <div class="glass" style="padding:30px;display:flex;align-items:center;gap:22px"><div class="num" style="width:76px;height:76px;font-size:40px">د</div><div><div style="font-size:56px">☕</div><div style="font-size:36px;font-weight:900">في الويكند</div></div></div>
</div>''',pill='سؤال للمحامين 💬',foot='شاركنا رأيك')
add(date=D,time='18:00',kind='post',media=['p31_1800.png'],
 text='سؤال للمحامين 💬\nإمتى بتكتب مذكراتك؟ ✍️\n\nأ) 🌅 الصبح بدري\nب) ⚖️ بعد المحكمة\nج) 🌙 بالليل متأخر\nد) ☕ في الويكند\n\nاكتب الحرف في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='سؤال تفاعلي: إمتى بتكتب مذكراتك؟ (أ/ب/ج/د)')

story('s31_1100','''
<div class="center" style="position:absolute;top:400px;left:60px;right:60px"><div style="font-size:84px;font-weight:900;line-height:1.3">من <span class="gold">الدُرج</span>…<br>لـ<span class="gold">الملف</span></div></div>
<div class="glass center" style="position:absolute;top:720px;left:150px;right:150px;padding:40px;border-color:rgba(252,165,165,.35)">
 <div style="font-size:120px">🗄️</div><div style="font-size:46px;font-weight:800;color:#fca5a5">ورق متكوّم… ومش لاقيه</div>
</div>
<div class="center" style="position:absolute;top:1020px;left:0;right:0;font-size:90px;color:var(--gold2)">⬇</div>
<div class="glass center" style="position:absolute;top:1140px;left:150px;right:150px;padding:40px;border-color:rgba(217,178,95,.7)">
 <div style="font-size:120px">📁</div><div style="font-size:46px;font-weight:800">كل قضية <span class="gold">ليها ملفها</span></div>
</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='11:00',kind='story',media=['s31_1100.png'],idea='قصة قبل/بعد: من الدُرج المتكوّم… لملف لكل قضية')

video('sv31_1500','''
<div class="sc" data-a="0" data-b="4.2">
 <div class="gold" style="font-family:Messiri;font-size:260px;line-height:.8;height:160px" data-fx="fade" data-at=".1">“</div>
 <div style="font-size:92px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".3">القضية<br>بتتكسب في<br><span class="gold">التحضير</span></div>
</div>
<div class="sc" data-a="4" data-b="8.2">
 <div style="font-size:80px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".1">قبل ما توصل<br><span class="gold">لقاعة الجلسة</span> ⚖️</div>
 <div class="line" style="width:340px;margin:50px auto" data-fx="bar" data-at=".7"></div>
 <div style="font-size:56px;font-weight:700;color:#c9d4ea" data-fx="rise" data-at="1">حضّر النهارده… وادخل بكرة واثق</div>
</div>
<div class="sc" data-a="8" data-b="12.3">
 <img src="../logo.svg" width="170" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:100px;margin-top:20px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="url" data-fx="pulse" data-at=".9" style="margin-top:40px;font-size:76px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv31_1500',D=12,preset='am2',seed=315,bpm=86,trans='4,8',pat=3),media=['sv31_1500.mp4'],idea='قصة فيديو اقتباس: «القضية بتتكسب في التحضير»')

story('s31_2030','''
<div class="center" style="position:absolute;top:380px;left:60px;right:60px;font-size:70px;font-weight:900">ميزان برو <span class="gold">بكام؟</span> 💬</div>
<div style="position:absolute;top:560px;left:80px;right:80px" class="col">
 <div style="align-self:flex-start;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);padding:26px 40px;border-radius:40px 40px 40px 10px;font-size:50px;font-weight:800">بكام في الشهر؟</div>
 <div style="align-self:flex-end;background:linear-gradient(160deg,var(--gold2),var(--gold));color:var(--navy);padding:26px 40px;border-radius:40px 40px 10px 40px;font-size:56px;font-weight:900">200 ج</div>
 <div style="align-self:flex-start;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);padding:26px 40px;border-radius:40px 40px 40px 10px;font-size:50px;font-weight:800;margin-top:20px">وفيه سنوي؟</div>
 <div style="align-self:flex-end;background:linear-gradient(160deg,var(--gold2),var(--gold));color:var(--navy);padding:26px 40px;border-radius:40px 40px 10px 40px;font-size:56px;font-weight:900">2000 ج في السنة</div>
 <div style="align-self:flex-start;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);padding:26px 40px;border-radius:40px 40px 40px 10px;font-size:50px;font-weight:800;margin-top:20px">أجرّب الأول؟</div>
 <div style="align-self:flex-end;background:linear-gradient(160deg,var(--gold2),var(--gold));color:var(--navy);padding:26px 40px;border-radius:40px 40px 10px 40px;font-size:56px;font-weight:900">أكيد… 14 يوم مجانًا 🎁</div>
</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='20:30',kind='story',media=['s31_2030.png'],idea='قصة أسعار بشكل شات: بكام؟ 200 ج شهري · 2000 ج سنوي · 14 يوم مجانًا')

# ======================= SUN 2026-11-01 =======================
D='2026-11-01'
video('v01_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">📚</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:88px">استلمت قضية<br><span class="gold">من زميل؟</span></div>
</div>
<div class="sc" data-a="3.2" data-b="6.6">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:80px">والأوراق <span class="gold">تقيلة</span>…</div>
 <div class="row" style="justify-content:center;gap:24px;margin-top:40px">
  <div class="paper" data-fx="drop" data-at=".4" style="width:150px;height:200px"></div>
  <div class="paper" data-fx="drop" data-at=".6" style="width:150px;height:200px"></div>
  <div class="paper" data-fx="drop" data-at=".8" style="width:150px;height:200px"></div>
  <div class="paper" data-fx="drop" data-at="1" style="width:150px;height:200px"></div>
 </div>
 <div class="lead" data-fx="rise" data-at="1.3" style="font-size:44px;margin-top:36px">تبدأ منين؟ 🤔</div>
</div>
<div class="sc" data-a="6.4" data-b="10.2">
 <div style="font-size:120px" data-fx="pop" data-at=".1">🤖</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:64px">ميزان برو بيلخّص<br><span class="gold">أوراق ومستندات القضية</span><br>بالذكاء الاصطناعي</div>
</div>
<div class="sc" data-a="10" data-b="13.4">
 <div class="glass" data-fx="pop" data-at=".1" style="padding:36px 50px;font-size:48px;font-weight:900;white-space:nowrap">📝 الملخص ← 📁 <span class="gold">ملف القضية</span></div>
 <div class="h1" data-fx="rise" data-at=".6" style="font-size:62px;margin-top:40px">ابدأ من الملخص…<br>وارجع للأصل في <span class="gold">أي تفصيلة</span></div>
</div>
<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:90px;margin-top:16px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px">جرّبه 14 يوم مجانًا</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v01_1000',D=16,preset='bm',seed=110,bpm=94,trans='3.2,6.4,10,13.2',pat=1),media=['v01_1000.mp4'],title='استلمت قضية من زميل؟ | ميزان برو',
 text='استلمت قضية من زميل والأوراق تقيلة؟ 📚\nتبدأ منين؟\n\nميزان برو بيلخّص أوراق ومستندات القضية بالذكاء الاصطناعي 🤖\nوالملخص بيتربط بملف القضية 📁\n\nابدأ من الملخص… وارجع للأصل في أي تفصيلة.\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='فيديو موشن ميزة: استلمت قضية من زميل؟ ابدأ من ملخص الذكاء الاصطناعي المربوط بملفها')

post('p01_1200','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:72px">ميعاد <span class="gold">الاستئناف</span> ⏳</div></div>
<div class="box row" style="top:330px;gap:30px">
 <div class="glass center" style="flex:1.3;padding:40px 20px;border-color:rgba(217,178,95,.6)">
  <div class="gold" style="font-family:CairoL;font-size:190px;font-weight:900;line-height:1">40</div>
  <div style="font-size:44px;font-weight:900">يوم</div>
  <div class="lead" style="font-size:28px;margin-top:10px">الأصل… ما لم ينص القانون<br>على غير ذلك</div>
 </div>
 <div class="glass center" style="flex:1;padding:40px 20px">
  <div style="font-family:CairoL;font-size:150px;font-weight:900;line-height:1.15;color:#eef2fa">15</div>
  <div style="font-size:40px;font-weight:900">يوم</div>
  <div class="lead" style="font-size:28px;margin-top:10px">في المواد<br>المستعجلة</div>
 </div>
</div>
<div class="box center" style="top:800px"><div class="tag" style="font-size:26px">المادة 227 من قانون المرافعات المدنية والتجارية</div>
<div style="font-size:30px;font-weight:800;margin-top:22px">اكتب آخر ميعاد للطعن <span class="gold">في ملف القضية من يوم الحكم</span> 📌</div></div>''',pill='معلومة إجرائية ⚖️',foot='احفظ البوست 🔖')
add(date=D,time='12:00',kind='post',media=['p01_1200.png'],
 text='معلومة إجرائية ⚖️ ميعاد الاستئناف\n\n⏳ 40 يوم — ده الأصل، ما لم ينص القانون على غير ذلك.\n⚡ 15 يوم — في المواد المستعجلة، أيًا كانت المحكمة اللي أصدرت الحكم.\n(المادة 227 من قانون المرافعات المدنية والتجارية)\n\n📌 نصيحة: اكتب آخر ميعاد للطعن في ملف القضية من يوم الحكم.\nاحفظ البوست 🔖 وابعته لزميل.\nmezan.pro'+TAGS,
 idea='معلومة إجرائية: ميعاد الاستئناف 40 يوم، و15 يوم في المستعجل (م.227 مرافعات)')

post('p01_1800','''
<div class="box" style="top:160px"><div class="h1" style="font-size:62px">اشرح لموكلك <span class="gold">الخطوة الجاية</span>…<br>مش المصطلح 🗣️</div></div>
<div class="box col" style="top:420px;gap:30px">
 <div class="glass" style="padding:30px 36px;border-color:rgba(252,165,165,.35)"><div class="row" style="align-items:center"><div style="font-size:54px">❌</div><div style="font-size:42px;font-weight:800">"القضية اتحجزت للحكم."</div></div></div>
 <div class="glass" style="padding:30px 36px;border-color:rgba(217,178,95,.65)"><div class="row" style="align-items:center"><div style="font-size:54px">✅</div><div style="font-size:38px;font-weight:800;line-height:1.5">"المحكمة هتقول قرارها يوم كذا،<br>ولحد ساعتها مفيش مطلوب منك…<br><span class="gold">وأنا هبلّغك أول ما يصدر</span>."</div></div></div>
</div>
<div class="box center" style="top:905px;font-size:30px;font-weight:800">الموكل المطمّن… <span class="gold">بيثق أكتر</span></div>''',pill='مع الموكلين 🤝',foot='نصيحة للتواصل')
add(date=D,time='18:00',kind='post',media=['p01_1800.png'],
 text='اشرح لموكلك الخطوة الجاية… مش المصطلح 🗣️\n\n❌ "القضية اتحجزت للحكم."\n✅ "المحكمة هتقول قرارها يوم كذا، ولحد ساعتها مفيش مطلوب منك… وأنا هبلّغك أول ما يصدر."\n\nالموكل المطمّن بيثق أكتر 🤝\nإنت بتشرح لموكلينك إزاي؟ قولنا 👇\nmezan.pro'+TAGS,
 idea='نصيحة تواصل مع الموكلين: اشرح الخطوة الجاية بكلام بسيط مش بالمصطلح')

video('sv01_1100','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:84px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">قبل <span class="gold">الجلسة</span>…</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:20px" data-fx="rise" data-at=".6">بتشرب إيه؟ 🤔</div>
</div>
<div class="sc" data-a="3.4" data-b="8.6">
 <div class="row" style="gap:40px;justify-content:center;width:100%">
  <div class="glass center" data-fx="left" data-at=".2" style="flex:1;padding:60px 20px"><div style="font-size:180px">☕</div><div style="font-size:70px;font-weight:900;margin-top:10px">قهوة</div></div>
  <div class="glass center" data-fx="right" data-at=".5" style="flex:1;padding:60px 20px"><div style="font-size:180px">🍵</div><div style="font-size:70px;font-weight:900;margin-top:10px">شاي</div></div>
 </div>
 <div style="font-size:90px;font-weight:900;margin-top:50px" data-fx="stamp" data-at="1.2"><span class="gold">ولا الاتنين؟</span> 😄</div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:76px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">ابعتلنا <span class="gold">اختيارك</span><br>في رسالة 📩</div>
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv01_1100',D=12,preset='f',seed=111,bpm=112,trans='3.4,8.4',pat=4),media=['sv01_1100.mp4'],idea='قصة فيديو تفاعلية خفيفة: قبل الجلسة… قهوة ولا شاي؟')

story('s01_1500','''
<div class="center" style="position:absolute;top:400px;left:60px;right:60px"><div style="font-size:74px;font-weight:900;line-height:1.35">يعني إيه<br><span class="gold">نظام ERP</span> لمكتبك؟</div></div>
<div class="glass center" style="position:absolute;top:760px;left:100px;right:100px;padding:60px 40px;border-color:rgba(217,178,95,.6)">
 <div style="font-size:130px">🗂️</div>
 <div style="font-size:60px;font-weight:900;line-height:1.45;margin-top:10px">نظام <span class="gold">واحد</span><br>بيدير شغل المكتب<br>كله في مكان واحد</div>
</div>
<div class="center" style="position:absolute;top:1360px;left:60px;right:60px;font-size:44px;font-weight:700;color:#c9d4ea">وده بالظبط ميزان برو ⚖️</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='15:00',kind='story',media=['s01_1500.png'],idea='قصة ميزة: يعني إيه نظام ERP لمكتبك؟ نظام واحد بيدير شغل المكتب')

story('s01_2030','''
<div class="center" style="position:absolute;top:390px;left:60px;right:60px"><div style="font-size:120px">💼</div><div style="font-size:80px;font-weight:900;line-height:1.3;margin-top:10px">شنطة بكرة<br><span class="gold">جاهزة؟</span></div></div>
<div style="position:absolute;top:860px;left:140px;right:140px" class="col">
 <div class="glass li" style="padding:26px 40px;gap:30px"><div style="font-size:56px">✅</div><div style="font-size:54px;font-weight:800">ملف الجلسة</div></div>
 <div class="glass li" style="padding:26px 40px;gap:30px"><div style="font-size:56px">✅</div><div style="font-size:54px;font-weight:800">التوكيل</div></div>
 <div class="glass li" style="padding:26px 40px;gap:30px"><div style="font-size:56px">✅</div><div style="font-size:54px;font-weight:800">الكارنيه</div></div>
 <div class="glass li" style="padding:26px 40px;gap:30px"><div style="font-size:56px">✅</div><div style="font-size:54px;font-weight:800">شاحن الموبايل 🔋</div></div>
</div>
<div class="url center" style="position:absolute;top:1590px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='20:30',kind='story',media=['s01_2030.png'],idea='قصة تنظيم: شنطة بكرة جاهزة؟ (ملف الجلسة · التوكيل · الكارنيه · الشاحن)')

# ======================= MON 2026-11-02 =======================
D='2026-11-02'
post('p02_1000','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:60px">رجعت لقضية <span class="gold">بعد سنة</span>؟ 📆</div></div>
<div class="box row" style="top:300px;gap:28px">
 <div class="glass" style="flex:1;padding:34px 30px;border-color:rgba(252,165,165,.35)">
  <div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5;font-size:26px">قبل: بالورق</div>
  <div class="col" style="gap:22px;margin-top:26px;font-size:32px;font-weight:700;line-height:1.45">
   <div>🗄️ تدوّر في الأرشيف</div><div>📄 تقرا الحافظة من الأول</div><div>🧩 تجمّع التفاصيل من ذاكرتك</div></div>
 </div>
 <div class="glass" style="flex:1;padding:34px 30px;border-color:rgba(217,178,95,.65)">
  <div class="tag" style="font-size:26px">بعد: مع ميزان برو</div>
  <div class="col" style="gap:22px;margin-top:26px;font-size:32px;font-weight:700;line-height:1.45">
   <div>📁 تفتح ملف القضية</div><div>📝 تبدأ من الملخص</div><div>✅ وتكمّل من مكان ما وقفت</div></div>
 </div>
</div>
<div class="box center" style="top:800px"><div style="font-size:36px;font-weight:900">ذاكرتك للقضايا الجديدة… <span class="gold">والقديمة في ملفها</span></div>
<div class="small" style="font-size:26px;margin-top:10px">جرّب 14 يوم مجانًا</div></div>''',pill='قبل / بعد 🔄')
add(date=D,time='10:00',kind='post',media=['p02_1000.png'],
 text='رجعت لقضية بعد سنة؟ 📆\n\nقبل (بالورق): 🗄️ تدوّر في الأرشيف · 📄 تقرا الحافظة من الأول · 🧩 تجمّع التفاصيل من ذاكرتك\nبعد (مع ميزان برو): 📁 تفتح ملف القضية · 📝 تبدأ من الملخص · ✅ وتكمّل من مكان ما وقفت\n\nذاكرتك للقضايا الجديدة… والقديمة في ملفها.\nجرّب 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='قبل/بعد: الرجوع لقضية قديمة بعد سنة — الأرشيف ضد ملف القضية والملخص')

video('v02_1200','''
<div class="sc" data-a="0" data-b="3.2">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:30px">ذكاء اصطناعي بأمان 🤖</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:30px">اكتب طلبك<br>للذكاء الاصطناعي <span class="gold">صح</span></div>
</div>
<div class="sc" data-a="3" data-b="10.2">
 <div class="col" style="width:100%;gap:28px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:30px 36px"><div class="num" style="width:76px;height:76px;font-size:40px">1</div><div style="text-align:right"><div class="t" style="font-size:46px">السياق</div><div class="d" style="font-size:30px">ده نوع المستند إيه؟</div></div></div>
  <div class="glass li" data-fx="right" data-at="1.6" style="padding:30px 36px"><div class="num" style="width:76px;height:76px;font-size:40px">2</div><div style="text-align:right"><div class="t" style="font-size:46px">المطلوب بالظبط</div><div class="d" style="font-size:30px">تلخيص؟ نقاط؟ تواريخ؟</div></div></div>
  <div class="glass li" data-fx="right" data-at="3" style="padding:30px 36px"><div class="num" style="width:76px;height:76px;font-size:40px">3</div><div style="text-align:right"><div class="t" style="font-size:46px">شكل الرد</div><div class="d" style="font-size:30px">قايمة · جدول · فقرة قصيرة</div></div></div>
 </div>
</div>
<div class="sc" data-a="10" data-b="13.4">
 <div style="font-size:48px;font-weight:800" data-fx="rise" data-at=".1">مثال 👇</div>
 <div class="paper" data-fx="pop" data-at=".4" style="padding:36px 44px;margin-top:30px;font-size:44px;font-weight:800;line-height:1.6;text-align:right">"لخّص المذكرة دي في 5 نقاط،<br>وطلّعلي التواريخ المهمة في جدول"</div>
 <div class="lead" data-fx="rise" data-at="1.2" style="font-size:34px;margin-top:30px">من غير بيانات شخصية… وراجع على الأصل ✅</div>
</div>
<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:90px;margin-top:16px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px">نظام إدارة متكامل لمكاتب المحاماة</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
add(date=D,time='12:00',kind='post',video=dict(src='v02_1200',D=16,preset='cm',seed=212,bpm=96,trans='3,10,13.2',pat=0),media=['v02_1200.mp4'],title='اكتب طلبك للذكاء الاصطناعي صح | ميزان برو',
 text='اكتب طلبك للذكاء الاصطناعي صح 🤖\n\n1️⃣ السياق: ده نوع المستند إيه؟\n2️⃣ المطلوب بالظبط: تلخيص؟ نقاط؟ تواريخ؟\n3️⃣ شكل الرد: قايمة، جدول، فقرة قصيرة\n\nمثال: "لخّص المذكرة دي في 5 نقاط، وطلّعلي التواريخ المهمة في جدول"\n\n⚠️ من غير بيانات شخصية للموكل… وراجع دايمًا على الأصل.\nاحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='فيديو موشن ذكاء اصطناعي بأمان: إزاي تكتب طلبك صح (سياق · مطلوب · شكل الرد)')

post('p02_1800','''
<div class="glowc" style="width:900px;height:900px;left:90px;top:120px"></div>
<div class="box center" style="top:190px">
 <div class="gold" style="font-family:Messiri;font-size:220px;line-height:.7;height:130px">“</div>
 <div class="h1" style="font-size:64px;line-height:1.5">الموكل ممكن ينسى<br>تفاصيل القضية…<br><span class="gold">لكن عمره ما ينسى</span><br><span class="gold">إنك كنت مهتم</span></div>
 <div class="line" style="width:300px;margin:40px auto 0"></div>
</div>''',pill='جملة للمحامي ✨',foot='شاركها مع زميل')
add(date=D,time='18:00',kind='post',media=['p02_1800.png'],
 text='«الموكل ممكن ينسى تفاصيل القضية… لكن عمره ما ينسى إنك كنت مهتم» ✨\n\nتوافق؟ شاركها مع زميل 🤝\nmezan.pro'+TAGS,
 idea='جملة تحفيزية: «الموكل ممكن ينسى التفاصيل… لكن مش هينسى إنك كنت مهتم»')

story('s02_1100','''
<div class="center" style="position:absolute;top:390px;left:60px;right:60px"><div style="font-size:76px;font-weight:900;line-height:1.3">اختار اللي<br><span class="gold">يناسبك</span> 🏷️</div></div>
<div class="glass center" style="position:absolute;top:720px;left:110px;right:110px;padding:40px">
 <div style="font-size:44px;font-weight:800;color:var(--mute)">شهري</div>
 <div style="font-size:120px;font-weight:900;line-height:1.2"><span class="gold" style="font-family:CairoL">200</span> ج</div>
</div>
<div class="glass center" style="position:absolute;top:1010px;left:110px;right:110px;padding:40px;border-color:rgba(217,178,95,.7)">
 <div style="font-size:44px;font-weight:800;color:var(--mute)">سنوي</div>
 <div style="font-size:120px;font-weight:900;line-height:1.2"><span class="gold" style="font-family:CairoL">2000</span> ج</div>
</div>
<div class="center" style="position:absolute;top:1340px;left:60px;right:60px;font-size:54px;font-weight:900">وابدأ بـ <span class="gold">14 يوم مجانًا</span> 🎁</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='11:00',kind='story',media=['s02_1100.png'],idea='قصة أسعار: اختار اللي يناسبك — شهري 200 ج / سنوي 2000 ج + 14 يوم مجانًا')

video('sv02_1500','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🏷️</div>
 <div style="font-size:80px;font-weight:900;line-height:1.35;margin-top:20px" data-fx="rise" data-at=".4">سمّي ملفاتك<br><span class="gold">بنفس الطريقة</span><br>كل مرة</div>
</div>
<div class="sc" data-a="3.4" data-b="8.6">
 <div class="col" style="width:100%;gap:26px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">1</div><div class="t" style="font-size:56px">التاريخ 📅</div></div>
  <div class="glass li" data-fx="right" data-at=".9" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">2</div><div class="t" style="font-size:56px">رقم القضية 🔢</div></div>
  <div class="glass li" data-fx="right" data-at="1.6" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">3</div><div class="t" style="font-size:56px">نوع المستند 📄</div></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:60px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".1">ولا تاني مرة<br><span class="gold">"نهائي_جديد_نهائي"</span> 😅</div>
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv02_1500',D=12,preset='c',seed=215,bpm=104,trans='3.4,8.4',pat=2),media=['sv02_1500.mp4'],idea='قصة فيديو تنظيم: سمّي ملفاتك بنفس الطريقة (التاريخ · رقم القضية · نوع المستند)')

story('s02_2030','''
<div class="center" style="position:absolute;top:400px;left:60px;right:60px"><div class="pill" style="font-size:34px;display:inline-block">أسئلة شائعة ❓</div><div style="font-size:90px;font-weight:900;line-height:1.3;margin-top:40px">ميزان برو<br><span class="gold">لمين؟</span></div></div>
<div style="position:absolute;top:880px;left:110px;right:110px" class="col">
 <div class="glass li" style="padding:36px 40px;gap:30px"><div class="ic" style="width:110px;height:110px;font-size:62px">👨‍💼</div><div style="font-size:54px;font-weight:900">للمحامين</div></div>
 <div class="glass li" style="padding:36px 40px;gap:30px"><div class="ic" style="width:110px;height:110px;font-size:62px">🏛️</div><div style="font-size:54px;font-weight:900">ولمكاتب المحاماة</div></div>
</div>
<div class="center" style="position:absolute;top:1340px;left:60px;right:60px;font-size:52px;font-weight:900">في <span class="gold">مصر</span> 🇪🇬</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='20:30',kind='story',media=['s02_2030.png'],idea='قصة أسئلة شائعة: ميزان برو لمين؟ للمحامين ومكاتب المحاماة في مصر')

# ======================= TUE 2026-11-03 =======================
D='2026-11-03'
post('p03_1000_1','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:200px"></div>
<div class="center" style="position:absolute;top:220px;left:60px;right:60px">
 <div style="display:inline-grid;place-items:center;width:190px;height:190px;border-radius:40px;background:rgba(217,178,95,.12);border:2px solid rgba(217,178,95,.5);font-size:100px">🤝</div>
 <div class="h1" style="font-size:74px;margin-top:30px">أول مقابلة<br>مع <span class="gold">موكل جديد</span></div>
 <div class="lead" style="margin-top:14px;font-size:34px">4 حاجات لازم تخرج بيها</div>
</div>''',pill='مع الموكلين 🤝',foot='اسحب ←',dots=(1,4))
post('p03_1000_2','''
<div class="box col" style="top:200px;gap:44px">
 <div class="glass" style="padding:50px 44px"><div class="row" style="align-items:center"><div class="num" style="width:76px;height:76px;font-size:40px">1</div><div style="font-size:48px;font-weight:900">الحكاية <span class="gold">بترتيبها الزمني</span> 🕰️</div></div><div class="lead" style="font-size:30px;margin-top:16px">إيه اللي حصل… وإمتى؟ بالتواريخ.</div></div>
 <div class="glass" style="padding:50px 44px"><div class="row" style="align-items:center"><div class="num" style="width:76px;height:76px;font-size:40px">2</div><div style="font-size:48px;font-weight:900">المستندات: <span class="gold">الموجود والناقص</span> 📄</div></div><div class="lead" style="font-size:30px;margin-top:16px">اكتب قايمة باللي استلمته واللي لسه مطلوب.</div></div>
</div>''',foot='اسحب ←',dots=(2,4))
post('p03_1000_3','''
<div class="box col" style="top:200px;gap:44px">
 <div class="glass" style="padding:50px 44px"><div class="row" style="align-items:center"><div class="num" style="width:76px;height:76px;font-size:40px">3</div><div style="font-size:48px;font-weight:900">هو عايز يوصل <span class="gold">لإيه بالظبط</span>؟ 🎯</div></div><div class="lead" style="font-size:30px;margin-top:16px">توقعاته من الأول… بتوفّر سوء فهم بعدين.</div></div>
 <div class="glass" style="padding:50px 44px"><div class="row" style="align-items:center"><div class="num" style="width:76px;height:76px;font-size:40px">4</div><div style="font-size:48px;font-weight:900">الخطوة الجاية <span class="gold">وميعادها</span> 📅</div></div><div class="lead" style="font-size:30px;margin-top:16px">يخرج من عندك عارف هيحصل إيه بعد كده.</div></div>
</div>''',foot='اسحب ←',dots=(3,4))
post('p03_1000_4','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:150px"></div>
<div class="center" style="position:absolute;top:230px;left:60px;right:60px">
 <div style="font-size:120px">📁</div>
 <div class="h1" style="font-size:64px;margin-top:20px">واكتب ده كله<br>في <span class="gold">ملف القضية</span><br>من أول يوم</div>
 <div class="btn" style="margin-top:44px">جرّب ميزان برو 14 يوم مجانًا</div>
 <div class="url" style="margin-top:26px;font-size:44px;color:var(--gold2)">mezan.pro</div>
</div>''',foot='احفظ البوست 🔖',dots=(4,4))
add(date=D,time='10:00',kind='post',media=['p03_1000_1.png','p03_1000_2.png','p03_1000_3.png','p03_1000_4.png'],
 text='أول مقابلة مع موكل جديد 🤝 — 4 حاجات لازم تخرج بيها:\n\n1️⃣ الحكاية بترتيبها الزمني 🕰️\n2️⃣ المستندات: الموجود والناقص 📄\n3️⃣ هو عايز يوصل لإيه بالظبط؟ 🎯\n4️⃣ الخطوة الجاية وميعادها 📅\n\nواكتب ده كله في ملف القضية من أول يوم 📁\nاحفظ البوست 🔖\nجرّب ميزان برو 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='كاروسيل 4 صور: أول مقابلة مع موكل جديد — 4 حاجات تخرج بيها')

video('v03_1200','''
<div class="sc" data-a="0" data-b="2.8">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:30px">أسئلة شائعة ❓</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:96px;margin-top:30px">ميزان برو<br><span class="gold">في 4 أسئلة</span></div>
</div>
<div class="sc" data-a="2.6" data-b="5.4">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:40px">يعني إيه؟</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:70px;margin-top:30px">نظام إدارة متكامل <span class="gold">(ERP)</span><br>لمكاتب المحاماة 🗂️</div>
</div>
<div class="sc" data-a="5.2" data-b="8.2">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:40px">فين الذكاء الاصطناعي؟</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:60px;margin-top:30px">بيلخّص أوراق ومستندات<br>القضية 🤖 <span class="gold">ويربط الملخص بملفها</span></div>
</div>
<div class="sc" data-a="8" data-b="10.8">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:40px">وبياناتي؟</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:70px;margin-top:30px">حمايتها وسريتها<br><span class="gold">أولوية</span> 🔒</div>
</div>
<div class="sc" data-a="10.6" data-b="13.4">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:40px">بكام؟</div>
 <div class="row" style="gap:30px;margin-top:34px">
  <div class="glass" data-fx="pop" data-at=".4" style="padding:30px 44px"><div style="font-size:84px;font-weight:900"><span class="gold" style="font-family:CairoL">200</span> ج</div><div class="small" style="font-size:32px">شهري</div></div>
  <div class="glass" data-fx="pop" data-at=".7" style="padding:30px 44px"><div style="font-size:84px;font-weight:900"><span class="gold" style="font-family:CairoL">2000</span> ج</div><div class="small" style="font-size:32px">سنوي</div></div>
 </div>
 <div style="font-size:50px;font-weight:900;margin-top:30px" data-fx="rise" data-at="1.1">+ <span class="gold">14 يوم مجانًا</span> 🎁</div>
</div>
<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:90px;margin-top:16px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px">عندك سؤال تاني؟ اكتبه في الكومنتات</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
add(date=D,time='12:00',kind='post',video=dict(src='v03_1200',D=16,preset='a',seed=312,bpm=106,trans='2.6,5.2,8,10.6,13.2',pat=3),media=['v03_1200.mp4'],title='ميزان برو في 4 أسئلة',
 text='ميزان برو في 4 أسئلة ❓\n\n🗂️ يعني إيه؟ نظام إدارة متكامل (ERP) لمكاتب المحاماة.\n🤖 فين الذكاء الاصطناعي؟ بيلخّص أوراق ومستندات القضية ويربط الملخص بملفها.\n🔒 وبياناتي؟ حمايتها وسريتها أولوية.\n💳 بكام؟ 200 ج شهري أو 2000 ج سنوي + 14 يوم تجربة مجانية.\n\nعندك سؤال تاني؟ اكتبه في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن أسئلة شائعة: ميزان برو في 4 أسئلة (إيه؟ الذكاء الاصطناعي؟ البيانات؟ بكام؟)')

post('p03_1800','''
<div class="box" style="top:160px;display:flex;align-items:center;gap:50px">
 <svg width="330" height="330" viewBox="0 0 330 330" style="flex:none"><circle cx="165" cy="165" r="140" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="26"/><circle cx="165" cy="165" r="140" fill="none" stroke="#d9b25f" stroke-width="26" stroke-linecap="round" stroke-dasharray="660 880" transform="rotate(-90 165 165)"/><text x="165" y="180" text-anchor="middle" font-family="CairoL" font-weight="700" font-size="104" fill="#f3d998">90</text><text x="165" y="235" text-anchor="middle" font-family="Cairo" font-weight="800" font-size="34" fill="#9fb0cf">دقيقة</text></svg>
 <div><div class="h1" style="font-size:64px">بلوك <span class="gold">تركيز</span><br>للمذكرة 🎯</div><div class="lead" style="margin-top:10px">بدل ما تكتبها على فترات متقطعة</div></div>
</div>
<div class="box col" style="top:520px;gap:20px">
 <div class="glass li" style="padding:20px 32px"><div class="ic">📵</div><div class="t" style="font-size:36px">الموبايل بعيد… والإشعارات مقفولة</div></div>
 <div class="glass li" style="padding:20px 32px"><div class="ic">📄</div><div class="t" style="font-size:36px">قضية واحدة بس قدامك</div></div>
 <div class="glass li" style="padding:20px 32px"><div class="ic">☕</div><div class="t" style="font-size:36px">بعدها بريك 10 دقايق تستاهله</div></div>
</div>''',pill='نصيحة وقت ⏳',foot='جرّبها بكرة')
add(date=D,time='18:00',kind='post',media=['p03_1800.png'],
 text='بلوك تركيز 90 دقيقة للمذكرة 🎯\nبدل ما تكتبها على فترات متقطعة:\n\n📵 الموبايل بعيد… والإشعارات مقفولة\n📄 قضية واحدة بس قدامك\n☕ بعدها بريك 10 دقايق تستاهله\n\nجرّبها بكرة وقولنا النتيجة 👇\nmezan.pro'+TAGS,
 idea='نصيحة وقت: بلوك تركيز 90 دقيقة لكتابة المذكرة')

video('sv03_1100','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🏛️</div>
 <div style="font-size:82px;font-weight:900;line-height:1.35;margin-top:20px" data-fx="rise" data-at=".4">قبل ما تخرج<br>من <span class="gold">المحكمة</span>…</div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:28px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">✍️</div><div class="t" style="font-size:54px">سجّل القرار</div></div>
  <div class="glass li" data-fx="right" data-at="1" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">📅</div><div class="t" style="font-size:54px">اكتب الميعاد الجاي</div></div>
  <div class="glass li" data-fx="right" data-at="1.8" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">📲</div><div class="t" style="font-size:54px">بلّغ الموكل</div></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:72px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".1">3 دقايق دلوقتي…<br><span class="gold">توفّر عليك كتير</span></div>
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv03_1100',D=12,preset='em',seed=331,bpm=98,trans='3.2,8.4',pat=0),media=['sv03_1100.mp4'],idea='قصة فيديو تنظيم: قبل ما تخرج من المحكمة — سجّل القرار · الميعاد الجاي · بلّغ الموكل')

story('s03_1500','''
<div class="center" style="position:absolute;top:400px;left:60px;right:60px"><div style="font-size:84px;font-weight:900;line-height:1.3">بتكتب مذكراتك<br><span class="gold">على إيه؟</span></div></div>
<div style="position:absolute;top:760px;left:110px;right:110px" class="col">
 <div class="glass li" style="padding:34px 44px;gap:30px"><div style="font-size:90px">💻</div><div style="font-size:60px;font-weight:900">الكمبيوتر</div></div>
 <div class="glass li" style="padding:34px 44px;gap:30px"><div style="font-size:90px">📝</div><div style="font-size:60px;font-weight:900">ورقة وقلم</div></div>
 <div class="glass li" style="padding:34px 44px;gap:30px"><div style="font-size:90px">🔁</div><div style="font-size:60px;font-weight:900">الاتنين</div></div>
</div>
<div class="center" style="position:absolute;top:1420px;left:60px;right:60px;font-size:46px;font-weight:800;color:#c9d4ea">ابعتلنا إجابتك 📩</div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='15:00',kind='story',media=['s03_1500.png'],idea='قصة سؤال: بتكتب مذكراتك على إيه؟ كمبيوتر / ورقة وقلم / الاتنين')

story('s03_2030','''
<div class="center" style="position:absolute;top:390px;left:60px;right:60px"><div style="font-size:110px">🤖</div><div style="font-size:66px;font-weight:900;line-height:1.35;margin-top:10px">جرّب تسأل<br>الذكاء الاصطناعي:</div></div>
<div class="paper center" style="position:absolute;top:800px;left:100px;right:100px;padding:50px 40px;font-size:56px;font-weight:900;line-height:1.5">"إيه الأسئلة اللي<br>ممكن الطرف التاني<br>يثيرها هنا؟"</div>
<div class="center" style="position:absolute;top:1250px;left:80px;right:80px;font-size:46px;font-weight:800;line-height:1.5">من غير بيانات الموكل…<br><span class="gold">والتقييم قرارك إنت</span></div>
<div class="url center" style="position:absolute;top:1560px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
add(date=D,time='20:30',kind='story',media=['s03_2030.png'],idea='قصة ذكاء اصطناعي: اسأله «إيه الأسئلة اللي ممكن الطرف التاني يثيرها؟» والتقييم قرارك')

json.dump(M,open('mw1.json','w'),ensure_ascii=False,indent=1);print('ok',len(M))
