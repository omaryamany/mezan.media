from w4c import *

# ======================= SAT 2026-11-21 =======================
D='2026-11-21'
def frow(k,at):
    return f'<div class="glass" data-fx="right" data-at="{at}" style="display:flex;justify-content:space-between;align-items:center;padding:18px 30px;width:820px"><span style="font-size:36px;font-weight:800">{k}</span><span style="font-size:30px;color:var(--mute);letter-spacing:6px">..........</span></div>'
video('v21_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="drop" data-at=".1">🗂️</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:76px;margin-top:20px">فتحت ملف قضية…<br>وقعدت <span class="gold">تدوّر</span> على أساسياته؟</div>
</div>
<div class="sc" data-a="3.2" data-b="6.6">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:34px">نصيحة تنظيم 📌</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:30px">اعمل <span class="gold">صفحة غلاف</span><br>لكل ملف</div>
</div>
<div class="sc" data-a="6.4" data-b="12.4">
 <div class="paper" data-fx="pop" data-at=".1" style="padding:30px 40px 24px;width:880px">
  <div style="font-size:40px;font-weight:900;color:#8a6a2c">صفحة الغلاف</div>
 </div>
 <div class="col" style="gap:16px;margin-top:22px">
  '''+frow('👥 الأطراف','.5')+frow('🔢 رقم الدعوى','1')+frow('🏛️ المحكمة والدايرة','1.5')+frow('📅 الجلسة الجاية','2')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='افتح الملف… تلاقي المهم في أول صفحة'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v21_1000',D=16,preset='a',seed=2110,bpm=98,trans='3.2,6.4,12.2',pat=2),media=['v21_1000.mp4'],title='صفحة غلاف لكل ملف | ميزان برو',
 text='فتحت ملف قضية… وقعدت تدوّر على أساسياته؟ 🗂️\n\nاعمل لكل ملف "صفحة غلاف" في أوله:\n👥 الأطراف\n🔢 رقم الدعوى\n🏛️ المحكمة والدايرة\n📅 الجلسة الجاية\n\nدقيقتين وانت بتفتح الملف… بيوفّروا عليك تدوير كل مرة 👌\nاحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='فيديو موشن نصيحة تنظيم: صفحة غلاف لكل ملف (الأطراف · رقم الدعوى · المحكمة · الجلسة الجاية)')

def w4(e,t):
    return f'<div class="glass center" style="padding:22px 20px"><div style="font-size:64px">{e}</div><div style="font-size:40px;font-weight:900;margin-top:4px">{t}</div></div>'
post('p21_1400','''
<div class="box center" style="top:165px"><div class="h1" style="font-size:64px">لو هتوصف مكتبك<br>في <span class="gold">كلمة واحدة</span>… 🤔</div></div>
<div class="box" style="top:395px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 '''+w4('✨','مرتّب')+w4('🌪️','زحمة')+w4('📈','بيتحسّن')+w4('🙈','بلاش أتكلم')+'''
</div>''',pill='سؤال للمحامين 💬',foot='اختار كلمتك في الكومنتات 👇')
add(date=D,time='14:00',kind='post',media=['p21_1400.png'],
 text='سؤال للمحامين 💬\nلو هتوصف مكتبك في كلمة واحدة… هتختار إيه؟ 🤔\n\n✨ مرتّب\n🌪️ زحمة\n📈 بيتحسّن\n🙈 بلاش أتكلم\n\nقولنا بصراحة في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='سؤال تفاعلي: لو هتوصف مكتبك في كلمة؟ (مرتّب / زحمة / بيتحسّن / بلاش أتكلم)')

post('p21_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:60px">الدعوى <span class="gold">اتشطبت</span>؟ ⚠️<br>خد بالك من الميعاد</div></div>
<div class="box" style="top:370px;display:flex;gap:30px;align-items:center">
 <div style="flex:none;width:300px;height:300px;border-radius:50%;border:6px solid rgba(217,178,95,.7);display:grid;place-items:center;background:radial-gradient(circle,rgba(217,178,95,.16),transparent 70%)">
  <div class="center"><div class="gold" style="font-family:CairoL;font-weight:700;font-size:150px;line-height:1">60</div><div style="font-size:44px;font-weight:900">يوم</div></div>
 </div>
 <div class="glass" style="padding:30px 32px;font-size:33px;font-weight:700;line-height:1.7">لو عدّوا <b class="gold">60 يوم</b> بعد الشطب<br>ومحدش من الخصوم طلب<br>السير في الدعوى…<br><b>الدعوى تُعتبر كأن لم تكن</b></div>
</div>
<div class="box glass" style="top:720px;padding:24px 32px;font-size:28px;line-height:1.6;color:var(--mute)">📖 المادة 82 من قانون المرافعات المدنية والتجارية<br><span style="color:var(--ink);font-weight:800">سجّل تاريخ الشطب في ملف القضية من نفس اليوم 📌</span></div>''',pill='معلومة إجرائية ⚖️')
add(date=D,time='19:00',kind='post',media=['p21_1900.png'],
 text='معلومة إجرائية ⚖️ الدعوى اتشطبت؟\n\nطبقًا للمادة 82 من قانون المرافعات المدنية والتجارية:\nلو الطرفين محضروش والدعوى مش صالحة للحكم، المحكمة بتقرر شطبها.\nولو عدّى ⏳ 60 يوم ومحدش من الخصوم طلب السير فيها… الدعوى تُعتبر كأن لم تكن.\n\n📌 سجّل تاريخ الشطب في ملف القضية من نفس اليوم، وتابع الميعاد.\nاحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='معلومة إجرائية: شطب الدعوى — 60 يوم بدون طلب السير فيها تُعتبر كأن لم تكن (م.82 مرافعات)')

sflow('s21_1100','''
<div class="tag" style="font-size:36px;align-self:center">ذكاء اصطناعي بأمان 🤖</div>
<div style="font-size:70px;font-weight:900;line-height:1.4">طالب منه ملخص؟<br>قوله: <span class="gold">«في نقط مرقّمة»</span></div>
<div class="glass" style="padding:34px 44px;text-align:right;font-size:46px;font-weight:800;line-height:1.9">
 <div><span class="gold">1.</span> ━━━━━━</div><div><span class="gold">2.</span> ━━━━━━━━</div><div><span class="gold">3.</span> ━━━━</div>
</div>
<div style="font-size:50px;font-weight:800;line-height:1.5">كل نقطة… <span class="gold">راجعها على الأصل</span> ✅</div>''',gap=50)
add(date=D,time='11:00',kind='story',media=['s21_1100.png'],idea='قصة ذكاء اصطناعي: اطلب الملخص في نقط مرقّمة… وراجع كل نقطة على الأصل')

video('sv21_1500','''
<div class="sc" data-a="0" data-b="4.4">
 <div style="font-size:150px" data-fx="float" data-at=".1">🍃</div>
 <div style="font-size:96px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">التحضير<br><span class="gold">الهادي</span>…</div>
</div>
<div class="sc" data-a="4.2" data-b="8.6">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🎙️</div>
 <div style="font-size:90px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".4">بيبان<br>في <span class="gold">المرافعة</span></div>
</div>
'''+END_S.format(a='8.4',line='حضّر بدري…<br><span class="gold">واتكلم بثقة</span>'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv21_1500',D=12,preset='f',seed=2115,bpm=88,trans='4.2,8.4',pat=3),media=['sv21_1500.mp4'],idea='قصة فيديو اقتباس: «التحضير الهادي… بيبان في المرافعة»')

def ticket(lbl,big,sub,hl=False):
    bc='rgba(217,178,95,.85)' if hl else 'rgba(255,255,255,.18)'
    return f'<div style="position:relative;display:flex;align-items:center;border:3px dashed {bc};border-radius:30px;background:rgba(255,255,255,.05);padding:34px 40px"><div style="flex:1;text-align:right"><div style="font-size:40px;font-weight:800;color:var(--mute)">{lbl}</div><div style="font-size:30px;color:var(--mute);margin-top:4px">{sub}</div></div><div style="width:3px;align-self:stretch;margin:0 28px;background:repeating-linear-gradient(transparent 0 12px,rgba(217,178,95,.6) 12px 24px)"></div><div class="gold" style="font-family:Cairo;font-weight:900;font-size:72px;line-height:1.2">{big}</div></div>'
sflow('s21_2030','''
<div style="font-size:66px;font-weight:900;line-height:1.35">اختار <span class="gold">تذكرتك</span> 🎟️</div>
'''+ticket('البداية','مجانًا','14 يوم تجربة',True)+ticket('شهري','200 ج','كل شهر')+ticket('سنوي','2000 ج','لمدة سنة')+'''
''',gap=44)
add(date=D,time='20:30',kind='story',media=['s21_2030.png'],idea='قصة أسعار بشكل تذاكر: 14 يوم مجانًا · 200 ج شهري · 2000 ج سنوي')

# ======================= SUN 2026-11-22 =======================
D='2026-11-22'
post('p22_1000','''
<div class="box" style="top:150px"><div class="h1" style="font-size:58px">جوه ملف القضية في <span class="gold">ميزان برو</span> 🔍</div></div>
<div style="position:absolute;top:300px;left:90px;right:90px;height:560px">
 <div class="glass" style="position:absolute;inset:0;padding:30px 36px;border-color:rgba(217,178,95,.35)"><div style="font-size:38px;font-weight:900">📁 ملف القضية</div></div>
 <div class="glass" style="position:absolute;top:110px;left:50px;right:50px;bottom:0;padding:30px 36px;background:rgba(19,36,74,.92)"><div style="font-size:36px;font-weight:900">📄 أوراق ومستندات القضية</div></div>
 <div style="position:absolute;top:230px;left:100px;right:100px;bottom:30px;padding:30px 36px;border-radius:26px;border:2px solid rgba(217,178,95,.85);background:linear-gradient(160deg,#2a2a3e,#1a2442)">
  <div style="font-size:36px;font-weight:900" class="gold">🤖 ملخص بالذكاء الاصطناعي</div>
  <div style="font-size:28px;color:var(--mute);margin-top:16px;line-height:1.7">مربوط بملف القضية 🔗<br>ترجعله وقت ما تحتاجه</div>
 </div>
</div>''',pill='من مزايا النظام ✨')
add(date=D,time='10:00',kind='post',media=['p22_1000.png'],
 text='جوه ملف القضية في ميزان برو 🔍\n\n📁 ملف القضية\n  ↳ 📄 أوراق ومستندات القضية\n      ↳ 🤖 ملخص بالذكاء الاصطناعي… مربوط بملف القضية 🔗\n\nكل حاجة في مكانها، وترجعلها وقت ما تحتاجها.\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='ميزة بتصميم طبقات: ملف القضية ← أوراقها ← ملخص بالذكاء الاصطناعي مربوط بالملف')

video('v22_1400','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:150px" data-fx="pop" data-at=".1">📨</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:74px;margin-top:20px">قدّمت مذكرة<br>أو حافظة مستندات؟</div>
</div>
<div class="sc" data-a="3.4" data-b="7">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:80px">ابعت لموكلك<br><span class="gold">نسخة منها</span> 📎</div>
</div>
<div class="sc" data-a="6.8" data-b="12.4">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:34px">ليه؟ 👇</div>
 <div class="col" style="gap:26px;width:880px;margin-top:40px">
  '''+li('👀','يشوف شغلك بعينه','مش بس يسمع عنه',at='.5',ts=42)+'''
  '''+li('🤝','يحس إنه شريك في قضيته','مش متفرّج',at='1.3',ts=42)+'''
  '''+li('🧾','يبقى معاه نسخة ويرجعلها','بدل ما يسأل كل شوية',at='2.1',ts=42,extra='border-color:rgba(217,178,95,.7)')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='الموكل اللي شايف… بيطمن'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v22_1400',D=16,preset='em',seed=2214,bpm=104,trans='3.4,6.8,12.2',pat=1),media=['v22_1400.mp4'],title='ابعت لموكلك نسخة | ميزان برو',
 text='قدّمت مذكرة أو حافظة مستندات؟ 📨\nابعت لموكلك نسخة منها 📎\n\n👀 يشوف شغلك بعينه… مش بس يسمع عنه\n🤝 يحس إنه شريك في قضيته\n🧾 يبقى معاه نسخة يرجعلها بدل ما يسأل كل شوية\n\nالموكل اللي شايف… بيطمن 🤍\nإنت بتعملها؟ 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن تعامل مع الموكلين: ابعت لموكلك نسخة من المذكرة/الحافظة اللي اتقدمت')

post('p22_1900_1','''
<div class="glowc" style="width:760px;height:760px;left:160px;top:180px"></div>
<div class="box center" style="top:210px">
 <div style="font-size:130px">📞🙂</div>
 <div class="h1" style="font-size:64px;margin-top:20px">موكل قديم رجعلك<br><span class="gold">بقضية جديدة</span>…</div>
 <div class="lead" style="font-size:38px;margin-top:20px">وعايز تفتكر شغلك معاه قبل كده</div>
</div>''',pill='قبل / بعد 🔁',foot='اسحب ←',dots=(1,3))
post('p22_1900_2','''
<div class="box" style="top:160px"><span class="tag" style="font-size:34px;background:rgba(252,165,165,.15);color:#fca5a5">قبل 😓</span></div>
<div class="box col" style="top:270px;gap:24px">
 '''+li('🧠','تعتمد على ذاكرتك','وتتمنى متكونش نسيت تفصيلة',ts=40,extra='border-color:rgba(252,165,165,.3)')+li('🗄️','تدوّر في الدواليب والأرشيف','على ملف قديم',ts=40,extra='border-color:rgba(252,165,165,.3)')+li('⏳','وتقعد تقرا من الأول','عشان تفتكر حصل إيه',ts=40,extra='border-color:rgba(252,165,165,.3)')+'''
</div>''',pill='قبل / بعد 🔁',foot='اسحب ←',dots=(2,3))
post('p22_1900_3','''
<div class="box" style="top:160px"><span class="tag" style="font-size:34px">بعد ✨ مع ميزان برو</span></div>
<div class="box col" style="top:270px;gap:24px">
 '''+li('📁','تفتح ملف قضيته القديمة','أوراقها ومستنداتها في مكانها',ts=40,extra='border-color:rgba(217,178,95,.6)')+li('🤖','تقرا الملخص الأول','ملخص بالذكاء الاصطناعي مربوط بالملف',ts=40,extra='border-color:rgba(217,178,95,.6)')+li('🤝','وتبدأ معاه وانت فاكر','وده بيفرق في ثقته فيك',ts=40,extra='border-color:rgba(217,178,95,.6)')+'''
</div>
<div class="box center" style="top:850px"><span class="btn" style="font-size:34px">mezan.pro</span></div>''',foot='نظام إدارة متكامل لمكاتب المحاماة',dots=(3,3))
add(date=D,time='19:00',kind='post',media=['p22_1900_1.png','p22_1900_2.png','p22_1900_3.png'],
 text='موكل قديم رجعلك بقضية جديدة… وعايز تفتكر شغلك معاه قبل كده 📞\n\nقبل 😓\nتعتمد على ذاكرتك، وتدوّر في الأرشيف، وتقرا من الأول.\n\nبعد ✨ مع ميزان برو\nتفتح ملف قضيته القديمة، تقرا الملخص المربوط بيه، وتبدأ معاه وانت فاكر 🤝\n\nاسحب الصور ←\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='كاروسيل 3 صور قبل/بعد: موكل قديم رجعلك بقضية جديدة — الذاكرة والأرشيف ضد ملف قضيته وملخصها')

def wk(d,c,t):
    return f'<div class="glass li" data-fx="right" data-at="{d}" style="padding:24px 30px;border-right:14px solid {c}"><div class="t" style="font-size:50px">{t}</div></div>'
video('sv22_1100','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:150px" data-fx="drop" data-at=".1">🎨</div>
 <div style="font-size:92px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5"><span class="gold">لوّن</span><br>أجندة أسبوعك</div>
</div>
<div class="sc" data-a="3.4" data-b="8.6">
 <div class="col" style="width:100%;gap:28px">
  '''+wk('.2','#60a5fa','🔵 جلسات')+wk('.8','#fbbf24','🟡 مذكرات')+wk('1.4','#86efac','🟢 مقابلات موكلين')+wk('2','#f87171','🔴 مواعيد مهمة')+'''
 </div>
</div>
'''+END_S.format(a='8.4',line='نظرة واحدة…<br><span class="gold">وتعرف أسبوعك</span>'),D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv22_1100',D=12,preset='am2',seed=2211,bpm=114,trans='3.4,8.4',pat=0),media=['sv22_1100.mp4'],idea='قصة فيديو تنظيم: لوّن أجندة أسبوعك (جلسات · مذكرات · مقابلات · مواعيد مهمة)')

sflow('s22_1500','''
<div style="font-size:72px;font-weight:900;line-height:1.4">بتركّز أكتر<br><span class="gold">إمتى؟</span></div>
<div class="glass" style="padding:34px 40px"><div style="font-size:100px">🌅</div><div style="font-size:60px;font-weight:900;margin-top:10px">الصبح بدري</div></div>
<div class="glass" style="padding:34px 40px"><div style="font-size:100px">🌙</div><div style="font-size:60px;font-weight:900;margin-top:10px">بالليل</div></div>''',gap=44)
add(date=D,time='15:00',kind='story',media=['s22_1500.png'],idea='قصة سؤال: بتركّز أكتر إمتى؟ الصبح بدري ولا بالليل')

sflow('s22_2030','''
<div style="font-size:200px;line-height:.8;font-family:Messiri" class="gold">“</div>
<div style="font-size:84px;font-weight:900;line-height:1.5">اللي بيكتب…<br><span class="gold">مش بيسيب حاجة</span><br>للصدفة</div>
<div class="line" style="width:420px;margin:0 auto"></div>
<div style="font-size:44px;font-weight:700;color:var(--mute)">اكتب كل ميعاد وكل تفصيلة ✍️</div>''',gap=50)
add(date=D,time='20:30',kind='story',media=['s22_2030.png'],idea='قصة اقتباس: «اللي بيكتب… مش بيسيب حاجة للصدفة»')

# ======================= MON 2026-11-23 =======================
D='2026-11-23'
video('v23_1000','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:150px" data-fx="drop" data-at=".1">😰</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:74px;margin-top:20px">قبل الجلسة بساعة…<br>مش لاقي <span class="gold">صورة التوكيل</span>؟</div>
</div>
<div class="sc" data-a="3.4" data-b="6.8">
 <div style="display:flex;gap:30px;justify-content:center">
  <div class="glass" data-fx="pop" data-at=".1" style="padding:30px 34px;font-size:40px;font-weight:800">🎒 الشنطة؟</div>
  <div class="glass" data-fx="pop" data-at=".4" style="padding:30px 34px;font-size:40px;font-weight:800">🗄️ الدُرج؟</div>
  <div class="glass" data-fx="pop" data-at=".7" style="padding:30px 34px;font-size:40px;font-weight:800">📱 الموبايل؟</div>
 </div>
 <div class="h1" data-fx="rise" data-at="1.2" style="font-size:64px;margin-top:50px">ولا عند <span class="gold">زميلك</span>؟ 🤷</div>
</div>
<div class="sc" data-a="6.6" data-b="12.4">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:34px">الحل ✨</div>
 <div class="col" style="gap:26px;width:880px;margin-top:40px">
  '''+li('📁','كل مستندات القضية في ملفها','التوكيل وأي ورقة تخصّها',at='.5',ts=42)+'''
  '''+li('🖥️','على نظام واحد لمكتبك','ميزان برو — نظام إدارة متكامل',at='1.3',ts=42,extra='border-color:rgba(217,178,95,.7)')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='كل ورقة… في ملف قضيتها'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v23_1000',D=16,preset='cm',seed=2310,bpm=110,trans='3.4,6.6,12.2',pat=4),media=['v23_1000.mp4'],title='فين صورة التوكيل؟ | ميزان برو',
 text='قبل الجلسة بساعة… ومش لاقي صورة التوكيل؟ 😰\nالشنطة؟ الدُرج؟ الموبايل؟ ولا عند زميلك؟ 🤷\n\nالحل ✨\n📁 كل مستندات القضية تبقى في ملفها\n🖥️ على نظام واحد لمكتبك كله\n\nميزان برو: نظام إدارة متكامل لمكاتب المحاماة.\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='فيديو موشن مشكلة وحلها: قبل الجلسة مش لاقي صورة التوكيل ← كل مستندات القضية في ملفها على نظام واحد')

post('p23_1400','''
<div class="box" style="top:150px"><div class="h1" style="font-size:58px">خلّي الذكاء الاصطناعي<br><span class="gold">يراجع لغة</span> مذكرتك ✍️</div></div>
<div class="box" style="top:380px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
 <div class="glass" style="padding:30px;border-color:rgba(134,239,172,.45)"><div style="font-size:36px;font-weight:900" class="ok">✅ اطلب منه</div><div style="font-size:31px;font-weight:700;line-height:1.9;margin-top:12px">الأخطاء الإملائية<br>الجمل الطويلة<br>علامات الترقيم<br>التكرار</div></div>
 <div class="glass" style="padding:30px;border-color:rgba(252,165,165,.45)"><div style="font-size:36px;font-weight:900" class="no">✋ إنت المسؤول عن</div><div style="font-size:31px;font-weight:700;line-height:1.9;margin-top:12px">الوقائع<br>الدفوع<br>الأسانيد<br>القرار النهائي</div></div>
</div>
<div class="box center" style="top:830px;font-size:30px;font-weight:800">وقبل ما تلصق النص: <span class="gold">شيل أي بيانات شخصية</span> 🔒</div>''',pill='ذكاء اصطناعي بأمان 🤖')
add(date=D,time='14:00',kind='post',media=['p23_1400.png'],
 text='خلّي الذكاء الاصطناعي يراجع لغة مذكرتك ✍️\n\n✅ اطلب منه: الأخطاء الإملائية، الجمل الطويلة، علامات الترقيم، التكرار\n✋ وإنت المسؤول عن: الوقائع، الدفوع، الأسانيد، والقرار النهائي\n\n🔒 وقبل ما تلصق النص في أي أداة: شيل أي بيانات شخصية.\nجرّبها في مذكرتك الجاية 👇\nmezan.pro'+TAGS,
 idea='نصيحة ذكاء اصطناعي بأمان: خليه يراجع لغة المذكرة (إملاء/جمل/ترقيم) والمضمون عليك')

post('p23_1900','''
<div class="box center" style="top:140px"><div class="h1" style="font-size:58px">حسابك مع <span class="gold">ميزان برو</span> 🧾</div></div>
<div class="paper" style="position:absolute;top:270px;left:190px;right:190px;padding:40px 46px 30px;transform:rotate(-1.5deg)">
 <div style="text-align:center;font-family:Messiri;font-size:40px;color:#8a6a2c">ميزان برو</div>
 <div style="border-top:3px dashed #c9bfa5;margin:18px 0"></div>
 <div style="display:flex;justify-content:space-between;font-size:34px;font-weight:800;line-height:2"><span>تجربة مجانية</span><span style="color:#8a6a2c">14 يوم</span></div>
 <div style="display:flex;justify-content:space-between;font-size:34px;font-weight:800;line-height:2"><span>اشتراك شهري</span><span>200 ج</span></div>
 <div style="text-align:center;font-size:28px;color:#6b7280;font-weight:700">أو</div>
 <div style="display:flex;justify-content:space-between;font-size:34px;font-weight:800;line-height:2"><span>اشتراك سنوي</span><span>2000 ج</span></div>
 <div style="border-top:3px dashed #c9bfa5;margin:18px 0"></div>
 <div style="text-align:center;font-family:CairoL;font-weight:700;font-size:34px;letter-spacing:2px;color:#1b2440">mezan.pro</div>
</div>''',pill='الأسعار 🏷️')
add(date=D,time='19:00',kind='post',media=['p23_1900.png'],
 text='حسابك مع ميزان برو 🧾\n\n🎁 تجربة مجانية: 14 يوم\n📅 اشتراك شهري: 200 ج\n🗓️ أو اشتراك سنوي: 2000 ج\n\nابدأ تجربتك النهارده 👈 mezan.pro'+TAGS,
 idea='تذكير بالأسعار بشكل فاتورة: 14 يوم مجانًا · 200 ج شهري · 2000 ج سنوي')

sflow('s23_1100','''
<div style="font-size:66px;font-weight:900;line-height:1.4">موكلك بعت رسالة<br>وإنت <span class="gold">مشغول</span>؟</div>
<div style="align-self:flex-start;max-width:760px;padding:34px 40px;border-radius:40px 40px 40px 10px;background:#f4f1e8;color:#1b2440;font-size:46px;font-weight:800;line-height:1.6;text-align:right">وصلتني رسالتك 👍<br>هرد عليك بالتفاصيل بكرة الصبح</div>
<div style="font-size:52px;font-weight:800;line-height:1.5">ردّ في نفس اليوم<br><span class="gold">ولو بسطر واحد</span> ⏱️</div>''',gap=56)
add(date=D,time='11:00',kind='story',media=['s23_1100.png'],idea='قصة تعامل مع الموكلين: رد على موكلك في نفس اليوم ولو بسطر «وصلتني… هرد بكرة»')

video('sv23_1500','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:84px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">يعني إيه<br><span class="gold">ERP</span><br>لمكتب محاماة؟</div>
</div>
<div class="sc" data-a="3.4" data-b="8.6">
 <div class="col" style="width:100%;gap:30px">
  '''+opt('1','نظام <span class="gold">واحد</span>','.2')+opt('2','لإدارة <span class="gold">المكتب كله</span>','.9')+opt('3','بدل <span class="gold">ألف مكان</span>','1.6')+'''
 </div>
</div>
'''+END_S.format(a='8.4',line='ميزان برو<br><span class="gold">نظام إدارة متكامل</span>'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv23_1500',D=12,preset='bm',seed=2315,bpm=126,trans='3.4,8.4',pat=2),media=['sv23_1500.mp4'],idea='قصة فيديو ميزة: يعني إيه ERP لمكتب محاماة؟ نظام واحد لإدارة المكتب كله')

sflow('s23_2030','''
<div style="font-size:70px;font-weight:900;line-height:1.4">بتاخد شغل معاك<br><span class="gold">البيت؟</span> 🏠</div>
'''+''.join(f'<div class="glass" style="padding:40px;font-size:60px;font-weight:900">{x}</div>' for x in ['دايمًا 😅','أحيانًا 🤏','أبدًا 😎'])+'''
<div style="font-size:42px;font-weight:700;color:var(--gold2)">ابعتلنا إجابتك 📩</div>''',gap=40)
add(date=D,time='20:30',kind='story',media=['s23_2030.png'],idea='قصة سؤال: بتاخد شغل معاك البيت؟ دايمًا / أحيانًا / أبدًا')

# ======================= TUE 2026-11-24 =======================
D='2026-11-24'
post('p24_1000','''
<div class="glowc" style="width:820px;height:820px;left:130px;top:140px"></div>
<div style="position:absolute;top:150px;right:90px;font-size:260px;line-height:1;font-family:Messiri" class="gold">“</div>
<div class="box center" style="top:330px"><div style="font-size:64px;font-weight:900;line-height:1.55">المكتب المرتّب…<br>بيخلّي المحامي <span class="gold">يفكّر</span><br>بدل ما <span class="gold">يدوّر</span></div></div>
<div class="box" style="top:770px;display:flex;justify-content:center"><div class="line" style="width:360px"></div></div>
<div class="box center" style="top:810px;font-size:30px;font-weight:700;color:var(--mute)">صباح التركيز يا متر ☕</div>''',pill='جملة النهارده ✨')
add(date=D,time='10:00',kind='post',media=['p24_1000.png'],
 text='«المكتب المرتّب… بيخلّي المحامي يفكّر بدل ما يدوّر» ✨\n\nصباح التركيز يا متر ☕\nشاركها مع زميل 👇\nmezan.pro'+TAGS,
 idea='جملة تحفيزية: «المكتب المرتّب… بيخلّي المحامي يفكّر بدل ما يدوّر»')

video('v24_1400','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:140px" data-fx="pop" data-at=".1">💬</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:70px;margin-top:20px">زميلك هيستلم قضية منك<br>وقالك: <span class="gold">«ابعتلي ملخصها»</span></div>
</div>
<div class="sc" data-a="3.4" data-b="7.8">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:34px;background:rgba(252,165,165,.15);color:#fca5a5">قبل 😓</div>
 <div class="glass" data-fx="rise" data-at=".5" style="padding:34px 44px;margin-top:36px;font-size:46px;font-weight:800;line-height:1.7;border-color:rgba(252,165,165,.35)">تقعد تجمّع الورق<br>وتكتب الملخص من الأول ✍️</div>
</div>
<div class="sc" data-a="7.6" data-b="12.4">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:34px">بعد ✨ مع ميزان برو</div>
 <div class="glass" data-fx="rise" data-at=".5" style="padding:34px 44px;margin-top:36px;font-size:46px;font-weight:800;line-height:1.7;border-color:rgba(217,178,95,.7)">أوراق القضية متلخّصة<br>بالذكاء الاصطناعي…<br><span class="gold">والملخص في ملفها</span> 🔗</div>
</div>
'''+END_P.format(a='12.2',line='سلّم القضية… وانت مطمّن'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v24_1400',D=16,preset='g',seed=2414,bpm=94,trans='3.4,7.6,12.2',pat=3),media=['v24_1400.mp4'],title='ابعتلي ملخصها | ميزان برو',
 text='زميلك هيستلم قضية منك وقالك: «ابعتلي ملخصها» 💬\n\nقبل 😓\nتقعد تجمّع الورق وتكتب الملخص من الأول.\n\nبعد ✨ مع ميزان برو\nأوراق ومستندات القضية متلخّصة بالذكاء الاصطناعي، والملخص مربوط بملف القضية 🔗\n\nسلّم القضية وانت مطمّن.\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='فيديو موشن قبل/بعد: زميل هيستلم قضية وطالب ملخصها — تكتبه من الأول ضد ملخص جاهز في ملفها')

def step4(n,t,d):
    return f'<div class="glass li" style="padding:30px 34px"><div class="num" style="width:80px;height:80px;font-size:42px">{n}</div><div><div class="t" style="font-size:42px">{t}</div><div class="d" style="font-size:29px">{d}</div></div></div>'
post('p24_1900_1','''
<div class="glowc" style="width:760px;height:760px;left:160px;top:170px"></div>
<div class="box center" style="top:200px">
 <div style="font-size:130px">📦</div>
 <div class="h1" style="font-size:66px;margin-top:20px">القضية <span class="gold">خلصت</span>…<br>ملفها هيروح فين؟</div>
 <div class="lead" style="font-size:38px;margin-top:20px">4 خطوات تقفل بيها الملف صح</div>
</div>''',pill='نصيحة تنظيم 📌',foot='اسحب ←',dots=(1,4))
post('p24_1900_2','''
<div class="box col" style="top:300px;gap:40px">
 '''+step4(1,'اكتب سطر النهاية','الحكم أو النتيجة + التاريخ')+step4(2,'راجع الأصول','اللي يخص الموكل يرجعله')+'''
</div>''',pill='نصيحة تنظيم 📌',foot='اسحب ←',dots=(2,4))
post('p24_1900_3','''
<div class="box col" style="top:300px;gap:40px">
 '''+step4(3,'علّم الملف «منتهي»','عشان ميتلخبطش مع الشغّال')+step4(4,'انقله للأرشيف','بنفس اسمه ورقمه')+'''
</div>''',pill='نصيحة تنظيم 📌',foot='اسحب ←',dots=(3,4))
post('p24_1900_4','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:150px"></div>
<div class="box center" style="top:200px">
 <div style="font-size:110px">🗄️✨</div>
 <div class="h1" style="font-size:58px;margin-top:20px">الملف اللي <span class="gold">اتقفل صح</span><br>بيتلاقي بسهولة بعد سنين</div>
 <div class="lead" style="font-size:34px;margin-top:24px">ومع ميزان برو: مكتبك كله على نظام واحد</div>
</div>
<div class="box center" style="top:800px"><span class="btn" style="font-size:34px">mezan.pro</span></div>''',foot='نظام إدارة متكامل لمكاتب المحاماة',dots=(4,4))
add(date=D,time='19:00',kind='post',media=['p24_1900_1.png','p24_1900_2.png','p24_1900_3.png','p24_1900_4.png'],
 text='القضية خلصت… ملفها هيروح فين؟ 📦\n4 خطوات تقفل بيها الملف صح:\n\n1️⃣ اكتب سطر النهاية: الحكم أو النتيجة + التاريخ\n2️⃣ راجع الأصول: اللي يخص الموكل يرجعله\n3️⃣ علّم الملف «منتهي» عشان ميتلخبطش مع الشغّال\n4️⃣ انقله للأرشيف بنفس اسمه ورقمه\n\nالملف اللي اتقفل صح… بيتلاقي بسهولة بعد سنين 🗄️\nاسحب الصور ←\nmezan.pro'+TAGS,
 idea='كاروسيل 4 صور نصيحة تنظيم: إزاي تقفل ملف قضية خلصت (سطر النهاية · الأصول · منتهي · الأرشيف)')

video('sv24_1100','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:150px" data-fx="pop" data-at=".1">📝</div>
 <div style="font-size:80px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">كتبت ملاحظات<br><span class="gold">على السريع</span>؟</div>
</div>
<div class="sc" data-a="3.4" data-b="8.6">
 <div class="glass" data-fx="rise" data-at=".1" style="padding:40px;font-size:54px;font-weight:800;line-height:1.6">اطلب من الذكاء الاصطناعي<br><span class="gold">يرتّبها في نقط</span> 🤖</div>
 <div style="font-size:50px;font-weight:800;margin-top:50px;line-height:1.5" data-fx="rise" data-at="1">من غير أسماء<br>ولا بيانات شخصية 🔒</div>
</div>
'''+END_S.format(a='8.4',line='هو يرتّب…<br><span class="gold">وإنت تراجع</span>'),D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv24_1100',D=12,preset='dm',seed=2411,bpm=100,trans='3.4,8.4',pat=1),media=['sv24_1100.mp4'],idea='قصة فيديو ذكاء اصطناعي: ملاحظات على السريع؟ خليه يرتّبها في نقط من غير بيانات شخصية')

sflow('s24_1500','''
<div style="font-size:64px;font-weight:900;line-height:1.4">الاشتراك <span class="gold">السنوي</span></div>
<div style="display:flex;justify-content:center;align-items:flex-end;gap:16px"><span class="gold" style="font-family:CairoL;font-weight:700;font-size:240px;line-height:1">2000</span><span style="font-size:80px;font-weight:900;margin-bottom:30px">ج</span></div>
<div style="font-size:52px;font-weight:800">سنة كاملة 🗓️</div>
<div class="glass" style="padding:30px;margin:0 40px;font-size:42px;font-weight:800;line-height:1.6">أو شهري بـ <span class="gold">200 ج</span><br>وابدأ بـ <span class="gold">14 يوم مجانًا</span> 🎁</div>''',gap=40)
add(date=D,time='15:00',kind='story',media=['s24_1500.png'],idea='قصة أسعار: رقم 2000 كبير «سنة كاملة» + شهري 200 ج + 14 يوم مجانًا')

sflow('s24_2030','''
<div style="font-size:64px;font-weight:900;line-height:1.4">موكلك أول مرة<br>يحضر <span class="gold">جلسة</span>؟ 🏛️</div>
<div style="font-size:42px;font-weight:700;color:var(--mute)">قوله قبلها:</div>
'''+''.join(f'<div class="glass li" style="padding:30px 36px;text-align:right"><div class="ic" style="width:90px;height:90px;font-size:48px">{a}</div><div class="t" style="font-size:46px">{b}</div></div>' for a,b in [('🕘','ييجي بدري'),('🪪','معاه بطاقته'),('🤫','يتكلم لما يتسأل بس')])+'''
''',gap=36)
add(date=D,time='20:30',kind='story',media=['s24_2030.png'],idea='قصة تعامل مع الموكلين: موكلك أول مرة يحضر جلسة؟ (ييجي بدري · بطاقته · يتكلم لما يتسأل)')

json.dump(M,open('mw5a.json','w'),ensure_ascii=False,indent=1);print(len(M))
