from lib import *
import json
M=[]
TAGS='\n\n#ميزان_برو #محاماة'
def add(**k): M.append(k)
END_P='''<div class="sc" data-a="{a}" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:90px;margin-top:16px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px">{line}</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>'''
END_S='''<div class="sc" data-a="{a}" data-b="12.3">
 <div style="font-size:74px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".1">{line}</div>
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>'''

# ======================= SAT 2026-11-07 =======================
D='2026-11-07'
post('p07_1000','''
<div class="box" style="top:160px"><div class="h1" style="font-size:70px">ورقة جديدة وصلت؟</div><div class="h1" style="font-size:70px"><span class="gold">ليها مكان واحد بس</span> 📥</div></div>
<div class="box row" style="top:420px;gap:24px">
 <div class="glass center" style="flex:1;padding:34px 20px"><div style="font-size:84px">📥</div><div style="font-size:34px;font-weight:900;margin-top:10px">صندوق وارد</div><div class="small" style="font-size:24px;margin-top:6px">أي ورقة جديدة<br>تدخله الأول</div></div>
 <div class="glass center" style="flex:1;padding:34px 20px"><div style="font-size:84px">🕔</div><div style="font-size:34px;font-weight:900;margin-top:10px">آخر اليوم</div><div class="small" style="font-size:24px;margin-top:6px">تفرزه في<br>ربع ساعة</div></div>
 <div class="glass center" style="flex:1;padding:34px 20px;border-color:rgba(217,178,95,.6)"><div style="font-size:84px">📁</div><div style="font-size:34px;font-weight:900;margin-top:10px">ملف القضية</div><div class="small" style="font-size:24px;margin-top:6px">كل ورقة<br>في ملف قضيتها</div></div>
</div>
<div class="box center" style="top:820px;font-size:34px;font-weight:800">مفيش ورق «طاير» على المكتب… <span class="gold">ومفيش ورقة تضيع</span></div>''',pill='نصيحة تنظيم 🗂️',foot='احفظ البوست 🔖')
add(date=D,time='10:00',kind='post',media=['p07_1000.png'],
 text='ورقة جديدة وصلت؟ ليها مكان واحد بس 📥\n\n1️⃣ صندوق وارد واحد: أي ورقة جديدة تدخله الأول\n2️⃣ آخر اليوم: تفرزه في ربع ساعة\n3️⃣ كل ورقة تروح ملف قضيتها\n\nمفيش ورق "طاير" على المكتب… ومفيش ورقة تضيع.\nجرّبها من النهارده واحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='نصيحة تنظيم: «صندوق وارد واحد» لأي ورقة جديدة وفرزه آخر اليوم')

video('v07_1400','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="drop" data-at=".1">🛍️</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:20px">موكل جديد<br>جالك <span class="gold">بشنطة ورق</span>…</div>
</div>
<div class="sc" data-a="3.2" data-b="7.2">
 <div class="h2" data-fx="rise" data-at=".1">وانت قدامك:</div>
 <div class="row" style="gap:26px;margin-top:40px">
  <div class="glass" data-fx="pop" data-at=".4" style="padding:30px 34px;font-size:40px;font-weight:800">📄 عقود</div>
  <div class="glass" data-fx="pop" data-at=".7" style="padding:30px 34px;font-size:40px;font-weight:800">🧾 إيصالات</div>
  <div class="glass" data-fx="pop" data-at="1" style="padding:30px 34px;font-size:40px;font-weight:800">✉️ مراسلات</div>
 </div>
 <div class="lead" data-fx="rise" data-at="1.5" style="margin-top:40px;font-size:40px">ومحتاج تفهم القصة <span class="gold">بسرعة</span></div>
</div>
<div class="sc" data-a="7" data-b="12.4">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:30px">مع ميزان برو ✨</div>
 <div class="col" style="gap:26px;margin-top:40px;width:820px">
  <div class="glass li" data-fx="right" data-at=".4" style="padding:26px 34px"><div class="num">1</div><div class="t" style="font-size:42px">افتح للقضية ملف 📁</div></div>
  <div class="glass li" data-fx="right" data-at="1.1" style="padding:26px 34px"><div class="num">2</div><div class="t" style="font-size:42px">الذكاء الاصطناعي يلخّص الأوراق 🤖</div></div>
  <div class="glass li" data-fx="right" data-at="1.8" style="padding:26px 34px"><div class="num">3</div><div class="t" style="font-size:42px">الملخص يتربط بملف القضية 🔗</div></div>
 </div>
</div>
'''+END_P.format(a='12.2',line='وابدأ من الفهم… مش من الكوم'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v07_1400',D=16,preset='fm',seed=714,bpm=98,trans='3.2,7,12.2',pat=2),media=['v07_1400.mp4'],title='موكل جديد بشنطة ورق | ميزان برو',
 text='موكل جديد جالك بشنطة ورق؟ 🛍️\nعقود وإيصالات ومراسلات… ومحتاج تفهم القصة بسرعة.\n\nمع ميزان برو:\n1️⃣ افتح للقضية ملف\n2️⃣ الذكاء الاصطناعي يلخّص أوراقها ومستنداتها\n3️⃣ الملخص يتربط بملف القضية\n\nوابدأ من الفهم… مش من الكوم.\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='فيديو موشن مشكلة وحلها: موكل جديد بشنطة ورق ← ملف + ملخص بالذكاء الاصطناعي')

post('p07_1900','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:68px">بتراجع ملف القضية<br><span class="gold">إمتى؟</span> 🤔</div></div>
<div class="box" style="top:400px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 <div class="glass li" style="padding:28px 30px"><div class="num">أ</div><div class="t">ليلة الجلسة 🌙</div></div>
 <div class="glass li" style="padding:28px 30px"><div class="num">ب</div><div class="t">قبلها بيومين 📅</div></div>
 <div class="glass li" style="padding:28px 30px"><div class="num">ج</div><div class="t">قبلها بأسبوع 🗓️</div></div>
 <div class="glass li" style="padding:28px 30px"><div class="num">د</div><div class="t">أول بأول ✅</div></div>
</div>
<div class="box center" style="top:780px;font-size:36px;font-weight:800">اكتب الحرف في الكومنتات 👇 <span class="gold">وخلّينا نشوف</span></div>''',pill='سؤال للمحامين 💬',foot='شاركنا رأيك')
add(date=D,time='19:00',kind='post',media=['p07_1900.png'],
 text='سؤال سريع يا متر 🤔\nبتراجع ملف القضية إمتى؟\n\nأ) ليلة الجلسة 🌙\nب) قبلها بيومين 📅\nج) قبلها بأسبوع 🗓️\nد) أول بأول ✅\n\nاكتب الحرف في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='سؤال تفاعلي: بتراجع ملف القضية إمتى؟ (أ/ب/ج/د)')

sflow('s07_1100','''
<div class="gold" style="font-family:Messiri;font-size:260px;line-height:.7;height:150px">“</div>
<div style="font-size:104px;font-weight:900;line-height:1.35">الدقة<br>مش <span class="gold">رفاهية</span>…</div>
<div class="line" style="width:300px;margin:0 auto"></div>
<div style="font-size:72px;font-weight:900;line-height:1.4">دي <span class="gold">أساس شغلك</span><br>يا متر ⚖️</div>''',gap=50)
add(date=D,time='11:00',kind='story',media=['s07_1100.png'],idea='قصة اقتباس: «الدقة مش رفاهية… دي أساس شغلك»')

video('sv07_1500','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🤖</div>
 <div style="font-size:78px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">الذكاء الاصطناعي<br>قالك معلومة<br><span class="gold">من المستند؟</span></div>
</div>
<div class="sc" data-a="3.4" data-b="8.4">
 <div style="font-size:60px;font-weight:900" data-fx="rise" data-at=".1">اسأله على طول:</div>
 <div class="paper" data-fx="pop" data-at=".6" style="padding:50px 44px;margin-top:50px;font-size:62px;font-weight:900;line-height:1.5">«الكلام ده<br>موجود فين<br>في المستند؟» 🔍</div>
 <div style="font-size:48px;font-weight:800;margin-top:50px;line-height:1.5" data-fx="rise" data-at="1.6">وارجع للمكان ده<br><span class="gold">بعينك</span> 👀</div>
</div>
'''+END_S.format(a='8.2',line='الأصل هو<br><span class="gold">المرجع دايمًا</span> ✅'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv07_1500',D=12,preset='g',seed=715,bpm=110,trans='3.4,8.2',pat=3),media=['sv07_1500.mp4'],idea='قصة فيديو ذكاء اصطناعي: اسأله «الكلام ده موجود فين في المستند؟» وارجع للأصل')

sflow('s07_2030','''
<div style="font-size:66px;font-weight:900;line-height:1.35">الاشتراك السنوي<br>في ميزان برو</div>
<div class="glass" style="padding:40px;margin:0 60px"><div style="font-size:150px;font-weight:900;line-height:1.2"><span class="gold" style="font-family:CairoL">2000</span> ج</div><div style="font-size:44px;font-weight:800;color:var(--mute)">في السنة</div></div>
<div style="font-size:60px;font-weight:900;line-height:1.45">يعني <span class="gold">أقل من 6 ج</span><br>في اليوم ☕</div>
<div style="font-size:46px;font-weight:800;color:#c9d4ea">وابدأ بـ 14 يوم مجانًا 🎁</div>''',gap=46)
add(date=D,time='20:30',kind='story',media=['s07_2030.png'],idea='قصة أسعار: السنوي 2000 ج = أقل من 6 ج في اليوم + 14 يوم مجانًا')

# ======================= SUN 2026-11-08 =======================
D='2026-11-08'
video('v08_1000','''
<div class="sc" data-a="0" data-b="3.2">
 <div style="font-size:140px" data-fx="drop" data-at=".1">🏖️</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:80px;margin-top:20px">واخد إجازة…<br>وزميلك <span class="gold">هيحضر جلستك</span></div>
</div>
<div class="sc" data-a="3" data-b="7.6">
 <div class="tag" data-fx="rise" data-at=".1" style="background:rgba(252,165,165,.15);color:#fca5a5;font-size:32px">من غير نظام 😓</div>
 <div class="col" style="gap:22px;margin-top:36px;width:800px">
  <div class="glass" data-fx="left" data-at=".4" style="padding:24px 34px;font-size:40px;font-weight:800">📞 مكالمة ساعة تشرح القضية</div>
  <div class="glass" data-fx="left" data-at=".9" style="padding:24px 34px;font-size:40px;font-weight:800">🗄️ «الورقة في الدرج التاني»</div>
  <div class="glass" data-fx="left" data-at="1.4" style="padding:24px 34px;font-size:40px;font-weight:800">📱 وإجازتك كلها تليفونات</div>
 </div>
</div>
<div class="sc" data-a="7.4" data-b="12.4">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:32px">مع ميزان برو 😌</div>
 <div class="col" style="gap:22px;margin-top:36px;width:800px">
  <div class="glass" data-fx="right" data-at=".4" style="padding:24px 34px;font-size:40px;font-weight:800;border-color:rgba(217,178,95,.6)">📁 ملف القضية جاهز قدامه</div>
  <div class="glass" data-fx="right" data-at=".9" style="padding:24px 34px;font-size:40px;font-weight:800;border-color:rgba(217,178,95,.6)">🤖 ملخص الأوراق مربوط بالملف</div>
  <div class="glass" data-fx="right" data-at="1.4" style="padding:24px 34px;font-size:40px;font-weight:800;border-color:rgba(217,178,95,.6)">🌴 وانت تستمتع بإجازتك</div>
 </div>
</div>
'''+END_P.format(a='12.2',line='القضية مش في دماغك لوحدك'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v08_1000',D=16,preset='c',seed=810,bpm=94,trans='3,7.4,12.2',pat=1),media=['v08_1000.mp4'],title='زميلك هيحضر جلستك | ميزان برو',
 text='واخد إجازة… وزميلك هيحضر جلستك 🏖️\n\nمن غير نظام 😓\n📞 مكالمة ساعة تشرح القضية\n🗄️ "الورقة في الدرج التاني"\n📱 وإجازتك كلها تليفونات\n\nمع ميزان برو 😌\n📁 ملف القضية جاهز قدامه\n🤖 ملخص الأوراق مربوط بالملف\n🌴 وانت تستمتع بإجازتك\n\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='فيديو موشن قبل/بعد: زميلك هيحضر جلستك وانت في إجازة — بالورق ضد مع ميزان برو')

post('p08_1400','''
<div class="box" style="top:160px"><div class="h1" style="font-size:64px">آخر يوم في الميعاد<br>جه <span class="gold">إجازة رسمية؟</span> 🗓️</div></div>
<div class="box" style="top:420px;display:flex;align-items:center;gap:20px;justify-content:center">
 <div class="glass center" style="width:250px;padding:26px"><div class="small">آخر يوم</div><div style="font-size:64px">🏖️</div><div style="font-size:30px;font-weight:900">إجازة رسمية</div></div>
 <div style="font-size:64px;color:var(--gold2);font-family:CairoL">←</div>
 <div class="glass center" style="width:330px;padding:26px;border-color:rgba(217,178,95,.7)"><div class="small">الميعاد يمتد لـ</div><div style="font-size:64px">💼</div><div style="font-size:30px;font-weight:900"><span class="gold">أول يوم عمل</span> بعدها</div></div>
</div>
<div class="box glass" style="top:720px;padding:22px 30px;display:flex;align-items:center;gap:20px"><div style="font-size:44px">📖</div><div style="font-size:28px;font-weight:700;line-height:1.5">المادة 18 مرافعات: «إذا صادف آخر الميعاد عطلة رسمية امتد إلى أول يوم عمل بعدها»</div></div>''',pill='معلومة إجرائية ⚖️',foot='احفظها 🔖')
add(date=D,time='14:00',kind='post',media=['p08_1400.png'],
 text='آخر يوم في الميعاد جه إجازة رسمية؟ 📅\n\nطبقًا للمادة 18 من قانون المرافعات: لو آخر الميعاد صادف عطلة رسمية، الميعاد يمتد لأول يوم عمل بعدها.\n\nومع ذلك… الأمان إنك متستناش لآخر يوم 😉\nسجّل مواعيدك في ملف كل قضية وخليك سابق بخطوة.\n\nاحفظ البوست 🔖 وشاركه مع زميل\nmezan.pro'+TAGS,
 idea='معلومة إجرائية: لو آخر الميعاد صادف عطلة رسمية يمتد لأول يوم عمل بعدها (م.18 مرافعات)')

post('p08_1900','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:66px">مع موكلك: <span class="gold">قول ده</span>… مش ده</div></div>
<div class="box col" style="top:330px;gap:20px">
 <div class="row" style="gap:20px"><div class="glass" style="flex:1;padding:22px 26px;font-size:30px;font-weight:800;border-color:rgba(252,165,165,.35)"><span class="no">✗</span> «القضية مضمونة»</div><div class="glass" style="flex:1.2;padding:22px 26px;font-size:30px;font-weight:800;border-color:rgba(217,178,95,.6)"><span class="ok">✓</span> «هشتغل عليها بكل جهدي»</div></div>
 <div class="row" style="gap:20px"><div class="glass" style="flex:1;padding:22px 26px;font-size:30px;font-weight:800;border-color:rgba(252,165,165,.35)"><span class="no">✗</span> «متقلقش… سيبها عليّا»</div><div class="glass" style="flex:1.2;padding:22px 26px;font-size:30px;font-weight:800;border-color:rgba(217,178,95,.6)"><span class="ok">✓</span> «هبلّغك بكل خطوة أول بأول»</div></div>
 <div class="row" style="gap:20px"><div class="glass" style="flex:1;padding:22px 26px;font-size:30px;font-weight:800;border-color:rgba(252,165,165,.35)"><span class="no">✗</span> «هكلمك بعدين»</div><div class="glass" style="flex:1.2;padding:22px 26px;font-size:30px;font-weight:800;border-color:rgba(217,178,95,.6)"><span class="ok">✓</span> «هرد عليك بكرة الضهر»</div></div>
</div>
<div class="box center" style="top:820px;font-size:34px;font-weight:800">الصراحة والوضوح… <span class="gold">بيبنوا ثقة</span> 🤝</div>''',pill='مع الموكلين 🤝',foot='احفظ البوست 🔖')
add(date=D,time='19:00',kind='post',media=['p08_1900.png'],
 text='مع موكلك: قول ده… مش ده 🤝\n\n✗ "القضية مضمونة"\n✓ "هشتغل عليها بكل جهدي"\n\n✗ "متقلقش… سيبها عليّا"\n✓ "هبلّغك بكل خطوة أول بأول"\n\n✗ "هكلمك بعدين"\n✓ "هرد عليك بكرة الضهر"\n\nالصراحة والوضوح بيبنوا ثقة.\nإنت بتقول إيه لموكلك؟ 👇\nmezan.pro'+TAGS,
 idea='نصيحة تواصل مع الموكلين: «قول ده… مش ده» (3 جمل بدل وعود مش مضمونة)')

video('sv08_1100','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🗂️</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">أي قضية…<br><span class="gold">3 أقسام</span> بس</div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:34px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:34px 40px"><div class="ic" style="width:110px;height:110px;font-size:62px">📄</div><div class="t" style="font-size:60px">المستندات</div></div>
  <div class="glass li" data-fx="right" data-at=".9" style="padding:34px 40px"><div class="ic" style="width:110px;height:110px;font-size:62px">✍️</div><div class="t" style="font-size:60px">المذكرات</div></div>
  <div class="glass li" data-fx="right" data-at="1.6" style="padding:34px 40px"><div class="ic" style="width:110px;height:110px;font-size:62px">✉️</div><div class="t" style="font-size:60px">المراسلات</div></div>
 </div>
</div>
'''+END_S.format(a='8.4',line='وتلاقي أي ورقة<br><span class="gold">بسهولة</span> ⚡'),D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv08_1100',D=12,preset='em',seed=811,bpm=104,trans='3.2,8.4',pat=1),media=['sv08_1100.mp4'],idea='قصة فيديو تنظيم: أي قضية 3 أقسام بس — مستندات · مذكرات · مراسلات')

sflow('s08_1500','''
<div><div class="pill" style="font-size:34px;display:inline-block">أسئلة شائعة ❓</div><div style="font-size:74px;font-weight:900;line-height:1.35;margin-top:30px">يعني إيه الملخص<br><span class="gold">مربوط بملف القضية؟</span></div></div>
<div class="glass" style="padding:50px 40px;margin:0 20px;border-color:rgba(217,178,95,.6)">
 <div style="display:flex;justify-content:center;align-items:center;gap:30px;font-size:110px"><span>🤖</span><span style="font-size:70px;color:var(--gold2)">🔗</span><span>📁</span></div>
 <div style="font-size:54px;font-weight:900;line-height:1.5;margin-top:20px">الملخص بيتحفظ<br><span class="gold">جوه ملف القضية نفسها</span></div>
</div>
<div style="font-size:48px;font-weight:800;color:#c9d4ea;line-height:1.5">ترجعله في أي وقت…<br>من غير ما تدوّر 👌</div>''',gap=56)
add(date=D,time='15:00',kind='story',media=['s08_1500.png'],idea='قصة أسئلة شائعة: يعني إيه الملخص مربوط بملف القضية؟ بيتحفظ جوه ملفها')

sflow('s08_2030','''
<div style="font-size:78px;font-weight:900;line-height:1.35">أكتر جملة<br>بتسمعها <span class="gold">من موكلك؟</span> 😄</div>
<div class="col" style="margin:0 30px;gap:24px">
 <div class="glass li" style="padding:26px 40px;gap:26px"><div class="num" style="width:80px;height:80px;font-size:42px">1</div><div style="font-size:50px;font-weight:900">«هنكسب يا متر؟»</div></div>
 <div class="glass li" style="padding:26px 40px;gap:26px"><div class="num" style="width:80px;height:80px;font-size:42px">2</div><div style="font-size:50px;font-weight:900">«الجلسة الجاية إمتى؟»</div></div>
 <div class="glass li" style="padding:26px 40px;gap:26px"><div class="num" style="width:80px;height:80px;font-size:42px">3</div><div style="font-size:50px;font-weight:900">«هتاخد وقت قد إيه؟»</div></div>
</div>
<div style="font-size:48px;font-weight:800;color:#c9d4ea">ابعتلنا رقمك 📩</div>''',gap=56)
add(date=D,time='20:30',kind='story',media=['s08_2030.png'],idea='قصة سؤال: أكتر جملة بتسمعها من موكلك؟ (هنكسب؟ / الجلسة الجاية إمتى؟ / هتاخد وقت قد إيه؟)')

# ======================= MON 2026-11-09 =======================
D='2026-11-09'
post('p09_1000_1','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:200px"></div>
<div class="center" style="position:absolute;top:220px;left:60px;right:60px">
 <div style="display:inline-grid;place-items:center;width:200px;height:200px;border-radius:40px;background:rgba(217,178,95,.12);border:2px solid rgba(217,178,95,.5);font-size:110px">⏱️</div>
 <div class="h1" style="font-size:78px;margin-top:30px">ميعاد الطعن<br><span class="gold">بيبدأ يتحسب إمتى؟</span></div>
 <div class="lead" style="margin-top:14px;font-size:32px">المادة 213 من قانون المرافعات</div>
</div>''',pill='معلومة إجرائية ⚖️',foot='اسحب ← للتفاصيل',dots=(1,4))
post('p09_1000_2','''
<div class="box" style="top:200px"><div class="tag" style="font-size:28px">القاعدة العامة</div></div>
<div class="box center" style="top:290px"><div class="glass" style="padding:60px 40px;border-color:rgba(217,178,95,.6)"><div style="font-size:100px">🔨</div><div style="font-size:58px;font-weight:900;line-height:1.45;margin-top:10px">من تاريخ <span class="gold">صدور الحكم</span></div><div class="lead" style="margin-top:14px;font-size:30px">ما لم ينص القانون على غير ذلك</div></div></div>''',foot='اسحب ←',dots=(2,4))
post('p09_1000_3','''
<div class="box" style="top:190px"><div class="tag" style="font-size:28px">الاستثناء: من تاريخ <b>إعلان الحكم</b> 📨</div></div>
<div class="box col" style="top:290px;gap:30px">
 <div class="glass" style="padding:40px 40px"><div class="row" style="align-items:center"><div class="num" style="width:70px;height:70px;font-size:38px">1</div><div style="font-size:38px;font-weight:900;line-height:1.45">المحكوم عليه <span class="gold">تخلّف عن الحضور</span> في كل الجلسات… ومقدّمش مذكرة بدفاعه</div></div></div>
 <div class="glass" style="padding:40px 40px"><div class="row" style="align-items:center"><div class="num" style="width:70px;height:70px;font-size:38px">2</div><div style="font-size:38px;font-weight:900;line-height:1.45">حصل سبب من أسباب <span class="gold">انقطاع الخصومة</span> والحكم صدر من غير اختصام مين قام مقام الخصم</div></div></div>
</div>''',foot='اسحب ←',dots=(3,4))
post('p09_1000_4','''
<div class="box center" style="top:210px">
 <div style="font-size:110px">📌</div>
 <div class="h1" style="font-size:64px;margin-top:10px">سجّل تاريخ الحكم<br><span class="gold">في ملف القضية فورًا</span></div>
 <div class="lead" style="margin-top:24px;font-size:32px">ولو الطعن بيبدأ من الإعلان… سجّل تاريخ الإعلان كمان</div>
 <div class="small" style="margin-top:40px;font-size:26px">احفظ البوست 🔖 · <span class="url">mezan.pro</span></div>
</div>''',foot='',dots=(4,4))
add(date=D,time='10:00',kind='post',media=['p09_1000_1.png','p09_1000_2.png','p09_1000_3.png','p09_1000_4.png'],
 text='ميعاد الطعن بيبدأ يتحسب إمتى؟ ⏱️\n\nطبقًا للمادة 213 من قانون المرافعات:\n🔨 القاعدة: من تاريخ صدور الحكم، ما لم ينص القانون على غير ذلك.\n📨 والاستثناء: من تاريخ إعلان الحكم للمحكوم عليه في حالتين:\n1️⃣ لو تخلّف عن الحضور في كل الجلسات ومقدّمش مذكرة بدفاعه\n2️⃣ لو حصل سبب من أسباب انقطاع الخصومة وصدر الحكم من غير اختصام مين قام مقام الخصم\n\n📌 سجّل تاريخ الحكم (وتاريخ الإعلان لو فيه) في ملف القضية فورًا.\nاحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='كاروسيل 4 صور معلومة إجرائية: ميعاد الطعن يبدأ من صدور الحكم، والاستثناءات من الإعلان (م.213 مرافعات)')

video('v09_1400','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">💡</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:78px;margin-top:20px">قبل ما الذكاء الاصطناعي<br><span class="gold">يكتبلك أي حاجة…</span></div>
</div>
<div class="sc" data-a="3.2" data-b="8">
 <div class="h2" data-fx="rise" data-at=".1">قوله في آخر طلبك:</div>
 <div class="paper" data-fx="stamp" data-at=".6" style="padding:44px 50px;margin-top:40px;font-size:50px;font-weight:900;line-height:1.55">«قبل ما تبدأ…<br>اسألني الأسئلة اللي<br>محتاجها علشان تفهم المطلوب»</div>
</div>
<div class="sc" data-a="7.8" data-b="12.4">
 <div class="h2" data-fx="rise" data-at=".1">ليه؟ 🤔</div>
 <div class="col" style="gap:24px;margin-top:36px;width:820px">
  <div class="glass li" data-fx="right" data-at=".4" style="padding:24px 34px"><div class="ic">🎯</div><div class="t" style="font-size:40px">رد أدق على المطلوب</div></div>
  <div class="glass li" data-fx="right" data-at="1" style="padding:24px 34px"><div class="ic">🧩</div><div class="t" style="font-size:40px">بيبان لك الناقص من الأول</div></div>
  <div class="glass li" data-fx="right" data-at="1.6" style="padding:24px 34px"><div class="ic">✅</div><div class="t" style="font-size:40px">وإنت اللي بتراجع وتقرر</div></div>
 </div>
</div>
'''+END_P.format(a='12.2',line='استخدمه صح… واستفيد بأمان'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v09_1400',D=16,preset='bm',seed=914,bpm=102,trans='3.2,7.8,12.2',pat=4),media=['v09_1400.mp4'],title='خلّي الذكاء الاصطناعي يسألك | ميزان برو',
 text='قبل ما الذكاء الاصطناعي يكتبلك أي حاجة… 💡\nقوله في آخر طلبك:\n"قبل ما تبدأ، اسألني الأسئلة اللي محتاجها علشان تفهم المطلوب"\n\nليه؟\n🎯 رد أدق على المطلوب\n🧩 بيبان لك الناقص من الأول\n✅ وفي الآخر إنت اللي بتراجع وتقرر\n\nوافتكر: متحطش بيانات شخصية لموكلك في أي طلب.\nجرّبها وقولنا الفرق 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن ذكاء اصطناعي بأمان: خلّيه يسألك الأسئلة قبل ما يكتب')

post('p09_1900','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:66px">شهري ولا سنوي؟ <span class="gold">إنت تختار</span></div></div>
<div class="box row" style="top:330px;gap:28px">
 <div class="glass center" style="flex:1;padding:34px 26px">
  <div style="font-size:70px">🗓️</div><div style="font-size:38px;font-weight:900;margin-top:6px">شهري</div>
  <div style="font-size:100px;font-weight:900;line-height:1.25"><span class="gold" style="font-family:CairoL">200</span> ج</div>
  <div class="small" style="font-size:26px">كل شهر</div>
 </div>
 <div class="glass center" style="flex:1;padding:34px 26px;border-color:rgba(217,178,95,.7);box-shadow:0 0 60px rgba(217,178,95,.2)">
  <div style="font-size:70px">💼</div><div style="font-size:38px;font-weight:900;margin-top:6px">سنوي</div>
  <div style="font-size:100px;font-weight:900;line-height:1.25"><span class="gold" style="font-family:CairoL">2000</span> ج</div>
  <div class="small" style="font-size:26px">مرة واحدة في السنة</div>
 </div>
</div>
<div class="box center" style="top:850px"><div class="btn">ابدأ بـ 14 يوم مجانًا 🎁</div></div>''',pill='الأسعار 🏷️')
add(date=D,time='19:00',kind='post',media=['p09_1900.png'],
 text='شهري ولا سنوي؟ إنت تختار 🏷️\n\n🗓️ شهري: 200 ج\n📆 سنوي: 2000 ج\n\nوقبل أي اختيار… ابدأ بتجربة مجانية 14 يوم 🎁\nنظام إدارة متكامل لمكتبك، وتلخيص لأوراق القضايا بالذكاء الاصطناعي.\n\n👈 mezan.pro'+TAGS,
 idea='تذكير بالأسعار: مقارنة شهري 200 ج / سنوي 2000 ج + زرار 14 يوم مجانًا')

video('sv09_1100','''
<div class="sc" data-a="0" data-b="4.4">
 <div class="gold" style="font-family:Messiri;font-size:260px;line-height:.7;height:150px" data-fx="fade" data-at=".1">“</div>
 <div style="font-size:90px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".3">موكلك بيدفع<br>عشان <span class="gold">خبرتك</span>…</div>
</div>
<div class="sc" data-a="4.2" data-b="8.6">
 <div style="font-size:84px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".2">مش عشان<br>وقتك وانت<br><span class="gold">بتدوّر على ورقة</span> 🔍</div>
</div>
'''+END_S.format(a='8.4',line='خلّي وقتك<br><span class="gold">للي يستاهل</span> ⚖️'),D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv09_1100',D=12,preset='dm',seed=911,bpm=88,trans='4.2,8.4',pat=0),media=['sv09_1100.mp4'],idea='قصة فيديو اقتباس: «موكلك بيدفع عشان خبرتك… مش عشان وقتك وانت بتدوّر على ورقة»')

sflow('s09_1500','''
<div><div style="font-size:110px">👋</div><div style="font-size:70px;font-weight:900;line-height:1.35">موكل جديد؟<br>ابعتله رسالة <span class="gold">فيها 3 حاجات</span></div></div>
<div class="paper" style="padding:44px 44px;margin:0 30px;text-align:right">
 <div style="font-size:48px;font-weight:900;line-height:1.7">1️⃣ مين هيتابع قضيته</div>
 <div style="font-size:48px;font-weight:900;line-height:1.7">2️⃣ إزاي يتواصل معاك</div>
 <div style="font-size:48px;font-weight:900;line-height:1.7">3️⃣ إيه الخطوة الجاية</div>
</div>
<div style="font-size:52px;font-weight:900">بداية واضحة = <span class="gold">ثقة من أول يوم</span></div>''',gap=56)
add(date=D,time='15:00',kind='story',media=['s09_1500.png'],idea='قصة تعامل مع الموكلين: رسالة ترحيب لموكل جديد فيها 3 حاجات')

sflow('s09_2030','''
<div style="font-size:76px;font-weight:900;line-height:1.35">ملف القضية<br><span class="gold">بيفتكر عنك</span> 🧠</div>
<div style="position:relative;height:660px;margin:0 20px">
 <div class="glass" style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:370px;height:370px;border-radius:50%;display:grid;place-items:center;border-color:rgba(217,178,95,.7)"><div><div style="font-size:120px">📁</div><div style="font-size:44px;font-weight:900">ملف القضية</div></div></div>
 <div class="glass" style="position:absolute;right:0;top:0;padding:20px 30px;font-size:42px;font-weight:800">📄 الأوراق</div>
 <div class="glass" style="position:absolute;left:0;top:0;padding:20px 30px;font-size:42px;font-weight:800">🤖 الملخص</div>
 <div class="glass" style="position:absolute;left:50%;bottom:0;transform:translateX(-50%);padding:20px 30px;font-size:42px;font-weight:800;white-space:nowrap">🔒 في سرية</div>
</div>
<div style="font-size:50px;font-weight:800;color:#c9d4ea">وإنت تركّز في <span class="gold">الدفاع</span></div>''',gap=50)
add(date=D,time='20:30',kind='story',media=['s09_2030.png'],idea='قصة ميزة: ملف القضية بيفتكر عنك — الأوراق + الملخص + السرية')

json.dump(M,open('mw3a.json','w'),ensure_ascii=False,indent=1);print('ok',len(M))
