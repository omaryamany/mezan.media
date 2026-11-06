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
def opt(n,t,at):
    return f'<div class="glass li" data-fx="right" data-at="{at}" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">{n}</div><div class="t" style="font-size:52px">{t}</div></div>'

# ======================= TUE 2026-11-10 =======================
D='2026-11-10'
post('p10_1000','''
<div class="glowc" style="width:900px;height:900px;left:90px;top:120px"></div>
<div class="center" style="position:absolute;top:150px;left:70px;right:70px">
 <div class="gold" style="font-family:Messiri;font-size:240px;line-height:.7;height:130px">“</div>
 <div style="font-size:66px;font-weight:900;line-height:1.5">المحامي الشاطر<br>مش اللي <span class="gold">بيحفظ كل حاجة</span>…</div>
 <div class="line" style="width:260px;margin:34px auto"></div>
 <div style="font-size:66px;font-weight:900;line-height:1.5">ده اللي <span class="gold">عارف يلاقيها</span><br>في الوقت الصح</div>
</div>''',pill='جملة اليوم ✨',foot='شاركها مع زميل 🤝')
add(date=D,time='10:00',kind='post',media=['p10_1000.png'],
 text='«المحامي الشاطر مش اللي بيحفظ كل حاجة… ده اللي عارف يلاقيها في الوقت الصح» ✨\n\nتتفق؟ 👇\nشاركها مع زميل بيعرف قيمة الترتيب 🤝\nmezan.pro'+TAGS,
 idea='اقتباس تحفيزي: «المحامي الشاطر مش اللي بيحفظ كل حاجة… ده اللي عارف يلاقيها في الوقت الصح»')

video('v10_1400','''
<div class="sc" data-a="0" data-b="3.2">
 <div style="font-size:140px" data-fx="drop" data-at=".1">📄</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:20px">رحلة ورقة<br><span class="gold">جوه ميزان برو</span></div>
</div>
<div class="sc" data-a="3" data-b="12.4">
 <div class="col" style="gap:20px;width:860px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:22px 34px"><div class="ic">📥</div><div><div class="t" style="font-size:40px">الورقة توصل</div></div></div>
  <div class="center gold" data-fx="fade" data-at=".9" style="font-size:44px;line-height:1">⬇</div>
  <div class="glass li" data-fx="right" data-at="1.4" style="padding:22px 34px"><div class="ic">📁</div><div><div class="t" style="font-size:40px">تتحفظ في ملف قضيتها</div></div></div>
  <div class="center gold" data-fx="fade" data-at="2.1" style="font-size:44px;line-height:1">⬇</div>
  <div class="glass li" data-fx="right" data-at="2.6" style="padding:22px 34px"><div class="ic">🤖</div><div><div class="t" style="font-size:40px">الذكاء الاصطناعي يلخّصها</div></div></div>
  <div class="center gold" data-fx="fade" data-at="3.3" style="font-size:44px;line-height:1">⬇</div>
  <div class="glass li" data-fx="right" data-at="3.8" style="padding:22px 34px;border-color:rgba(217,178,95,.7)"><div class="ic">🔗</div><div><div class="t" style="font-size:40px">الملخص يتربط بملف القضية</div></div></div>
  <div class="tag center" data-fx="pop" data-at="5" style="font-size:30px;align-self:center;margin-top:10px">🔒 وحماية بياناتك وسريتها أولوية</div>
 </div>
</div>
'''+END_P.format(a='12.2',line='كل ورقة في مكانها… وفهمها جاهز'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v10_1400',D=16,preset='a',seed=1014,bpm=96,trans='3,12.2',pat=2),media=['v10_1400.mp4'],title='رحلة ورقة جوه ميزان برو',
 text='رحلة ورقة جوه ميزان برو 📄\n\n📥 الورقة توصل\n📁 تتحفظ في ملف قضيتها\n🤖 الذكاء الاصطناعي يلخّصها\n🔗 الملخص يتربط بملف القضية\n🔒 وحماية بياناتك وسريتها أولوية\n\nكل ورقة في مكانها… وفهمها جاهز.\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='فيديو موشن ميزة: رحلة ورقة جوه ميزان برو (ملف القضية ← تلخيص ← ربط ← سرية)')

post('p10_1900','''
<div class="box" style="top:150px"><div class="pill" style="display:inline-block;font-size:26px">أسئلة شائعة ❓</div></div>
<div class="box" style="top:240px;display:flex;justify-content:flex-start">
 <div class="glass" style="padding:28px 40px;border-radius:34px 34px 34px 8px;font-size:48px;font-weight:900">أنا محامي شغال لوحدي…<br>ميزان برو <span class="gold">ينفعني؟</span> 🤔</div>
</div>
<div class="box" style="top:520px;display:flex;justify-content:flex-end">
 <div style="padding:30px 44px;border-radius:34px 34px 8px 34px;font-size:46px;font-weight:900;line-height:1.5;color:var(--navy);background:linear-gradient(160deg,var(--gold2),var(--gold) 60%,#b88d3a)">أكيد 👌 ميزان برو معمول<br>للمحامين ومكاتب المحاماة</div>
</div>
<div class="box center" style="top:850px;font-size:32px;font-weight:800">وجرّبه بنفسك <span class="gold">14 يوم مجانًا</span> 🎁</div>''',pill='',foot='نظام إدارة متكامل لمكاتب المحاماة')
add(date=D,time='19:00',kind='post',media=['p10_1900.png'],
 text='❓ «أنا محامي شغال لوحدي… ميزان برو ينفعني؟»\n\nأكيد 👌 ميزان برو معمول للمحامين ومكاتب المحاماة في مصر.\nنظام إدارة متكامل لشغلك، وتلخيص لأوراق ومستندات القضايا بالذكاء الاصطناعي مربوط بملف كل قضية.\n\nجرّبه بنفسك 14 يوم مجانًا 🎁\n👈 mezan.pro\n\nعندك سؤال تاني؟ اكتبه في الكومنتات 👇'+TAGS,
 idea='أسئلة شائعة: «أنا محامي شغال لوحدي… ينفعني؟» — معمول للمحامين ومكاتب المحاماة')

sflow('s10_1100','''
<div style="font-size:72px;font-weight:900;line-height:1.35">زميلك سألك:<br><span class="gold">«فين عقد القضية؟»</span></div>
<div class="glass" style="padding:40px;margin:0 40px;border-color:rgba(252,165,165,.35)"><div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5;font-size:34px">قبل</div><div style="font-size:100px;margin-top:10px">🗄️😵</div><div style="font-size:50px;font-weight:800">«استنى… أدوّر»</div></div>
<div class="glass" style="padding:40px;margin:0 40px;border-color:rgba(217,178,95,.7)"><div class="tag" style="font-size:34px">بعد</div><div style="font-size:100px;margin-top:10px">📁😌</div><div style="font-size:50px;font-weight:800">«في <span class="gold">ملف القضية</span>»</div></div>''',gap=44)
add(date=D,time='11:00',kind='story',media=['s10_1100.png'],idea='قصة قبل/بعد: زميلك سألك «فين عقد القضية؟» — أدوّر ضد في ملف القضية')

video('sv10_1500','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">☀️</div>
 <div style="font-size:86px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">صباحك<br><span class="gold">بيبدأ بإيه؟</span></div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:28px">
  '''+opt(1,'المحكمة على طول ⚖️','.3')+opt(2,'المكتب والورق 🗂️','.8')+opt(3,'مكالمات الموكلين 📞','1.3')+opt(4,'القهوة الأول ☕','1.8')+'''
 </div>
</div>
'''+END_S.format(a='8.4',line='ابعتلنا <span class="gold">رقمك</span><br>في رسالة 📩'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv10_1500',D=12,preset='f',seed=1015,bpm=114,trans='3.2,8.4',pat=0),media=['sv10_1500.mp4'],idea='قصة فيديو تفاعلية: صباحك بيبدأ بإيه؟ (المحكمة / المكتب / المكالمات / القهوة)')

sflow('s10_2030','''
<div><div style="font-size:120px">🧯</div><div style="font-size:76px;font-weight:900;line-height:1.35">سيب في جدولك<br><span class="gold">نص ساعة فاضية</span></div></div>
<div class="glass" style="padding:44px 40px;margin:0 40px"><div style="font-size:50px;font-weight:800;line-height:1.6">موكل اتصل فجأة؟<br>ورقة مستعجلة؟<br>جلسة طوّلت؟</div></div>
<div style="font-size:56px;font-weight:900;line-height:1.45">النص ساعة دي<br><span class="gold">بتنقذ يومك</span> 👌</div>''',gap=56)
add(date=D,time='20:30',kind='story',media=['s10_2030.png'],idea='قصة تنظيم وقت: سيب نص ساعة فاضية في جدولك للطوارئ')

# ======================= WED 2026-11-11 =======================
D='2026-11-11'
video('v11_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">😟</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:20px">موكلك <span class="gold">قلقان</span>؟</div>
 <div class="lead" data-fx="rise" data-at=".8" style="font-size:40px;margin-top:10px">3 جمل تطمّنه… بصدق</div>
</div>
<div class="sc" data-a="3.2" data-b="6.4">
 <div class="num" data-fx="pop" data-at=".1" style="width:100px;height:100px;font-size:56px">1</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:66px;margin-top:30px">«هشرحلك اللي جاي<br><span class="gold">خطوة بخطوة</span>»</div>
</div>
<div class="sc" data-a="6.2" data-b="9.4">
 <div class="num" data-fx="pop" data-at=".1" style="width:100px;height:100px;font-size:56px">2</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:66px;margin-top:30px">«هبلّغك بأي جديد<br><span class="gold">أول ما يحصل</span>»</div>
</div>
<div class="sc" data-a="9.2" data-b="12.4">
 <div class="num" data-fx="pop" data-at=".1" style="width:100px;height:100px;font-size:56px">3</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:66px;margin-top:30px">«اكتبلي أي سؤال…<br><span class="gold">وهرد عليك</span>»</div>
</div>
'''+END_P.format(a='12.2',line='الطمأنينة بتيجي من الوضوح… مش من الوعود'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v11_1000',D=16,preset='am2',seed=1110,bpm=84,trans='3.2,6.2,9.2,12.2',pat=1),media=['v11_1000.mp4'],title='موكلك قلقان؟ | ميزان برو',
 text='موكلك قلقان؟ 😟 3 جمل تطمّنه… بصدق:\n\n1️⃣ «هشرحلك اللي جاي خطوة بخطوة»\n2️⃣ «هبلّغك بأي جديد أول ما يحصل»\n3️⃣ «اكتبلي أي سؤال… وهرد عليك»\n\nالطمأنينة بتيجي من الوضوح… مش من الوعود.\nإنت بتطمّن موكلك إزاي؟ 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن تعامل مع الموكلين: موكلك قلقان؟ 3 جمل تطمّنه بصدق')

post('p11_1400_1','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:200px"></div>
<div class="center" style="position:absolute;top:220px;left:60px;right:60px">
 <div style="display:inline-grid;place-items:center;width:200px;height:200px;border-radius:40px;background:rgba(217,178,95,.12);border:2px solid rgba(217,178,95,.5);font-size:110px">📑</div>
 <div class="h1" style="font-size:80px;margin-top:30px">ملف القضية كبر؟<br><span class="gold">اعمله فهرس</span></div>
 <div class="lead" style="margin-top:14px;font-size:32px">صفحة واحدة في أوله… توفّر عليك كتير</div>
</div>''',pill='نصيحة تنظيم 🗂️',foot='اسحب ← للخطوات',dots=(1,3))
post('p11_1400_2','''
<div class="box" style="top:180px"><div class="h2" style="font-size:52px">الفهرس فيه إيه؟ 📋</div></div>
<div class="box paper" style="top:290px;padding:30px 36px">
 <div style="display:grid;grid-template-columns:90px 1fr 220px;gap:0;font-size:30px;font-weight:800">
  <div style="padding:14px;border-bottom:2px solid #c9bfa6;color:#8a6a2c">#</div><div style="padding:14px;border-bottom:2px solid #c9bfa6;color:#8a6a2c">المستند</div><div style="padding:14px;border-bottom:2px solid #c9bfa6;color:#8a6a2c">التاريخ</div>
  <div style="padding:14px;border-bottom:1px solid #e0d8c4">1</div><div style="padding:14px;border-bottom:1px solid #e0d8c4">صحيفة الدعوى</div><div style="padding:14px;border-bottom:1px solid #e0d8c4">…/…/…</div>
  <div style="padding:14px;border-bottom:1px solid #e0d8c4">2</div><div style="padding:14px;border-bottom:1px solid #e0d8c4">صورة العقد</div><div style="padding:14px;border-bottom:1px solid #e0d8c4">…/…/…</div>
  <div style="padding:14px;border-bottom:1px solid #e0d8c4">3</div><div style="padding:14px;border-bottom:1px solid #e0d8c4">مذكرة دفاع</div><div style="padding:14px;border-bottom:1px solid #e0d8c4">…/…/…</div>
  <div style="padding:14px">4</div><div style="padding:14px">…</div><div style="padding:14px">…</div>
 </div>
</div>
<div class="box center" style="top:820px;font-size:32px;font-weight:800">رقم · اسم المستند · تاريخه… <span class="gold">وبس</span></div>''',foot='اسحب ←',dots=(2,3))
post('p11_1400_3','''
<div class="box col" style="top:190px;gap:26px">
 <div class="glass li" style="padding:30px 36px"><div class="num">✓</div><div><div class="t">حدّثه مع كل ورقة جديدة</div><div class="d">سطر واحد بياخد دقيقة</div></div></div>
 <div class="glass li" style="padding:30px 36px"><div class="num">✓</div><div><div class="t">رقّم المستندات بنفس ترتيبه</div><div class="d">علشان توصل لأي ورقة على طول</div></div></div>
 <div class="glass li" style="padding:30px 36px"><div class="num">✓</div><div><div class="t">خلّيه أول صفحة دايمًا</div><div class="d">أي حد يمسك الملف يفهمه بسرعة</div></div></div>
</div>
<div class="box center" style="top:830px"><div style="font-size:34px;font-weight:800">احفظ البوست 🔖 وجرّبها في أكبر ملف عندك</div><div class="url" style="font-size:30px;color:var(--gold2);margin-top:8px">mezan.pro</div></div>''',foot='',dots=(3,3))
add(date=D,time='14:00',kind='post',media=['p11_1400_1.png','p11_1400_2.png','p11_1400_3.png'],
 text='ملف القضية كبر؟ اعمله فهرس 📑\n\nصفحة واحدة في أول الملف فيها:\n#️⃣ رقم المستند · 📄 اسمه · 📅 تاريخه\n\nوعلشان يفضل مفيد:\n✓ حدّثه مع كل ورقة جديدة\n✓ رقّم المستندات بنفس ترتيبه\n✓ خلّيه أول صفحة دايمًا\n\nاحفظ البوست 🔖 وجرّبها في أكبر ملف عندك.\nmezan.pro'+TAGS,
 idea='كاروسيل 3 صور نصيحة تنظيم: اعمل فهرس لملف القضية الكبير')

post('p11_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:62px">مع الذكاء الاصطناعي:<br><span class="gold">قسّم الطلب الكبير</span> ✂️</div></div>
<div class="box row" style="top:400px;gap:26px">
 <div class="glass" style="flex:1;padding:30px;border-color:rgba(252,165,165,.35)">
  <div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5">بدل</div>
  <div style="font-size:40px;font-weight:900;margin-top:20px;line-height:1.5">«اكتبلي<br>المذكرة كلها»</div>
 </div>
 <div class="glass" style="flex:1.3;padding:30px;border-color:rgba(217,178,95,.6)">
  <div class="tag">جرّب</div>
  <div class="col" style="gap:12px;margin-top:20px;font-size:30px;font-weight:800">
   <div>1️⃣ رتّب الوقائع دي زمنيًا</div><div>2️⃣ لخّص النقط الأساسية</div><div>3️⃣ اقترح عناوين للأقسام</div>
  </div>
 </div>
</div>
<div class="box center" style="top:810px;font-size:31px;font-weight:800;line-height:1.6">خطوات صغيرة = مراجعة أسهل ✅<br><span class="small" style="font-size:25px">ومن غير بيانات شخصية للموكل</span></div>''',pill='ذكاء اصطناعي بأمان 🤖',foot='احفظ البوست 🔖')
add(date=D,time='19:00',kind='post',media=['p11_1900.png'],
 text='مع الذكاء الاصطناعي: قسّم الطلب الكبير ✂️\n\nبدل: «اكتبلي المذكرة كلها»\nجرّب خطوات صغيرة:\n1️⃣ رتّب الوقائع دي زمنيًا\n2️⃣ لخّص النقط الأساسية\n3️⃣ اقترح عناوين للأقسام\n\nخطوات صغيرة = مراجعة أسهل ✅\nوالكتابة والقرار النهائي ليك… ومن غير بيانات شخصية للموكل.\nmezan.pro'+TAGS,
 idea='نصيحة ذكاء اصطناعي بأمان: قسّم الطلب الكبير لخطوات صغيرة سهلة المراجعة')

sflow('s11_1100','''
<div style="font-size:64px;font-weight:900">ابدأ بـ</div>
<div style="font-size:300px;font-weight:900;line-height:1"><span class="gold" style="font-family:CairoL">14</span></div>
<div style="font-size:76px;font-weight:900">يوم <span class="gold">مجانًا</span> 🎁</div>
<div class="glass" style="padding:34px;margin:0 50px"><div style="font-size:42px;font-weight:800;color:var(--mute)">ولو كمّلت معانا</div><div style="font-size:52px;font-weight:900;margin-top:10px;line-height:1.5">شهري: 200 ج<br>سنوي: 2000 ج</div></div>''',gap=30)
add(date=D,time='11:00',kind='story',media=['s11_1100.png'],idea='قصة أسعار: رقم 14 كبير «ابدأ بـ 14 يوم مجانًا» + الشهري والسنوي')

video('sv11_1500','''
<div class="sc" data-a="0" data-b="4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🤐</div>
 <div style="font-size:80px;font-weight:900;line-height:1.4;margin-top:30px" data-fx="rise" data-at=".5">سرّ موكلك<br><span class="gold">أمانة</span></div>
</div>
<div class="sc" data-a="3.8" data-b="8.6">
 <div style="font-size:150px" data-fx="spin" data-at=".1">🔒</div>
 <div style="font-size:66px;font-weight:900;line-height:1.45;margin-top:30px" data-fx="rise" data-at=".5">وفي ميزان برو<br><span class="gold">حماية البيانات وسريتها</span><br>أولوية</div>
</div>
'''+END_S.format(a='8.4',line='اشتغل وانت<br><span class="gold">مطمّن</span> 🤍'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv11_1500',D=12,preset='cm',seed=1115,bpm=90,trans='3.8,8.4',pat=2),media=['sv11_1500.mp4'],idea='قصة فيديو ميزة: سرّ موكلك أمانة… وحماية البيانات وسريتها أولوية في ميزان برو')

sflow('s11_2030','''
<div style="font-size:76px;font-weight:900;line-height:1.35">آخر اليوم<br>على <span class="gold">مكتبك</span> 🌙</div>
<div class="row" style="gap:30px;margin:0 10px">
 <div class="glass" style="flex:1;padding:40px 20px;border-color:rgba(252,165,165,.35)"><div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5;font-size:34px">قبل</div><div style="font-size:120px;margin-top:20px">📚</div><div style="font-size:44px;font-weight:800;margin-top:10px;line-height:1.4">كوم ورق<br>مستنيك بكرة</div></div>
 <div class="glass" style="flex:1;padding:40px 20px;border-color:rgba(217,178,95,.7)"><div class="tag" style="font-size:34px">بعد</div><div style="font-size:120px;margin-top:20px">📁</div><div style="font-size:44px;font-weight:800;margin-top:10px;line-height:1.4">كل ورقة<br><span class="gold">في ملفها</span></div></div>
</div>
<div style="font-size:52px;font-weight:900">وتروّح <span class="gold">دماغك فاضية</span> 😌</div>''',gap=60)
add(date=D,time='20:30',kind='story',media=['s11_2030.png'],idea='قصة قبل/بعد: آخر اليوم على مكتبك — كوم ورق ضد كل ورقة في ملفها')

# ======================= THU 2026-11-12 =======================
D='2026-11-12'
post('p12_1000','''
<div class="box" style="top:150px"><div class="h1" style="font-size:62px">الجلسة بكرة…<br>والملف <span class="gold">تقيل ومش فاكر تفاصيله</span> 😰</div></div>
<div class="box col" style="top:420px;gap:22px">
 <div class="glass li" style="padding:26px 34px"><div class="ic">🤖</div><div><div class="t">ابدأ بملخص الأوراق</div><div class="d">الذكاء الاصطناعي يلخّصها والملخص في ملف القضية</div></div></div>
 <div class="glass li" style="padding:26px 34px"><div class="ic">🎯</div><div><div class="t">حدّد النقط المهمة</div><div class="d">اللي هتتكلم فيها بكرة</div></div></div>
 <div class="glass li" style="padding:26px 34px;border-color:rgba(217,178,95,.6)"><div class="ic">📄</div><div><div class="t">ارجع للأصل في التفاصيل</div><div class="d">التواريخ والأرقام من المستند نفسه</div></div></div>
</div>''',pill='مشكلة وحلها 💡')
add(date=D,time='10:00',kind='post',media=['p12_1000.png'],
 text='الجلسة بكرة… والملف تقيل ومش فاكر تفاصيله؟ 😰\n\n🤖 ابدأ بملخص الأوراق: في ميزان برو الذكاء الاصطناعي بيلخّص أوراق القضية والملخص بيتربط بملفها\n🎯 حدّد النقط المهمة اللي هتتكلم فيها\n📄 وارجع للأصل في التفاصيل: التواريخ والأرقام من المستند نفسه\n\nتحضير أهدى… ودماغ أصفى.\nجرّب 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='مشكلة وحلها: الجلسة بكرة والملف تقيل ← ابدأ بالملخص، حدّد النقط، ارجع للأصل')

video('v12_1400','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:140px" data-fx="spin" data-at=".1">⏳</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:80px;margin-top:20px">لو يومك فيه<br><span class="gold">ساعة زيادة</span>…</div>
</div>
<div class="sc" data-a="3.4" data-b="11.4">
 <div class="h2" data-fx="rise" data-at=".1">هتعمل بيها إيه؟ 🤔</div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:40px;width:900px">
  <div class="glass li" data-fx="pop" data-at=".5" style="padding:28px 30px"><div class="num">أ</div><div class="t" style="font-size:42px">أخلّص مذكرة ✍️</div></div>
  <div class="glass li" data-fx="pop" data-at=".9" style="padding:28px 30px"><div class="num">ب</div><div class="t" style="font-size:42px">أقرا وأتعلم 📚</div></div>
  <div class="glass li" data-fx="pop" data-at="1.3" style="padding:28px 30px"><div class="num">ج</div><div class="t" style="font-size:42px">مع العيلة 👨‍👩‍👧</div></div>
  <div class="glass li" data-fx="pop" data-at="1.7" style="padding:28px 30px"><div class="num">د</div><div class="t" style="font-size:42px">أنام بدري 😴</div></div>
 </div>
 <div class="lead" data-fx="rise" data-at="2.6" style="margin-top:40px;font-size:40px">اكتب الحرف في الكومنتات 👇</div>
</div>
'''+END_P.format(a='11.2',line='وخلّي النظام يوفّرلك وقت التدوير'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v12_1400',D=16,preset='g',seed=1214,bpm=108,trans='3.4,11.2',pat=4),media=['v12_1400.mp4'],title='لو يومك فيه ساعة زيادة | ميزان برو',
 text='لو يومك فيه ساعة زيادة… هتعمل بيها إيه؟ ⏳\n\nأ) أخلّص مذكرة ✍️\nب) أقرا وأتعلم 📚\nج) مع العيلة 👨‍👩‍👧\nد) أنام بدري 😴\n\nاكتب الحرف في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن سؤال تفاعلي: لو يومك فيه ساعة زيادة… هتعمل بيها إيه؟ (أ/ب/ج/د)')

post('p12_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:62px"><span class="gold">3 لحظات</span> تبعت فيها<br>تحديث لموكلك 📲</div></div>
<div class="box" style="top:410px;display:flex;gap:22px">
 <div class="glass center" style="flex:1;padding:34px 18px"><div class="num" style="margin:0 auto">1</div><div style="font-size:70px;margin-top:14px">⚖️</div><div style="font-size:32px;font-weight:900;margin-top:8px;line-height:1.4">بعد<br>كل جلسة</div></div>
 <div class="glass center" style="flex:1;padding:34px 18px"><div class="num" style="margin:0 auto">2</div><div style="font-size:70px;margin-top:14px">📄</div><div style="font-size:32px;font-weight:900;margin-top:8px;line-height:1.4">لما توصل<br>ورقة مهمة</div></div>
 <div class="glass center" style="flex:1;padding:34px 18px"><div class="num" style="margin:0 auto">3</div><div style="font-size:70px;margin-top:14px">⏰</div><div style="font-size:32px;font-weight:900;margin-top:8px;line-height:1.4">لما حاجة<br>تتأخر</div></div>
</div>
<div class="box center" style="top:810px;font-size:33px;font-weight:800">رسالة قصيرة منك… <span class="gold">أحسن من 10 مكالمات منه</span> 😉</div>''',pill='مع الموكلين 🤝',foot='احفظ البوست 🔖')
add(date=D,time='19:00',kind='post',media=['p12_1900.png'],
 text='3 لحظات تبعت فيها تحديث لموكلك 📲\n\n1️⃣ بعد كل جلسة ⚖️\n2️⃣ لما توصل ورقة مهمة 📄\n3️⃣ لما حاجة تتأخر ⏰ (خصوصًا دي!)\n\nرسالة قصيرة منك… أحسن من 10 مكالمات منه 😉\nاحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='نصيحة تواصل: 3 لحظات تبعت فيها تحديث لموكلك (بعد الجلسة · ورقة مهمة · تأخير)')

sflow('s12_1100','''
<div><div style="font-size:120px">🤖</div><div style="font-size:70px;font-weight:900;line-height:1.35">بتستخدم الذكاء الاصطناعي<br>في صياغة رسالة؟</div></div>
<div class="paper" style="padding:46px 40px;margin:0 30px;font-size:56px;font-weight:900;line-height:1.5">«اكتبلي<br><span style="color:#8a6a2c">تلات صيغ مختلفة</span>»</div>
<div style="font-size:54px;font-weight:900;line-height:1.5">وإنت <span class="gold">تختار وتعدّل</span><br>بأسلوبك ✍️</div>''',gap=60)
add(date=D,time='11:00',kind='story',media=['s12_1100.png'],idea='قصة ذكاء اصطناعي: اطلب 3 صيغ مختلفة… وإنت تختار وتعدّل بأسلوبك')

video('sv12_1500','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">📝</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">ملاحظاتك<br>عن القضية <span class="gold">فين؟</span></div>
</div>
<div class="sc" data-a="3.2" data-b="6.4">
 <div class="tag" data-fx="rise" data-at=".1" style="background:rgba(252,165,165,.15);color:#fca5a5;font-size:40px">قبل 😓</div>
 <div style="font-size:70px;font-weight:900;line-height:1.6;margin-top:40px" data-fx="rise" data-at=".4">ورقة في الشنطة<br>ونوتة على الموبايل<br>وجزء <span style="color:#fca5a5">في دماغك</span></div>
</div>
<div class="sc" data-a="6.2" data-b="8.6">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:40px">بعد 😌</div>
 <div style="font-size:150px;margin-top:30px" data-fx="pop" data-at=".3">📁</div>
 <div style="font-size:72px;font-weight:900;line-height:1.5" data-fx="rise" data-at=".6">كلها في<br><span class="gold">ملف القضية</span></div>
</div>
'''+END_S.format(a='8.4',line='مكان واحد<br><span class="gold">لكل قضية</span> ⚖️'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv12_1500',D=12,preset='c',seed=1215,bpm=100,trans='3.2,6.2,8.4',pat=3),media=['sv12_1500.mp4'],idea='قصة فيديو قبل/بعد: ملاحظاتك متوزعة (شنطة · موبايل · دماغك) ضد كلها في ملف القضية')

sflow('s12_2030','''
<div><div class="pill" style="font-size:34px;display:inline-block">أسئلة شائعة ❓</div><div style="font-size:70px;font-weight:900;line-height:1.35;margin-top:30px">الذكاء الاصطناعي<br>بيعمل إيه <span class="gold">في ميزان برو؟</span></div></div>
<div class="col" style="margin:0 30px;gap:26px">
 <div class="glass li" style="padding:30px 40px;gap:30px"><div class="ic" style="width:110px;height:110px;font-size:60px">📄</div><div style="font-size:50px;font-weight:900;text-align:right">بيلخّص أوراق ومستندات القضية</div></div>
 <div class="glass li" style="padding:30px 40px;gap:30px"><div class="ic" style="width:110px;height:110px;font-size:60px">🔗</div><div style="font-size:50px;font-weight:900;text-align:right">ويربط الملخص بملف القضية</div></div>
</div>
<div style="font-size:48px;font-weight:800;color:#c9d4ea">والقرار دايمًا <span class="gold">ليك</span> ⚖️</div>''',gap=60)
add(date=D,time='20:30',kind='story',media=['s12_2030.png'],idea='قصة أسئلة شائعة: الذكاء الاصطناعي بيعمل إيه في ميزان برو؟ يلخّص ويربط الملخص بالملف')

# ======================= FRI 2026-11-13 =======================
D='2026-11-13'
video('v13_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:30px">الأسعار 🏷️</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:30px">بـ <span class="gold" style="font-family:CairoL">200</span> ج في الشهر…<br>إيه اللي في إيدك؟</div>
</div>
<div class="sc" data-a="3.2" data-b="9.6">
 <div class="col" style="gap:24px;width:860px">
  <div class="glass li" data-fx="right" data-at=".3" style="padding:26px 34px"><div class="ic">🗂️</div><div class="t" style="font-size:42px">نظام إدارة متكامل لمكتبك</div></div>
  <div class="glass li" data-fx="right" data-at="1" style="padding:26px 34px"><div class="ic">🤖</div><div class="t" style="font-size:42px">تلخيص أوراق القضايا بالذكاء الاصطناعي</div></div>
  <div class="glass li" data-fx="right" data-at="1.7" style="padding:26px 34px"><div class="ic">🔒</div><div class="t" style="font-size:42px">حماية بياناتك وسريتها أولوية</div></div>
 </div>
</div>
<div class="sc" data-a="9.4" data-b="12.4">
 <div class="lead" data-fx="rise" data-at=".1" style="font-size:44px">أو السنوي</div>
 <div style="font-size:150px;font-weight:900;line-height:1.2" data-fx="stamp" data-at=".3"><span class="gold" style="font-family:CairoL">2000</span> ج</div>
 <div class="btn" data-fx="pop" data-at="1" style="margin-top:30px">وابدأ بـ 14 يوم مجانًا 🎁</div>
</div>
'''+END_P.format(a='12.2',line='جرّب الأول… وقرّر بنفسك'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v13_1000',D=16,preset='em',seed=1310,bpm=100,trans='3.2,9.4,12.2',pat=0),media=['v13_1000.mp4'],title='بـ 200 ج في الشهر | ميزان برو',
 text='بـ 200 ج في الشهر… إيه اللي في إيدك؟ 🏷️\n\n🗂️ نظام إدارة متكامل لمكتبك\n🤖 تلخيص أوراق ومستندات القضايا بالذكاء الاصطناعي، مربوط بملف كل قضية\n🔒 حماية بياناتك وسريتها أولوية\n\nأو الاشتراك السنوي بـ 2000 ج.\nوابدأ بـ 14 يوم مجانًا 🎁 جرّب الأول… وقرّر بنفسك.\n👈 mezan.pro'+TAGS,
 idea='فيديو موشن أسعار: بـ 200 ج في الشهر إيه اللي في إيدك؟ + السنوي 2000 ج + 14 يوم مجانًا')

post('p13_1400','''
<div class="glowc" style="width:900px;height:900px;left:90px;top:120px"></div>
<div class="center" style="position:absolute;top:190px;left:70px;right:70px">
 <div style="font-size:130px">🌿</div>
 <div style="font-size:74px;font-weight:900;line-height:1.45;margin-top:20px">الراحة<br><span class="gold">مش وقت ضايع</span></div>
 <div class="line" style="width:260px;margin:34px auto"></div>
 <div style="font-size:52px;font-weight:800;line-height:1.5;color:#c9d4ea">دي جزء من <span class="gold">التحضير</span><br>للأسبوع الجاي</div>
</div>''',pill='جمعة سعيدة 🤍',foot='شاركها مع زميل محتاجها')
add(date=D,time='14:00',kind='post',media=['p13_1400.png'],
 text='«الراحة مش وقت ضايع… دي جزء من التحضير للأسبوع الجاي» 🌿\n\nجمعة سعيدة يا متر 🤍\nاقفل الموبايل شوية، واشحن طاقتك.\nشاركها مع زميل محتاجها 👇\nmezan.pro'+TAGS,
 idea='جملة تحفيزية للجمعة: «الراحة مش وقت ضايع… دي جزء من التحضير»')

post('p13_1900','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:62px">ميزان برو <span class="gold">في معادلة</span> 🧮</div></div>
<div class="box" style="top:330px;display:flex;align-items:center;justify-content:center;gap:14px">
 <div class="glass center" style="width:260px;padding:30px 10px"><div style="font-size:70px">🗂️</div><div style="font-size:28px;font-weight:900;margin-top:6px;line-height:1.4">نظام إدارة<br>متكامل</div></div>
 <div class="gold" style="font-size:70px;font-weight:900">+</div>
 <div class="glass center" style="width:260px;padding:30px 10px"><div style="font-size:70px">🤖</div><div style="font-size:28px;font-weight:900;margin-top:6px;line-height:1.4;white-space:nowrap">تلخيص<br>بالذكاء الاصطناعي</div></div>
 <div class="gold" style="font-size:70px;font-weight:900">+</div>
 <div class="glass center" style="width:260px;padding:30px 10px"><div style="font-size:70px">🔒</div><div style="font-size:28px;font-weight:900;margin-top:6px;line-height:1.4">سرية<br>البيانات</div></div>
</div>
<div class="box center" style="top:690px"><div class="gold" style="font-size:80px;font-weight:900;line-height:1">=</div>
 <div style="display:inline-flex;align-items:center;gap:20px;margin-top:16px" class="glass"><div style="padding:24px 40px;display:flex;align-items:center;gap:20px"><img src="../logo.svg" width="70"><span class="gold" style="font-family:Messiri;font-size:60px">مكتب مرتّب</span></div></div>
</div>''',pill='ميزة ✨')
add(date=D,time='19:00',kind='post',media=['p13_1900.png'],
 text='ميزان برو في معادلة 🧮\n\n🗂️ نظام إدارة متكامل\n➕ 🤖 تلخيص أوراق القضايا بالذكاء الاصطناعي مربوط بملف القضية\n➕ 🔒 حماية البيانات وسريتها أولوية\n🟰 مكتب مرتّب\n\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='ميزة في معادلة: نظام إدارة + تلخيص بالذكاء الاصطناعي + سرية = مكتب مرتّب')

sflow('s13_1100','''
<div><div style="font-size:120px">🌤️</div><div style="font-size:80px;font-weight:900;line-height:1.35">الجمعة عندك<br><span class="gold">عاملة إزاي؟</span></div></div>
<div class="col" style="margin:0 40px;gap:26px">
 <div class="glass li" style="padding:28px 44px;gap:30px"><div style="font-size:80px">😴</div><div style="font-size:58px;font-weight:900">راحة تامة</div></div>
 <div class="glass li" style="padding:28px 44px;gap:30px"><div style="font-size:80px">📂</div><div style="font-size:58px;font-weight:900">تحضير للأسبوع</div></div>
 <div class="glass li" style="padding:28px 44px;gap:30px"><div style="font-size:80px">😅</div><div style="font-size:58px;font-weight:900">شوية من ده وده</div></div>
</div>
<div style="font-size:48px;font-weight:800;color:#c9d4ea">ابعتلنا إجابتك 📩</div>''',gap=56)
add(date=D,time='11:00',kind='story',media=['s13_1100.png'],idea='قصة سؤال: الجمعة عندك عاملة إزاي؟ راحة / تحضير / شوية من ده وده')

def tf(q,a,ok):
    c='#86efac' if ok else '#fca5a5'
    return f'''<div class="sc" data-a="{{a}}" data-b="{{b}}">
 <div style="font-size:44px;font-weight:800;color:var(--mute)" data-fx="rise" data-at=".1">صح ولا غلط؟ 🤔</div>
 <div style="font-size:70px;font-weight:900;line-height:1.45;margin-top:30px" data-fx="rise" data-at=".3">{q}</div>
 <div data-fx="stamp" data-at="1.4" style="margin-top:50px;font-size:90px;font-weight:900;color:{c}">{"صح ✓" if ok else "غلط ✗"}</div>
 <div style="font-size:50px;font-weight:800;line-height:1.5;margin-top:20px" data-fx="rise" data-at="1.9">{a}</div>
</div>'''
sc=(tf('ميزان برو<br>للمكاتب الكبيرة بس؟','للمحامين<br><span class="gold">ومكاتب المحاماة</span>',False).replace('{a}','0').replace('{b}','4.2')+
    tf('الذكاء الاصطناعي<br>بيلخّص أوراق القضية؟','والملخص <span class="gold">بيتربط<br>بملف القضية</span>',True).replace('{a}','4').replace('{b}','8.6'))
video('sv13_1500',sc+END_S.format(a='8.4',line='جرّبه بنفسك<br><span class="gold">14 يوم مجانًا</span> 🎁'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv13_1500',D=12,preset='fm',seed=1315,bpm=106,trans='4,8.4',pat=4),media=['sv13_1500.mp4'],idea='قصة فيديو أسئلة شائعة «صح ولا غلط؟»: للمكاتب الكبيرة بس؟ غلط · بيلخّص الأوراق؟ صح')

sflow('s13_2030','''
<div><div style="font-size:120px">📌</div><div style="font-size:74px;font-weight:900;line-height:1.35">اقفل أسبوعك<br>بـ <span class="gold">سطرين</span> في كل ملف</div></div>
<div class="paper" style="padding:44px 40px;margin:0 30px;text-align:right">
 <div style="font-size:50px;font-weight:900;line-height:1.8">✔️ آخر حاجة اتعملت</div>
 <div style="font-size:50px;font-weight:900;line-height:1.8">➡️ الخطوة الجاية</div>
</div>
<div style="font-size:52px;font-weight:900;line-height:1.5">والسبت تكمّل<br><span class="gold">من غير ما تفتكر</span> 😌</div>''',gap=60)
add(date=D,time='20:30',kind='story',media=['s13_2030.png'],idea='قصة تنظيم: اقفل أسبوعك بسطرين في كل ملف (آخر حاجة اتعملت · الخطوة الجاية)')

json.dump(M,open('mw3b.json','w'),ensure_ascii=False,indent=1);print('ok',len(M))
