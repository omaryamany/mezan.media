from w4c import *

# ======================= WED 2026-11-18 =======================
D='2026-11-18'
def bar(n,t,w):
    return f'<div class="glass" style="padding:14px 30px;display:flex;align-items:center;gap:24px"><div class="num" style="width:60px;height:60px;font-size:32px">{n}</div><div style="flex:1;font-size:38px;font-weight:900">{t}</div><div style="width:44px;height:44px;border-radius:50%;border:3px solid rgba(217,178,95,.6)"></div></div>'
post('p18_1000','''
<div class="box" style="top:160px"><div class="h1" style="font-size:60px">إيه أكتر نوع قضايا<br><span class="gold">بتشتغل فيه؟</span> ⚖️</div></div>
<div class="box col" style="top:360px;gap:14px">
 '''+bar(1,'مدني',62)+bar(2,'جنائي',48)+bar(3,'أسرة',70)+bar(4,'عمالي',35)+bar(5,'تجاري',55)+'''
</div>''',pill='سؤال للمحامين 💬',foot='اكتب الرقم في الكومنتات 👇')
add(date=D,time='10:00',kind='post',media=['p18_1000.png'],
 text='سؤال للمحامين 💬\nإيه أكتر نوع قضايا بتشتغل فيه؟ ⚖️\n\n1️⃣ مدني\n2️⃣ جنائي\n3️⃣ أسرة\n4️⃣ عمالي\n5️⃣ تجاري\n\nاكتب الرقم في الكومنتات 👇 ولو بتشتغل في كله قول 😄\nmezan.pro'+TAGS,
 idea='سؤال تفاعلي: إيه أكتر نوع قضايا بتشتغل فيه؟ (مدني/جنائي/أسرة/عمالي/تجاري)')

def word(a,b,ic,w,d):
    return f'''<div class="sc" data-a="{a}" data-b="{b}">
 <div style="font-size:130px" data-fx="pop" data-at=".1">{ic}</div>
 <div class="gold" data-fx="stamp" data-at=".4" style="font-family:Messiri;font-size:150px;line-height:1.3">{w}</div>
 <div class="lead" data-fx="rise" data-at=".9" style="font-size:42px;font-weight:800;color:#fff;line-height:1.5">{d}</div>
</div>'''
video('v18_1400','''
<div class="sc" data-a="0" data-b="3.4">
 <img src="../logo.svg" width="170" data-fx="spin" data-at=".1">
 <div class="h1" data-fx="rise" data-at=".5" style="font-size:84px;margin-top:24px">ميزان برو<br><span class="gold">في 3 كلمات</span></div>
</div>
'''+word(3.2,6.4,'🗂️','منظّم','نظام إدارة متكامل (ERP)<br>لمكتبك')+word(6.2,9.4,'🤖','ذكي','بيلخّص أوراق ومستندات القضايا<br>ويربط الملخص بملف القضية')+word(9.2,12.4,'🔒','آمن','حماية بياناتك وسريتها<br>أولوية')+END_P.format(a='12.2',line='جرّبه 14 يوم مجانًا'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v18_1400',D=16,preset='f',seed=1814,bpm=104,trans='3.2,6.2,9.2,12.2',pat=0),media=['v18_1400.mp4'],title='ميزان برو في 3 كلمات',
 text='ميزان برو في 3 كلمات ✨\n\n🗂️ منظّم: نظام إدارة متكامل (ERP) لمكتبك\n🤖 ذكي: بيلخّص أوراق ومستندات القضايا بالذكاء الاصطناعي ويربط الملخص بملف القضية\n🔒 آمن: حماية بياناتك وسريتها أولوية\n\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='فيديو موشن ميزة: ميزان برو في 3 كلمات (منظّم · ذكي · آمن)')

RD='<span style="display:inline-block;width:{w}px;height:34px;background:#1b2440;border-radius:6px;vertical-align:middle"></span>'
post('p18_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:54px">قبل أي أداة ذكاء اصطناعي عامة…<br><span class="gold">شيل البيانات الشخصية</span> ✂️</div></div>
<div class="box paper" style="top:360px;padding:28px 34px;font-size:32px;font-weight:700;line-height:1.9">
 <div>الموكل '''+RD.format(w=150)+''' ساكن في '''+RD.format(w=170)+'''</div>
 <div>ورقمه '''+RD.format(w=230)+''' وعنده نزاع إيجار…</div>
 <div style="border-top:2px dashed #c9bfa6;margin-top:12px;padding-top:12px;color:#8a6a2c">✓ «موكل (أ) عنده نزاع إيجار…»</div>
</div>
<div class="box" style="top:720px;display:flex;gap:16px;justify-content:center">
 <span class="tag" style="font-size:28px">👤 الأسماء</span><span class="tag" style="font-size:28px">🪪 الأرقام القومية والتليفونات</span><span class="tag" style="font-size:28px">🏠 العناوين</span>
</div>
<div class="box center" style="top:830px;font-size:34px;font-weight:800">اسأل عن <span class="gold">الفكرة القانونية</span>… مش عن الشخص</div>''',pill='ذكاء اصطناعي بأمان 🤖')
add(date=D,time='19:00',kind='post',media=['p18_1900.png'],
 text='قبل ما تكتب لأي أداة ذكاء اصطناعي عامة… 🤖\nشيل البيانات الشخصية الأول ✂️\n\n👤 الأسماء ← اكتب «موكل (أ)»\n🪪 الأرقام القومية والتليفونات\n🏠 العناوين وأي تفصيلة تعرّف الشخص\n\nاسأل عن الفكرة القانونية… مش عن الشخص 🔒\nmezan.pro'+TAGS,
 idea='نصيحة ذكاء اصطناعي بأمان: شيل الأسماء والأرقام والعناوين قبل ما تكتب لأداة عامة')

sflow('s18_1100','''
<div style="font-size:120px">📞</div>
<div style="font-size:68px;font-weight:900;line-height:1.4">آخر كل مكالمة<br>مع موكلك… قوله<br><span class="gold">الخطوة الجاية</span> ➡️</div>
<div class="glass" style="padding:40px;margin:0 30px;border-radius:40px 40px 40px 10px;font-size:50px;font-weight:800;line-height:1.55">«هقدّم المذكرة يوم …<br>وهكلّمك بعدها»</div>
<div style="font-size:54px;font-weight:900;line-height:1.5">يقفل المكالمة<br><span class="gold">وهو فاهم</span> 👌</div>''',gap=50)
add(date=D,time='11:00',kind='story',media=['s18_1100.png'],idea='قصة تعامل مع الموكلين: آخر كل مكالمة قول لموكلك الخطوة الجاية')

video('sv18_1500','''
<div class="sc" data-a="0" data-b="3.2">
 <div style="font-size:160px" data-fx="drop" data-at=".1">🏔️</div>
 <div style="font-size:86px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">أصعب مهمة<br><span class="gold">في يومك؟</span></div>
</div>
<div class="sc" data-a="3" data-b="6.2">
 <div style="font-size:160px" data-fx="pop" data-at=".1">☀️</div>
 <div style="font-size:86px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".4">اعملها<br><span class="gold">الأول</span></div>
 <div class="lead" data-fx="rise" data-at=".8" style="font-size:50px;margin-top:20px">وانت لسه مركّز</div>
</div>
<div class="sc" data-a="6" data-b="8.6">
 <div style="font-size:160px" data-fx="pop" data-at=".1">👌</div>
 <div style="font-size:80px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".4">والباقي<br><span class="gold">هيبقى أسهل</span></div>
</div>
'''+END_S.format(a='8.4',line='جرّبها<br><span class="gold">بكرة الصبح</span> ☕'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv18_1500',D=12,preset='am2',seed=1815,bpm=116,trans='3,6,8.4',pat=2),media=['sv18_1500.mp4'],idea='قصة فيديو تنظيم وقت: ابدأ يومك بأصعب مهمة')

sflow('s18_2030','''
<div style="font-size:130px">🧘</div>
<div style="font-size:96px;font-weight:900;line-height:1.35">التنظيم<br>مش <span class="gold">رفاهية</span>…</div>
<div class="line" style="width:360px;margin:0 auto"></div>
<div style="font-size:96px;font-weight:900;line-height:1.35">ده<br><span class="gold">راحة بال</span></div>''',gap=50)
add(date=D,time='20:30',kind='story',media=['s18_2030.png'],idea='قصة اقتباس: «التنظيم مش رفاهية… ده راحة بال»')

# ======================= THU 2026-11-19 =======================
D='2026-11-19'
video('v19_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="drop" data-at=".1">😱</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:80px;margin-top:20px">المستند الأصلي<br><span class="gold">ضاع أو اتبهدل؟</span></div>
</div>
<div class="sc" data-a="3.2" data-b="6.6">
 <div style="font-size:150px" data-fx="pop" data-at=".1">📄📄</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:90px;margin-top:20px">قاعدة<br><span class="gold">النسختين</span></div>
</div>
<div class="sc" data-a="6.4" data-b="12.4">
 <div class="col" style="gap:26px;width:880px">
  '''+li('📸','صوّر أي مستند مهم','أول ما يوصلك',at='.2',ts=42)+li('🗂️','احتفظ بالنسخة في مكان تاني','غير مكان الأصل',at='1',ts=42)+li('🔐','والأصل في مكان آمن ومعروف','تلاقيه وقت ما تحتاجه',at='1.8',ts=42,extra='border-color:rgba(217,178,95,.7)')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='نسخة زيادة… راحة بال كبيرة'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v19_1000',D=16,preset='g',seed=1910,bpm=96,trans='3.2,6.4,12.2',pat=1),media=['v19_1000.mp4'],title='قاعدة النسختين | ميزان برو',
 text='قاعدة النسختين 📄📄\n\nالمستند الأصلي ضاع أو اتبهدل؟ متخليش ده يحصل:\n📸 صوّر أي مستند مهم أول ما يوصلك\n🗂️ احتفظ بالنسخة في مكان تاني غير الأصل\n🔐 والأصل يتحفظ في مكان آمن ومعروف\n\nنسخة زيادة… راحة بال كبيرة 👌\nmezan.pro'+TAGS,
 idea='فيديو موشن نصيحة تنظيم: قاعدة النسختين للمستندات المهمة')

def side(tag,c,items,bg):
    s=''.join(f'<div class="li" style="gap:16px;margin-top:20px"><div style="font-size:46px">{i}</div><div style="font-size:31px;font-weight:800;line-height:1.35">{t}</div></div>' for i,t in items)
    return f'<div style="flex:1;padding:30px 28px;border-radius:26px;border:2px solid {c};background:{bg}"><div class="tag" style="font-size:30px;{"background:rgba(252,165,165,.15);color:#fca5a5" if "252" in c else ""}">{tag}</div>{s}</div>'
post('p19_1400','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:64px">زميل جديد <span class="gold">انضم لمكتبك</span> 👋</div></div>
<div class="box row" style="top:290px;gap:22px">
 '''+side('قبل (بالورق)','rgba(252,165,165,.35)',[('🗄️','يدوّر في الدواليب'),('❓','يسأل عن كل ملف'),('⏳','وياخد وقت لحد ما يفهم')],'rgba(255,255,255,.03)')+side('بعد (مع ميزان برو)','rgba(217,178,95,.7)',[('📁','كل قضية ليها ملف'),('🤖','ملخص أوراقها مربوط بالملف'),('✅','يبدأ من الملخص ويفهم أسرع')],'rgba(217,178,95,.08)')+'''
</div>
<div class="box center" style="top:860px;font-size:32px;font-weight:800">مكتب منظّم… <span class="gold">أي حد يكمّل فيه</span></div>''',pill='قبل / بعد ⚖️')
add(date=D,time='14:00',kind='post',media=['p19_1400.png'],
 text='زميل جديد انضم لمكتبك 👋\n\nقبل (بالورق):\n🗄️ يدوّر في الدواليب\n❓ يسأل عن كل ملف\n⏳ وياخد وقت لحد ما يفهم\n\nبعد (مع ميزان برو):\n📁 كل قضية ليها ملف\n🤖 وملخص أوراقها بالذكاء الاصطناعي مربوط بالملف\n✅ يبدأ من الملخص ويفهم أسرع\n\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='قبل/بعد: زميل جديد انضم للمكتب — الدواليب والأسئلة ضد ملف القضية والملخص')

def ck(t):
    return f'<div style="display:flex;align-items:center;gap:20px;padding:14px 0;border-bottom:1px solid #e0d8c4"><div style="width:44px;height:44px;border-radius:10px;border:3px solid #b88d3a;display:grid;place-items:center;color:#8a6a2c;font-size:30px;font-weight:900">✓</div><div style="font-size:36px;font-weight:800">{t}</div></div>'
post('p19_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:58px">اتفاق الأتعاب…<br><span class="gold">اكتبه من أول يوم</span> ✍️</div></div>
<div class="box paper" style="top:350px;left:120px;right:120px;padding:20px 40px 24px;transform:rotate(1.5deg)">
 <div style="text-align:center;font-family:Messiri;font-size:38px;color:#8a6a2c;padding-bottom:6px;border-bottom:2px solid #c9bfa6">اتفاق أتعاب</div>
 '''+ck('💰 قيمة الأتعاب وطريقة الدفع')+ck('📋 نطاق الشغل: إيه داخل وإيه لأ')+ck('📅 مواعيد الدفعات')+ck('🤝 توقيع الطرفين').replace('border-bottom:1px solid #e0d8c4','')+'''
</div>
<div class="box center" style="top:905px;font-size:30px;font-weight:800">الوضوح من الأول <span class="gold">بيحمي الطرفين</span></div>''',pill='تعامل مع الموكلين 🤝')
add(date=D,time='19:00',kind='post',media=['p19_1900.png'],
 text='اتفاق الأتعاب… اكتبه من أول يوم ✍️\n\n💰 قيمة الأتعاب وطريقة الدفع\n📋 نطاق الشغل: إيه اللي داخل وإيه لأ\n📅 مواعيد الدفعات\n🤝 توقيع الطرفين\n\nالوضوح من الأول بيحمي العلاقة مع موكلك… وبيحميك.\nإنت بتكتبه دايمًا؟ 👇\nmezan.pro'+TAGS,
 idea='نصيحة تعامل مع الموكلين: اتفاق الأتعاب مكتوب من أول يوم (القيمة/النطاق/الدفعات/التوقيع)')

sflow('s19_1100','''
<div style="font-size:120px">🛋️</div>
<div style="font-size:72px;font-weight:900;line-height:1.4">في الويكند…<br>بتفتح <span class="gold">ملفات الشغل</span>؟</div>
<div class="glass" style="padding:44px;margin:0 60px;font-size:64px;font-weight:900">آه طبعًا 📂</div>
<div style="padding:44px;margin:0 60px;border-radius:28px;font-size:64px;font-weight:900;color:var(--navy);background:linear-gradient(160deg,var(--gold2),var(--gold) 60%,#b88d3a)">لأ… راحة 😌</div>
<div style="font-size:46px;font-weight:800;color:var(--gold2)">ابعتلنا ردّك 📩</div>''',gap=44)
add(date=D,time='11:00',kind='story',media=['s19_1100.png'],idea='قصة سؤال: في الويكند بتفتح ملفات الشغل؟ آه / لأ')

video('sv19_1500','''
<div class="sc" data-a="0" data-b="3">
 <div style="font-size:160px" data-fx="pop" data-at=".1">🏷️</div>
 <div style="font-size:90px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">ميزان برو<br><span class="gold">بكام؟</span></div>
</div>
<div class="sc" data-a="2.8" data-b="5.8">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:48px">شهري</div>
 <div style="font-size:200px;font-weight:900;line-height:1.2;margin-top:20px"><span class="gold" style="font-family:CairoL" data-fx="count" data-to="200" data-at=".3" data-d="1">0</span> ج</div>
</div>
<div class="sc" data-a="5.6" data-b="8.6">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:48px">سنوي</div>
 <div style="font-size:180px;font-weight:900;line-height:1.2;margin-top:20px"><span class="gold" style="font-family:CairoL" data-fx="count" data-to="2000" data-at=".3" data-d="1">0</span> ج</div>
</div>
'''+END_S.format(a='8.4',line='وابدأ بـ <span class="gold">14 يوم</span><br>مجانًا 🎁'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv19_1500',D=12,preset='dm',seed=1915,bpm=122,trans='2.8,5.6,8.4',pat=4),media=['sv19_1500.mp4'],idea='قصة فيديو أسعار: عدّاد 200 ج شهري ← 2000 ج سنوي + 14 يوم مجانًا')

sflow('s19_2030','''
<div style="font-size:120px">🤖</div>
<div style="font-size:66px;font-weight:900;line-height:1.4">اطلب من الذكاء الاصطناعي<br><span class="gold">يبسّط كلامك لموكلك</span></div>
<div class="glass" style="padding:34px 40px;margin:0 20px;text-align:right;font-size:46px;font-weight:700;line-height:1.6;border-color:rgba(217,178,95,.6)"><span class="small" style="font-size:32px">اكتب مثلًا:</span><br>«بسّط الفقرة دي لشخص مش دارس قانون»</div>
<div style="font-size:50px;font-weight:800;line-height:1.6">✅ وإنت راجع إن المعنى<br>ماتغيّرش</div>''',gap=48)
add(date=D,time='20:30',kind='story',media=['s19_2030.png'],idea='قصة ذكاء اصطناعي: اطلب منه يبسّط كلامك لموكلك… وراجع إن المعنى ماتغيّرش')

# ======================= FRI 2026-11-20 =======================
D='2026-11-20'
video('v20_1000','''
<div class="sc" data-a="0" data-b="3.2">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🤍</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:20px">جمعة سعيدة<br><span class="gold">يا متر</span></div>
</div>
<div class="sc" data-a="3" data-b="8.4">
 <div data-fx="fade" data-at=".1" style="font-size:110px">✨</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:80px">ثقة موكلك…</div>
 <div class="h1" data-fx="rise" data-at="1.4" style="font-size:80px;margin-top:10px">بتتبني من<br><span class="gold">التفاصيل الصغيرة</span></div>
</div>
<div class="sc" data-a="8.2" data-b="12.4">
 <div class="col" style="gap:24px;width:780px">
  '''+li('⏱️','رد في وقته',at='.2',ts=46)+li('📅','ميعاد محترم',at='.8',ts=46)+li('📁','ورقة في مكانها',at='1.4',ts=46,extra='border-color:rgba(217,178,95,.7)')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='شاركها مع زميل 🤝'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v20_1000',D=16,preset='c',seed=2010,bpm=76,trans='3,8.2,12.2',pat=3),media=['v20_1000.mp4'],title='ثقة موكلك | ميزان برو',
 text='«ثقة موكلك… بتتبني من التفاصيل الصغيرة» 🤍\n\n⏱️ رد في وقته\n📅 ميعاد محترم\n📁 ورقة في مكانها\n\nجمعة سعيدة يا متر ✨\nشاركها مع زميل 👇\nmezan.pro'+TAGS,
 idea='فيديو اقتباس للجمعة: «ثقة موكلك… بتتبني من التفاصيل الصغيرة»')

post('p20_1400','''
<div style="position:absolute;top:170px;right:66px;width:420px">
 <div style="height:60px;border-radius:24px 24px 0 0;background:linear-gradient(160deg,var(--gold2),var(--gold) 60%,#b88d3a);display:flex;justify-content:space-around;align-items:center"><i style="width:22px;height:22px;border-radius:50%;background:#0b1530"></i><i style="width:22px;height:22px;border-radius:50%;background:#0b1530"></i><i style="width:22px;height:22px;border-radius:50%;background:#0b1530"></i></div>
 <div class="paper center" style="border-radius:0 0 24px 24px;padding:20px 0 30px"><div style="font-family:CairoL;font-weight:700;font-size:200px;line-height:1;color:#8a6a2c">40</div><div style="font-size:52px;font-weight:900">يوم</div></div>
</div>
<div style="position:absolute;top:200px;left:66px;width:500px">
 <div class="h1" style="font-size:62px">التماس<br><span class="gold">إعادة النظر</span> ⚖️</div>
 <div class="lead" style="font-size:30px;margin-top:20px">طبقًا للمادة 242 من قانون المرافعات المدنية والتجارية</div>
</div>
<div class="box glass center" style="top:640px;padding:26px 36px;font-size:40px;font-weight:800">«ميعاد الالتماس <span class="gold">أربعون يومًا</span>»</div>
<div class="box center" style="top:800px;font-size:29px;font-weight:800;line-height:1.6">📌 وفي بعض حالات الالتماس الميعاد مش بيبدأ من تاريخ الحكم<br>راجع نص المادة… وسجّل الميعاد في ملف القضية</div>''',pill='معلومة إجرائية 📚',foot='احفظ البوست 🔖')
add(date=D,time='14:00',kind='post',media=['p20_1400.png'],
 text='معلومة إجرائية ⚖️ التماس إعادة النظر\n\n⏳ 40 يوم\nطبقًا للمادة 242 من قانون المرافعات المدنية والتجارية: «ميعاد الالتماس أربعون يومًا».\n\n📌 وفي بعض حالات الالتماس، الميعاد مش بيبدأ من تاريخ الحكم… فراجع نص المادة كويس، وسجّل الميعاد في ملف القضية من أول يوم.\n\nاحفظ البوست 🔖\nmezan.pro'+TAGS,
 idea='معلومة إجرائية: ميعاد التماس إعادة النظر 40 يوم (م.242 مرافعات) وبدايته بتختلف حسب الحالة')

thumbs=''.join(f'<div style="aspect-ratio:1;border-radius:10px;background:rgba(255,255,255,{.08+.04*(i%3)});display:grid;place-items:center;font-size:34px">📄</div>' for i in range(12))
post('p20_1900_1','''
<div style="position:absolute;top:170px;left:90px;width:360px;height:700px;border-radius:50px;border:6px solid rgba(217,178,95,.6);background:#0b1530;padding:40px 22px;transform:rotate(-5deg)">
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">'''+thumbs+'''</div>
 <div class="btn" style="position:absolute;bottom:40px;left:50%;transform:translateX(-50%);font-size:40px;padding:10px 30px">+30</div>
</div>
<div style="position:absolute;top:250px;right:66px;width:520px">
 <div style="font-size:100px">📱😅</div>
 <div class="h1" style="font-size:62px;margin-top:10px">موكلك بعتلك<br><span class="gold">30 صورة مستندات</span><br>على الواتساب؟</div>
</div>''',pill='مشكلة وحلها 💡',foot='اسحب ← للحل',dots=(1,3))
post('p20_1900_2','''
<div class="box" style="top:170px"><div class="h2" style="font-size:56px">أول حاجة 👇</div></div>
<div class="box col" style="top:290px;gap:28px">
 <div class="glass li" style="padding:34px 36px"><div class="num" style="width:76px;height:76px;font-size:40px">1</div><div><div class="t" style="font-size:42px">متسيبهاش في الشات</div><div class="d" style="font-size:28px">هتضيع وسط الرسايل 💬</div></div></div>
 <div class="glass li" style="padding:34px 36px;border-color:rgba(217,178,95,.7)"><div class="num" style="width:76px;height:76px;font-size:40px">2</div><div><div class="t" style="font-size:42px">نزّلها في نفس اليوم</div><div class="d" style="font-size:28px">في المكان الخاص بالقضية 📁</div></div></div>
</div>
<div class="box center" style="top:760px;font-size:34px;font-weight:800">النهارده سهلة… <span class="gold">بعد شهر صعبة</span></div>''',foot='اسحب ←',dots=(2,3))
post('p20_1900_3','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:150px"></div>
<div class="center" style="position:absolute;top:170px;left:66px;right:66px">
 <img src="../logo.svg" width="130">
 <div class="h1" style="font-size:60px;margin-top:16px">وفي <span class="gold">ميزان برو</span></div>
</div>
<div class="box col" style="top:430px;gap:22px">
 '''+li('🤖','أوراق ومستندات القضية تتلخّص','بالذكاء الاصطناعي',ts=40)+li('🔗','والملخص يتربط بملف القضية','تلاقيه وقت ما تحتاجه',ts=40)+'''
</div>
<div class="box center" style="top:820px"><span class="btn" style="font-size:36px">mezan.pro</span></div>''',foot='نظام إدارة متكامل لمكاتب المحاماة',dots=(3,3))
add(date=D,time='19:00',kind='post',media=['p20_1900_1.png','p20_1900_2.png','p20_1900_3.png'],
 text='موكلك بعتلك 30 صورة مستندات على الواتساب؟ 📱😅\n\n1️⃣ متسيبهاش في الشات… هتضيع وسط الرسايل\n2️⃣ نزّلها في نفس اليوم في المكان الخاص بالقضية\n3️⃣ وفي ميزان برو: أوراق ومستندات القضية بتتلخّص بالذكاء الاصطناعي، والملخص بيتربط بملف القضية 🔗\n\nاسحب الصور ←\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='كاروسيل 3 صور مشكلة وحلها: موكل بعت 30 صورة مستندات على الواتساب ← نزّلها في يومها + ملخص مربوط بملف القضية')

sflow('s20_1100','''
<div style="font-size:140px">🤍</div>
<div style="font-size:66px;font-weight:900;line-height:1.4">في آخر القضية…<br>قول لموكلك</div>
<div class="glass" style="padding:50px 40px;margin:0 40px;border-color:rgba(217,178,95,.7);font-size:84px;font-weight:900" ><span class="gold">«شكرًا على ثقتك»</span></div>
<div style="font-size:56px;font-weight:800;line-height:1.5">كلمة صغيرة…<br>بتفضل في ذاكرته</div>''',gap=56)
add(date=D,time='11:00',kind='story',media=['s20_1100.png'],idea='قصة تعامل مع الموكلين: «شكرًا على ثقتك» في آخر القضية')

video('sv20_1500','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🗓️</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">قبل الأسبوع<br>الجديد…<br><span class="gold">3 أسئلة</span></div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:30px">
  '''+opt(1,'إيه أهم جلسة؟ ⚖️','.3')+opt(2,'أنهي مذكرة لازم تخلص؟ ✍️','1')+opt(3,'مين محتاج أكلّمه؟ 📞','1.7')+'''
 </div>
</div>
'''+END_S.format(a='8.4',line='أسبوعك يبدأ<br><span class="gold">واضح</span> ✨'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv20_1500',D=12,preset='bm',seed=2015,bpm=110,trans='3.2,8.4',pat=0),media=['sv20_1500.mp4'],idea='قصة فيديو تنظيم: قبل الأسبوع الجديد 3 أسئلة (أهم جلسة/مذكرة/مكالمة)')

def g2(ic,t):
    return f'<div class="glass center" style="padding:36px 10px"><div style="font-size:96px">{ic}</div><div style="font-size:46px;font-weight:900;margin-top:10px;line-height:1.3">{t}</div></div>'
sflow('s20_2030','''
<div style="font-size:66px;font-weight:900;line-height:1.4">إيه أكتر حاجة<br>عايز <span class="gold">تنظّمها</span><br>في مكتبك؟</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">'''+g2('📄','الأوراق')+g2('⏰','وقتي')+g2('📞','التواصل<br>مع الموكلين')+g2('🗄️','الأرشيف')+'''</div>
<div style="font-size:46px;font-weight:800;color:var(--gold2)">ابعتلنا ردّك 📩</div>''',gap=50)
add(date=D,time='20:30',kind='story',media=['s20_2030.png'],idea='قصة سؤال: إيه أكتر حاجة عايز تنظّمها في مكتبك؟ (الأوراق/وقتي/التواصل/الأرشيف)')

json.dump(M,open('mw4b.json','w'),ensure_ascii=False,indent=1);print(len(M))
