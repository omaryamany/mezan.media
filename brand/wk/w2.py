from lib import *
import json
M=[]
TAGS='\n\n#ميزان_برو #محاماة'
def add(**k): M.append(k)
OUT='''<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".1">
 <div class="gold" style="font-family:Messiri;font-size:90px;margin-top:16px" data-fx="rise" data-at=".4">ميزان برو</div>
 <div class="lead" data-fx="rise" data-at=".7" style="font-size:38px">{sub}</div>
 <div class="url" data-fx="pulse" data-at="1.1" style="margin-top:30px;font-size:56px;color:var(--gold2)">mezan.pro</div>
</div>'''

# ======================= WED 2026-11-04 =======================
D='2026-11-04'
video('v04_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:84px">مستندات القضية<br><span class="gold">فين بالظبط؟</span> 🤔</div>
</div>
<div class="sc" data-a="3.2" data-b="7.4">
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;width:100%">
  <div class="glass center" data-fx="pop" data-at=".1" style="padding:36px"><div style="font-size:100px">📧</div><div style="font-size:44px;font-weight:900">في الإيميل</div></div>
  <div class="glass center" data-fx="pop" data-at=".5" style="padding:36px"><div style="font-size:100px">💬</div><div style="font-size:44px;font-weight:900">على الواتساب</div></div>
  <div class="glass center" data-fx="pop" data-at=".9" style="padding:36px"><div style="font-size:100px">💾</div><div style="font-size:44px;font-weight:900">على فلاشة</div></div>
  <div class="glass center" data-fx="pop" data-at="1.3" style="padding:36px"><div style="font-size:100px">🗄️</div><div style="font-size:44px;font-weight:900">في الدُرج</div></div>
 </div>
</div>
<div class="sc" data-a="7.2" data-b="10.4">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:76px">4 أماكن… 😓<br><span class="gold">ولا مكان</span> فيهم كامل</div>
</div>
<div class="sc" data-a="10.2" data-b="13.4">
 <div class="h1" data-fx="stamp" data-at=".1" style="font-size:88px">خلّيهم في<br><span class="gold">نظام واحد</span> 🗂️</div>
 <div class="lead" data-fx="rise" data-at=".8" style="font-size:40px;margin-top:30px">ميزان برو… نظام إدارة متكامل لمكتبك<br>وكل قضية ليها ملفها</div>
</div>
'''+OUT.format(sub='جرّبه 14 يوم مجانًا'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v04_1000',D=16,preset='fm',seed=410,bpm=90,trans='3.2,7.2,10.2,13.2',pat=4),media=['v04_1000.mp4'],title='مستندات القضية فين؟ | ميزان برو',
 text='مستندات القضية فين بالظبط؟ 🤔\n📧 في الإيميل\n💬 على الواتساب\n💾 على فلاشة\n🗄️ في الدُرج\n\n4 أماكن… ولا مكان فيهم كامل 😓\nخلّيهم في نظام واحد 🗂️\nميزان برو: نظام إدارة متكامل لمكتبك، وكل قضية ليها ملفها.\n\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='فيديو موشن مشكلة وحلها: مستندات متوزعة في 4 أماكن ← نظام واحد لمكتبك')

post('p04_1200','''
<div class="box" style="top:160px"><div class="h1" style="font-size:62px">قول لموكلك <span class="gold">إمتى بترد</span>…<br>ووفّر عليه القلق 📲</div></div>
<div class="box" style="top:430px;display:flex;justify-content:flex-start">
 <div style="max-width:820px;background:linear-gradient(160deg,var(--gold2),var(--gold));color:var(--navy);padding:34px 44px;border-radius:36px 36px 36px 10px;font-size:36px;font-weight:800;line-height:1.6">"أهلًا يا أستاذ… أنا بتابع الرسايل يوميًا<br>من الساعة 4 لـ 6 ✅<br>وأي جديد في قضيتك هبلّغك بيه على طول."</div>
</div>
<div class="box center" style="top:790px"><div class="tag" style="font-size:26px">مثال — غيّر المواعيد حسب جدولك</div>
<div style="font-size:32px;font-weight:800;margin-top:22px">لما الموكل يعرف إمتى… <span class="gold">مش هيقلق لو اتأخرت</span></div></div>''',pill='مع الموكلين 🤝',foot='ابعتها لموكلينك')
add(date=D,time='12:00',kind='post',media=['p04_1200.png'],
 text='قول لموكلك إمتى بترد… ووفّر عليه القلق 📲\n\nرسالة بسيطة زي دي:\n"أهلًا يا أستاذ… أنا بتابع الرسايل يوميًا من الساعة 4 لـ 6 ✅ وأي جديد في قضيتك هبلّغك بيه على طول."\n(غيّر المواعيد حسب جدولك)\n\nلما الموكل يعرف إمتى… مش هيقلق لو اتأخرت.\nmezan.pro'+TAGS,
 idea='نصيحة تواصل: حدّد لموكلك مواعيد ثابتة للرد (رسالة جاهزة)')

post('p04_1800','''
<div class="box center" style="top:160px"><div class="h1" style="font-size:66px">ميزان برو <span class="gold">بالأرقام</span> 🔢</div></div>
<div class="box row" style="top:330px;gap:24px">
 <div class="glass center" style="flex:1;padding:40px 10px;border-color:rgba(217,178,95,.7)"><div class="gold" style="font-family:CairoL;font-size:130px;font-weight:900;line-height:1.1">14</div><div style="font-size:36px;font-weight:900">يوم</div><div class="lead" style="font-size:28px;margin-top:8px">تجربة مجانية</div></div>
 <div class="glass center" style="flex:1;padding:40px 10px"><div class="gold" style="font-family:CairoL;font-size:130px;font-weight:900;line-height:1.1">200</div><div style="font-size:36px;font-weight:900">جنيه</div><div class="lead" style="font-size:28px;margin-top:8px">في الشهر</div></div>
 <div class="glass center" style="flex:1;padding:40px 10px"><div class="gold" style="font-family:CairoL;font-size:116px;font-weight:900;line-height:1.2">2000</div><div style="font-size:36px;font-weight:900">جنيه</div><div class="lead" style="font-size:28px;margin-top:8px">في السنة</div></div>
</div>
<div class="box center" style="top:780px"><div class="btn">ابدأ تجربتك من mezan.pro</div></div>''',pill='الأسعار 💳')
add(date=D,time='18:00',kind='post',media=['p04_1800.png'],
 text='ميزان برو بالأرقام 🔢\n\n14 يوم تجربة مجانية 🎁\n200 ج في الشهر\n2000 ج في السنة\n\nنظام إدارة متكامل لمكتبك، بيلخّص أوراق القضايا بالذكاء الاصطناعي، وسرية بياناتك أولوية 🔒\nابدأ تجربتك 👈 mezan.pro'+TAGS,
 idea='تذكير بالأسعار بالأرقام الكبيرة: 14 يوم · 200 ج · 2000 ج')

sflow('s04_1100','''
<div class="gold" style="font-family:Messiri;font-size:300px;line-height:1;height:190px;overflow:visible">“</div>
<div style="font-size:96px;font-weight:900;line-height:1.4">كل ميعاد<br>بتحترمه…<br><span class="gold">بيبني اسمك</span></div>
<div class="line" style="width:320px;margin:0 auto"></div>''',gap=60)
add(date=D,time='11:00',kind='story',media=['s04_1100.png'],idea='قصة اقتباس: «كل ميعاد بتحترمه… بيبني اسمك»')

video('sv04_1500','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:84px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">إيه <span class="gold">أصعب حاجة</span><br>في يومك يا متر؟</div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:26px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">1</div><div class="t" style="font-size:52px">الزحمة والمواصلات 🚗</div></div>
  <div class="glass li" data-fx="right" data-at=".7" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">2</div><div class="t" style="font-size:52px">الانتظار في المحكمة ⏳</div></div>
  <div class="glass li" data-fx="right" data-at="1.2" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">3</div><div class="t" style="font-size:52px">كوم الورق 📚</div></div>
  <div class="glass li" data-fx="right" data-at="1.7" style="padding:30px 40px"><div class="num" style="width:84px;height:84px;font-size:46px">4</div><div class="t" style="font-size:52px">متابعة الموكلين 📲</div></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:78px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">ابعتلنا <span class="gold">رقمك</span> 📩</div>
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv04_1500',D=12,preset='dm',seed=415,bpm=116,trans='3.2,8.4',pat=2),media=['sv04_1500.mp4'],idea='قصة فيديو تفاعلية: إيه أصعب حاجة في يومك؟ (زحمة / انتظار / ورق / موكلين)')

sflow('s04_2030','''
<div><div style="font-size:120px">🖥️</div><div style="font-size:78px;font-weight:900;line-height:1.35">سطح المكتب<br><span class="gold">مليان ملفات؟</span></div></div>
<div class="glass" style="padding:50px 40px;margin:0 30px;border-color:rgba(217,178,95,.6)">
 <div style="font-size:60px;font-weight:900;line-height:1.5"><span class="gold">10 دقايق</span><br>مرة في الأسبوع</div>
 <div style="font-size:46px;font-weight:700;color:#c9d4ea;margin-top:16px">كل ملف يروح لمكانه 📁</div>
</div>''',gap=70)
add(date=D,time='20:30',kind='story',media=['s04_2030.png'],idea='قصة تنظيم: سطح المكتب مليان؟ 10 دقايق مرة في الأسبوع وكل ملف لمكانه')

# ======================= THU 2026-11-05 =======================
D='2026-11-05'
post('p05_1000','''
<div class="box center" style="top:160px"><div class="h1" style="font-size:60px">لو هتختار حاجة واحدة<br><span class="gold">تريّحك في المكتب</span>… 🤔</div></div>
<div class="box col" style="top:420px;gap:20px">
 <div class="glass li" style="padding:22px 32px"><div class="num" style="width:66px;height:66px;font-size:36px">أ</div><div class="t" style="font-size:38px">ورق أقل على المكتب 📄</div></div>
 <div class="glass li" style="padding:22px 32px"><div class="num" style="width:66px;height:66px;font-size:36px">ب</div><div class="t" style="font-size:38px">ملخصات جاهزة للقضايا 📝</div></div>
 <div class="glass li" style="padding:22px 32px"><div class="num" style="width:66px;height:66px;font-size:36px">ج</div><div class="t" style="font-size:38px">وقت أكتر للموكلين 🤝</div></div>
 <div class="glass li" style="padding:22px 32px"><div class="num" style="width:66px;height:66px;font-size:36px">د</div><div class="t" style="font-size:38px">كل ده مع بعض 😄</div></div>
</div>''',pill='سؤال للمحامين 💬',foot='اكتب الحرف في الكومنتات 👇')
add(date=D,time='10:00',kind='post',media=['p05_1000.png'],
 text='لو هتختار حاجة واحدة تريّحك في المكتب… تختار إيه؟ 🤔\n\nأ) ورق أقل على المكتب 📄\nب) ملخصات جاهزة للقضايا 📝\nج) وقت أكتر للموكلين 🤝\nد) كل ده مع بعض 😄\n\nاكتب الحرف في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='سؤال تفاعلي: لو هتختار حاجة واحدة تريّحك في المكتب؟ (أ/ب/ج/د)')

video('v05_1200','''
<div class="sc" data-a="0" data-b="3">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:30px">قبل / بعد 🔄</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:96px;margin-top:30px">أول ساعة<br>في <span class="gold">يومك</span> ☀️</div>
</div>
<div class="sc" data-a="2.8" data-b="7.6">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:40px;background:rgba(252,165,165,.15);color:#fca5a5">قبل: بالورق</div>
 <div class="col" style="width:100%;gap:24px;margin-top:36px">
  <div class="glass li" data-fx="left" data-at=".4" style="padding:26px 36px"><div class="ic">🗂️</div><div class="t" style="font-size:44px">تقلّب في الدوسيهات</div></div>
  <div class="glass li" data-fx="left" data-at="1" style="padding:26px 36px"><div class="ic">❓</div><div class="t" style="font-size:44px">"هو أنا وقفت فين؟"</div></div>
  <div class="glass li" data-fx="left" data-at="1.6" style="padding:26px 36px"><div class="ic">⏰</div><div class="t" style="font-size:44px">والساعة تعدّي…</div></div>
 </div>
</div>
<div class="sc" data-a="7.4" data-b="12.2">
 <div class="tag" data-fx="rise" data-at=".1" style="font-size:40px">بعد: مع ميزان برو</div>
 <div class="col" style="width:100%;gap:24px;margin-top:36px">
  <div class="glass li" data-fx="right" data-at=".4" style="padding:26px 36px;border-color:rgba(217,178,95,.6)"><div class="ic">🗂️</div><div class="t" style="font-size:44px">مكتبك كله في نظام واحد</div></div>
  <div class="glass li" data-fx="right" data-at="1" style="padding:26px 36px;border-color:rgba(217,178,95,.6)"><div class="ic">📝</div><div class="t" style="font-size:44px">ملخص كل قضية في ملفها</div></div>
  <div class="glass li" data-fx="right" data-at="1.6" style="padding:26px 36px;border-color:rgba(217,178,95,.6)"><div class="ic">🚀</div><div class="t" style="font-size:44px">وتبدأ شغل على طول</div></div>
 </div>
</div>
<div class="sc" data-a="12" data-b="13.4">
 <div class="h1" data-fx="stamp" data-at=".1" style="font-size:90px">الفرق <span class="gold">واضح</span> ✨</div>
</div>
'''+OUT.format(sub='جرّبه 14 يوم مجانًا'),D=16)
add(date=D,time='12:00',kind='post',video=dict(src='v05_1200',D=16,preset='g',seed=512,bpm=102,trans='2.8,7.4,12,13.2',pat=1),media=['v05_1200.mp4'],title='أول ساعة في يومك | ميزان برو',
 text='أول ساعة في يومك ☀️\n\nقبل (بالورق): 🗂️ تقلّب في الدوسيهات… ❓ "هو أنا وقفت فين؟"… ⏰ والساعة تعدّي.\nبعد (مع ميزان برو): 🗂️ مكتبك كله في نظام واحد · 📝 ملخص كل قضية في ملفها · 🚀 وتبدأ شغل على طول.\n\nالفرق واضح ✨\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='فيديو موشن قبل/بعد: أول ساعة في يومك بالورق ضد مع ميزان برو')

post('p05_1800','''
<div class="box" style="top:160px"><div class="h1" style="font-size:60px">خلّي الذكاء الاصطناعي<br>يعملّك <span class="gold">تشيك ليست</span> ✅</div></div>
<div class="box row" style="top:410px;gap:26px;align-items:stretch">
 <div class="paper" style="flex:1.3;padding:30px 34px">
  <div style="font-size:26px;font-weight:900;color:#8a6a2c">💬 اطلب منه مثلًا:</div>
  <div style="font-size:31px;font-weight:800;line-height:1.6;margin-top:10px">"اعملّي قايمة بالمستندات اللي غالبًا هحتاجها في قضية<br>من النوع ده"</div>
 </div>
 <div class="col" style="flex:1;gap:16px">
  <div class="glass li" style="padding:20px 24px"><div class="ic" style="width:60px;height:60px;font-size:32px">🚫</div><div class="t" style="font-size:28px">من غير بيانات الموكل</div></div>
  <div class="glass li" style="padding:20px 24px"><div class="ic" style="width:60px;height:60px;font-size:32px">🧠</div><div class="t" style="font-size:28px">راجعها بخبرتك</div></div>
  <div class="glass li" style="padding:20px 24px"><div class="ic" style="width:60px;height:60px;font-size:32px">✏️</div><div class="t" style="font-size:28px">زوّد وشيل براحتك</div></div>
 </div>
</div>
<div class="box center" style="top:860px;font-size:32px;font-weight:800">هو بيجهّز المسودة… <span class="gold">وإنت صاحب القرار</span></div>''',pill='ذكاء اصطناعي بأمان 🤖',foot='احفظ الفكرة 🔖')
add(date=D,time='18:00',kind='post',media=['p05_1800.png'],
 text='خلّي الذكاء الاصطناعي يعملّك تشيك ليست ✅\n\nاطلب منه مثلًا: "اعملّي قايمة بالمستندات اللي غالبًا هحتاجها في قضية من النوع ده"\n\n🚫 من غير أي بيانات للموكل\n🧠 راجعها بخبرتك\n✏️ زوّد وشيل براحتك\n\nهو بيجهّز المسودة… وإنت صاحب القرار.\nmezan.pro'+TAGS,
 idea='نصيحة ذكاء اصطناعي بأمان: اطلب منه تشيك ليست مستندات لنوع القضية وراجعها بخبرتك')

video('sv05_1100','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🗓️</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:20px" data-fx="rise" data-at=".4">النهارده <span class="gold">الخميس</span><br>قفّل أسبوعك نضيف</div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:28px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">✅</div><div class="t" style="font-size:52px">خلّص المهام الصغيرة</div></div>
  <div class="glass li" data-fx="right" data-at="1" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">📁</div><div class="t" style="font-size:52px">كل ورقة في ملفها</div></div>
  <div class="glass li" data-fx="right" data-at="1.8" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">📝</div><div class="t" style="font-size:52px">اكتب أول مهمة للسبت</div></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:76px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".1">وادخل الويكند<br><span class="gold">دماغك فاضية</span> 🤍</div>
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv05_1100',D=12,preset='c',seed=511,bpm=92,trans='3.2,8.4',pat=3),media=['sv05_1100.mp4'],idea='قصة فيديو تنظيم: الخميس — قفّل أسبوعك نضيف في 3 خطوات')

sflow('s05_1500','''
<div style="font-size:76px;font-weight:900;line-height:1.35">لسه <span class="gold">بتفكر</span>؟ 🤔</div>
<div class="glass" style="padding:50px 30px;margin:0 60px;border-color:rgba(217,178,95,.7)">
 <div class="gold" style="font-family:CairoL;font-size:260px;font-weight:900;line-height:1">14</div>
 <div style="font-size:64px;font-weight:900">يوم مجانًا 🎁</div>
</div>
<div style="font-size:56px;font-weight:900;line-height:1.5">جرّب ميزان برو<br><span class="gold">وقرّر بعدها</span></div>''',gap=60)
add(date=D,time='15:00',kind='story',media=['s05_1500.png'],idea='قصة تجربة مجانية: لسه بتفكر؟ 14 يوم مجانًا وقرّر بعدها')

sflow('s05_2030','''
<div><div class="pill" style="font-size:34px;display:inline-block">أسئلة شائعة ❓</div><div style="font-size:78px;font-weight:900;line-height:1.35;margin-top:30px">"بيانات موكليني<br><span class="gold">في أمان؟</span>"</div></div>
<div style="font-size:200px;line-height:1">🔒</div>
<div class="glass" style="padding:44px 40px;margin:0 20px;border-color:rgba(217,178,95,.6)"><div style="font-size:54px;font-weight:900;line-height:1.5">حماية البيانات وسريتها<br><span class="gold">أولوية</span> في ميزان برو</div></div>''',gap=60)
add(date=D,time='20:30',kind='story',media=['s05_2030.png'],idea='قصة أسئلة شائعة: «بيانات موكليني في أمان؟» حماية البيانات وسريتها أولوية')

# ======================= FRI 2026-11-06 =======================
D='2026-11-06'
post('p06_1000_1','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:200px"></div>
<div class="center" style="position:absolute;top:220px;left:60px;right:60px">
 <div style="display:inline-grid;place-items:center;width:190px;height:190px;border-radius:40px;background:rgba(217,178,95,.12);border:2px solid rgba(217,178,95,.5);font-size:100px">⌛</div>
 <div class="h1" style="font-size:74px;margin-top:30px">3 عادات صغيرة<br><span class="gold">بتسرق وقتك</span></div>
 <div class="lead" style="margin-top:14px;font-size:34px">وإزاي تبطّلها</div>
</div>''',pill='نصيحة تنظيم 🗓️',foot='اسحب ←',dots=(1,3))
def hab(n,bad,good,top):
    return f'''<div class="glass" style="padding:40px 40px"><div class="row" style="align-items:center"><div class="num" style="width:70px;height:70px;font-size:38px">{n}</div><div style="font-size:42px;font-weight:900"><span class="no">❌</span> {bad}</div></div>
 <div style="font-size:38px;font-weight:800;margin-top:20px;margin-right:92px"><span class="ok">✅</span> <span class="gold">{good}</span></div></div>'''
post('p06_1000_2','<div class="box col" style="top:210px;gap:44px">'+hab(1,'"هحفظ الورقة دي بعدين"','احفظها في ملف قضيتها فورًا',0)+hab(2,'تدوّر في رسايل قديمة','كل مستند مهم له مكان ثابت',0)+'</div>',foot='اسحب ←',dots=(2,3))
post('p06_1000_3','<div class="box col" style="top:200px;gap:40px">'+hab(3,'تبدأ يومك من غير خطة','حدّد أهم 3 مهام قبل ما تبدأ',0)+'''</div>
<div class="box center" style="top:640px"><div style="font-size:40px;font-weight:900">وقت أقل في التدوير… <span class="gold">ووقت أكتر للقضايا</span></div>
<div class="small" style="font-size:28px;margin-top:16px">احفظ البوست 🔖 · <span class="url">mezan.pro</span></div></div>''',foot='',dots=(3,3))
add(date=D,time='10:00',kind='post',media=['p06_1000_1.png','p06_1000_2.png','p06_1000_3.png'],
 text='3 عادات صغيرة بتسرق وقتك ⌛ وإزاي تبطّلها:\n\n1️⃣ ❌ "هحفظ الورقة دي بعدين" ← ✅ احفظها في ملف قضيتها فورًا\n2️⃣ ❌ تدوّر في رسايل قديمة ← ✅ كل مستند مهم له مكان ثابت\n3️⃣ ❌ تبدأ يومك من غير خطة ← ✅ حدّد أهم 3 مهام قبل ما تبدأ\n\nوقت أقل في التدوير… ووقت أكتر للقضايا.\nاحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='كاروسيل 3 صور: 3 عادات صغيرة بتسرق وقتك وإزاي تبطّلها')

post('p06_1200','''
<div class="glowc" style="width:900px;height:900px;left:90px;top:120px"></div>
<div class="box center" style="top:200px">
 <div style="font-size:110px">⚖️</div>
 <div class="h1" style="font-size:64px;line-height:1.55;margin-top:10px">المحاماة مش بس<br>كسب قضايا…<br><span class="gold">دي ثقة بتتبني</span><br><span class="gold">كل يوم</span></div>
 <div class="line" style="width:300px;margin:36px auto 0"></div>
</div>''',pill='جمعة سعيدة 🤍',foot='شاركها مع زميل')
add(date=D,time='12:00',kind='post',media=['p06_1200.png'],
 text='«المحاماة مش بس كسب قضايا… دي ثقة بتتبني كل يوم» ⚖️\n\nجمعة سعيدة يا متر 🤍\nشاركها مع زميل بيبني الثقة دي كل يوم.\nmezan.pro'+TAGS,
 idea='جملة تحفيزية للجمعة: «المحاماة مش بس كسب قضايا… دي ثقة بتتبني كل يوم»')

post('p06_1800','''
<div class="box center" style="top:160px"><div class="h1" style="font-size:62px">الملخص في <span class="gold">ملف القضية</span>…<br>مش في دماغك 🧠</div></div>
<div class="box row" style="top:440px;gap:16px;align-items:center;justify-content:center">
 <div class="glass center" style="width:250px;padding:30px 10px"><div style="font-size:84px">📄📄</div><div style="font-size:30px;font-weight:900;margin-top:8px">أوراق القضية</div></div>
 <div style="font-size:54px;color:var(--gold2);font-family:CairoL">←</div>
 <div class="glass center" style="width:250px;padding:30px 10px;border-color:rgba(217,178,95,.6)"><div style="font-size:84px">🤖</div><div style="font-size:30px;font-weight:900;margin-top:8px">تلخيص بالذكاء<br>الاصطناعي</div></div>
 <div style="font-size:54px;color:var(--gold2);font-family:CairoL">←</div>
 <div class="glass center" style="width:250px;padding:30px 10px;border-color:rgba(217,178,95,.9)"><div style="font-size:84px">📁</div><div style="font-size:30px;font-weight:900;margin-top:8px">مربوط بملف<br>القضية</div></div>
</div>
<div class="box center" style="top:820px;font-size:32px;font-weight:800">ترجعله في أي وقت… <span class="gold">وتكمّل من غير ما تبدأ من الصفر</span></div>''',pill='مزايا ميزان برو ⭐')
add(date=D,time='18:00',kind='post',media=['p06_1800.png'],
 text='الملخص في ملف القضية… مش في دماغك 🧠\n\n📄 أوراق القضية ← 🤖 تلخيص بالذكاء الاصطناعي ← 📁 مربوط بملف القضية\n\nترجعله في أي وقت… وتكمّل من غير ما تبدأ من الصفر.\nجرّب ميزان برو 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='ميزة: رسم توضيحي أوراق ← تلخيص بالذكاء الاصطناعي ← مربوط بملف القضية')

sflow('s06_1100','''
<div style="font-size:84px;font-weight:900;line-height:1.35">خطتك في<br><span class="gold">الويكند</span>؟ 🌤️</div>
<div class="col" style="margin:0 40px;gap:26px">
 <div class="glass li" style="padding:28px 44px;gap:30px"><div style="font-size:84px">📚</div><div style="font-size:58px;font-weight:900">قراية</div></div>
 <div class="glass li" style="padding:28px 44px;gap:30px"><div style="font-size:84px">👨‍👩‍👧</div><div style="font-size:58px;font-weight:900">وقت مع العيلة</div></div>
 <div class="glass li" style="padding:28px 44px;gap:30px"><div style="font-size:84px">💼</div><div style="font-size:58px;font-weight:900">شغل برضه 😅</div></div>
</div>
<div style="font-size:48px;font-weight:800;color:#c9d4ea">ابعتلنا إجابتك 📩</div>''',gap=60)
add(date=D,time='11:00',kind='story',media=['s06_1100.png'],idea='قصة سؤال: خطتك في الويكند؟ قراية / عيلة / شغل برضه')

video('sv06_1500','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🤖</div>
 <div style="font-size:78px;font-weight:900;line-height:1.35;margin-top:20px" data-fx="rise" data-at=".4">3 استخدامات<br>للذكاء الاصطناعي<br><span class="gold">في المكتب</span></div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:28px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">📝</div><div class="t" style="font-size:54px">تلخيص المستندات</div></div>
  <div class="glass li" data-fx="right" data-at="1" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">✍️</div><div class="t" style="font-size:54px">مسودة أولى لرسالة</div></div>
  <div class="glass li" data-fx="right" data-at="1.8" style="padding:32px 40px"><div class="ic" style="width:100px;height:100px;font-size:56px">❓</div><div class="t" style="font-size:54px">أسئلة للتحضير</div></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:74px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".1">والمراجعة…<br><span class="gold">دايمًا عليك</span> ✅</div>
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv06_1500',D=12,preset='bm',seed=615,bpm=100,trans='3.2,8.4',pat=4),media=['sv06_1500.mp4'],idea='قصة فيديو ذكاء اصطناعي: 3 استخدامات في المكتب… والمراجعة دايمًا عليك')

sflow('s06_2030','''
<div style="font-size:180px;line-height:1">🤍</div>
<div style="font-size:100px;font-weight:900;line-height:1.35">خد نفسك<br><span class="gold">يا متر</span></div>
<div class="line" style="width:300px;margin:0 auto"></div>
<div style="font-size:54px;font-weight:700;color:#c9d4ea;line-height:1.6">الأسبوع الجاي<br>محتاجك فايق</div>''',gap=50)
add(date=D,time='20:30',kind='story',media=['s06_2030.png'],idea='قصة ويكند: «خد نفسك يا متر… الأسبوع الجاي محتاجك فايق»')

json.dump(M,open('mw2.json','w'),ensure_ascii=False,indent=1);print('ok',len(M))
