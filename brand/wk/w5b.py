from w4c import *

# ======================= WED 2026-11-25 =======================
D='2026-11-25'
video('v25_1000','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:150px" data-fx="drop" data-at=".1">📱🌙</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:72px;margin-top:20px">موكل بعتلك رسالة<br>الساعة <span class="gold">11 بالليل</span>…</div>
</div>
<div class="sc" data-a="3.4" data-b="12.4">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:66px;margin-bottom:34px">بتعمل إيه؟ 🤔</div>
 <div class="col" style="width:880px;gap:22px">
  '''+opt('أ','أرد فورًا','.5')+opt('ب','أرد الصبح','1.1')+opt('ج','حسب الرسالة','1.7')+opt('د','عندي رقم للشغل بس 😅','2.3')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='اكتب حرفك في الكومنتات 👇'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v25_1000',D=16,preset='fm',seed=2510,bpm=102,trans='3.4,12.2',pat=0),media=['v25_1000.mp4'],title='رسالة الساعة 11 بالليل | ميزان برو',
 text='سؤال للمحامين 💬\nموكل بعتلك رسالة الساعة 11 بالليل… بتعمل إيه؟ 📱🌙\n\nأ) أرد فورًا\nب) أرد الصبح\nج) حسب الرسالة\nد) عندي رقم للشغل بس 😅\n\nاكتب حرفك في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن سؤال تفاعلي: موكل بعت رسالة الساعة 11 بالليل… بتعمل إيه؟ (أ/ب/ج/د)')

def sit(ic,t,d):
    return f'<div class="glass" style="padding:28px 24px;text-align:center"><div style="font-size:74px">{ic}</div><div style="font-size:34px;font-weight:900;margin-top:10px;line-height:1.35">{t}</div><div style="font-size:25px;color:var(--mute);margin-top:10px;line-height:1.5">{d}</div></div>'
post('p25_1400','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:54px">«الملخص مربوط بملف القضية»<br><span class="gold">يعني إيه عمليًا؟</span> 🔗</div></div>
<div class="box" style="top:400px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px">
 '''+sit('📅','قبل الجلسة','تفتح ملف القضية وتبدأ من الملخص')+sit('📞','موكل بيسأل','تفتح ملفه وترد وانت فاكر')+sit('🤝','زميل هيستلم','الملخص مستنيه في ملف القضية')+'''
</div>
<div class="box center" style="top:830px;font-size:30px;font-weight:800">ميزان برو: تلخيص أوراق القضايا <span class="gold">بالذكاء الاصطناعي</span> 🤖</div>''',pill='من مزايا النظام ✨')
add(date=D,time='14:00',kind='post',media=['p25_1400.png'],
 text='«الملخص مربوط بملف القضية»… يعني إيه عمليًا؟ 🔗\n\n📅 قبل الجلسة: تفتح ملف القضية وتبدأ من الملخص\n📞 موكل بيسأل: تفتح ملفه وترد وانت فاكر\n🤝 زميل هيستلم القضية: الملخص مستنيه في ملفها\n\nميزان برو بيلخّص أوراق ومستندات القضايا بالذكاء الاصطناعي، ويربط الملخص بملف القضية.\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='ميزة: يعني إيه الملخص مربوط بملف القضية عمليًا؟ 3 مواقف (قبل الجلسة · موكل بيسأل · زميل هيستلم)')

def flowc(ic,t,last=False):
    arr='' if last else '<div style="font-size:50px;color:var(--gold)">←</div>'
    return f'<div class="glass center" style="width:250px;height:230px;padding:30px 10px;display:flex;flex-direction:column;justify-content:center"><div style="font-size:70px">{ic}</div><div style="font-size:34px;font-weight:900;margin-top:8px;line-height:1.3">{t}</div></div>{arr}'
post('p25_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:58px">رسالة أو إيميل جديد؟<br>افتحه <span class="gold">مرة واحدة بس</span> 📩</div></div>
<div class="box" style="top:420px;display:flex;align-items:center;justify-content:center;gap:16px">
 '''+flowc('👀','اقرا')+flowc('🧭','قرّر')+flowc('✅','نفّذ أو<br>حدّد ميعاد',True)+'''
</div>
<div class="box glass center" style="top:740px;padding:26px 30px;font-size:32px;font-weight:800;line-height:1.6">بدل ما تفتح نفس الرسالة 5 مرات… <span class="gold">وكل مرة تقول «بعدين»</span> 😅</div>''',pill='نصيحة تنظيم ⏱️')
add(date=D,time='19:00',kind='post',media=['p25_1900.png'],
 text='رسالة أو إيميل جديد؟ افتحه مرة واحدة بس 📩\n\n👀 اقرا\n🧭 قرّر\n✅ نفّذ… أو حدّد له ميعاد\n\nبدل ما تفتح نفس الرسالة 5 مرات وكل مرة تقول «بعدين» 😅\nجرّبها بكرة وقولنا 👇\nmezan.pro'+TAGS,
 idea='نصيحة تنظيم: قاعدة «افتح الرسالة مرة واحدة» — اقرا · قرّر · نفّذ أو حدّد ميعاد')

def bub(t,me=False):
    if me: return f'<div style="align-self:flex-end;max-width:720px;padding:28px 34px;border-radius:36px 36px 10px 36px;background:linear-gradient(160deg,var(--gold2),var(--gold));color:var(--navy);font-size:42px;font-weight:800;line-height:1.5;text-align:right">{t}</div>'
    return f'<div style="align-self:flex-start;max-width:720px;padding:28px 34px;border-radius:36px 36px 36px 10px;background:#f4f1e8;color:#1b2440;font-size:42px;font-weight:800;line-height:1.5;text-align:right">{t}</div>'
sflow('s25_1100','''
<div style="font-size:60px;font-weight:900;line-height:1.4">موكلك سألك:</div>
'''+bub('فين الورقة اللي ادتهالك الشهر اللي فات؟')+'''
<div class="tag" style="align-self:center;font-size:34px;background:rgba(252,165,165,.15);color:#fca5a5">قبل 😓</div>
'''+bub('هدوّر عليها وأرد عليك 🙏',True)+'''
<div class="tag" style="align-self:center;font-size:34px">بعد ✨ مع ميزان برو</div>
'''+bub('معايا 👍 في ملف قضيتك',True),gap=30)
add(date=D,time='11:00',kind='story',media=['s25_1100.png'],idea='قصة قبل/بعد بشكل شات: «فين الورقة اللي ادتهالك؟» — هدوّر وأرد ضد معايا في ملف قضيتك')

video('sv25_1500','''
<div class="sc" data-a="0" data-b="4">
 <div style="font-size:150px" data-fx="drop" data-at=".1">📚</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">مستند <span class="gold">80 صفحة</span><br>وصلك النهارده؟</div>
</div>
<div class="sc" data-a="3.8" data-b="8.6">
 <div class="col" style="width:100%;gap:30px">
  <div class="glass" data-fx="rise" data-at=".2" style="padding:36px;font-size:52px;font-weight:800">🤖 يتلخّص بالذكاء الاصطناعي</div>
  <div style="font-size:70px;color:var(--gold)" data-fx="pop" data-at=".8">↓</div>
  <div class="glass" data-fx="rise" data-at="1.2" style="padding:36px;font-size:52px;font-weight:800;border-color:rgba(217,178,95,.7)">🔗 والملخص في <span class="gold">ملف القضية</span></div>
 </div>
</div>
'''+END_S.format(a='8.4',line='ابدأ من الملخص…<br><span class="gold">وارجع للأصل</span>'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv25_1500',D=12,preset='c',seed=2515,bpm=118,trans='3.8,8.4',pat=3),media=['sv25_1500.mp4'],idea='قصة فيديو مشكلة وحلها: مستند 80 صفحة وصلك النهارده؟ ملخص بالذكاء الاصطناعي في ملف القضية')

sflow('s25_2030','''
<div style="font-size:200px;line-height:.8;font-family:Messiri" class="gold">“</div>
<div style="font-size:74px;font-weight:900;line-height:1.55">مش لازم تبقى<br>أسرع محامي…<br>كفاية تبقى<br><span class="gold">الأكتر استعدادًا</span></div>
<div class="line" style="width:420px;margin:0 auto"></div>''',gap=50)
add(date=D,time='20:30',kind='story',media=['s25_2030.png'],idea='قصة اقتباس: «مش لازم تبقى أسرع محامي… كفاية تبقى الأكتر استعدادًا»')

# ======================= THU 2026-11-26 =======================
D='2026-11-26'
def qcard(n,q,why):
    return f'<div class="glass" style="display:flex;gap:26px;align-items:center;padding:28px 34px"><div class="gold" style="font-family:CairoL;font-weight:700;font-size:96px;line-height:1;width:80px;text-align:center">{n}</div><div><div style="font-size:40px;font-weight:900">{q}</div><div style="font-size:27px;color:var(--mute);margin-top:6px">{why}</div></div></div>'
post('p26_1000','''
<div class="box" style="top:150px"><div class="h1" style="font-size:56px">في آخر أي مقابلة مع موكل…<br>اسأله <span class="gold">3 أسئلة</span> 🤝</div></div>
<div class="box col" style="top:360px;gap:22px">
 '''+qcard(1,'«الخطوة الجاية واضحة؟»','عشان ميمشيش وهو مش فاهم')+qcard(2,'«عندك أي سؤال؟»','سؤال النهارده أحسن من قلق بكرة')+qcard(3,'«أوصلك إزاي لو جدّ جديد؟»','تليفون، رسالة، إيميل')+'''
</div>''',pill='تعامل مع الموكلين 🤝')
add(date=D,time='10:00',kind='post',media=['p26_1000.png'],
 text='في آخر أي مقابلة مع موكل… اسأله 3 أسئلة 🤝\n\n1️⃣ «الخطوة الجاية واضحة؟» عشان ميمشيش وهو مش فاهم\n2️⃣ «عندك أي سؤال؟» سؤال النهارده أحسن من قلق بكرة\n3️⃣ «أوصلك إزاي لو جدّ جديد؟» تليفون، رسالة، ولا إيميل\n\nدقيقة واحدة… بتفرق في ثقته فيك 🤍\nmezan.pro'+TAGS,
 idea='نصيحة تعامل مع الموكلين: 3 أسئلة في آخر كل مقابلة (الخطوة واضحة؟ عندك سؤال؟ أوصلك إزاي؟)')

def qa(q,a,at):
    return f'''<div class="col" style="gap:14px;width:900px" data-fx="rise" data-at="{at}"><div class="glass" style="padding:20px 30px;font-size:40px;font-weight:800;text-align:right">❓ {q}</div><div class="glass" style="padding:20px 30px;font-size:44px;font-weight:900;text-align:left;border-color:rgba(217,178,95,.7)">{a}</div></div>'''
video('v26_1400','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🏷️</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:80px;margin-top:20px">ميزان برو<br><span class="gold">في 3 أسئلة</span></div>
</div>
<div class="sc" data-a="3.2" data-b="12.4">
 <div class="col" style="gap:34px">
  '''+qa('بكام؟','<span class="gold">200 ج</span> شهري · <span class="gold">2000 ج</span> سنوي','.3')+'''
  '''+qa('فيه تجربة؟','<span class="gold">14 يوم</span> مجانًا 🎁','2.6')+'''
  '''+qa('أبدأ منين؟','<span class="url" style="color:var(--gold2)">mezan.pro</span> 👈','4.9')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='جرّب… وقرّر بنفسك'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v26_1400',D=16,preset='a',seed=2614,bpm=120,trans='3.2,12.2',pat=4),media=['v26_1400.mp4'],title='ميزان برو في 3 أسئلة | ميزان برو',
 text='ميزان برو في 3 أسئلة 🏷️\n\n❓ بكام؟\n200 ج شهري · أو 2000 ج سنوي\n\n❓ فيه تجربة؟\n14 يوم مجانًا 🎁\n\n❓ أبدأ منين؟\nmezan.pro 👈\n\nجرّب… وقرّر بنفسك'+TAGS,
 idea='فيديو موشن أسعار بشكل سؤال وجواب: بكام؟ فيه تجربة؟ أبدأ منين؟')

post('p26_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:56px">قبل ما تستخدم أي أداة<br>ذكاء اصطناعي <span class="gold">لشغلك</span> 🔒</div></div>
<div class="box" style="top:380px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
 '''+''.join(f'<div class="glass" style="padding:28px 30px"><div style="font-size:60px">{a}</div><div style="font-size:34px;font-weight:900;margin-top:8px;line-height:1.4">{b}</div><div style="font-size:25px;color:var(--mute);margin-top:6px;line-height:1.5">{c}</div></div>' for a,b,c in [('⚙️','افتح إعدادات الخصوصية','واعرف الأداة بتعمل إيه بمحادثاتك'),('💾','اعرف المحادثات بتتحفظ؟','وفين ولمدة قد إيه'),('🧹','امسح اللي مش محتاجه','خصوصًا لو فيه تفاصيل شغل'),('🙅','وفي كل الأحوال','متكتبش بيانات موكلينك')])+'''
</div>''',pill='ذكاء اصطناعي بأمان 🤖')
add(date=D,time='19:00',kind='post',media=['p26_1900.png'],
 text='قبل ما تستخدم أي أداة ذكاء اصطناعي لشغلك 🔒\n\n⚙️ افتح إعدادات الخصوصية واعرف الأداة بتعمل إيه بمحادثاتك\n💾 اعرف المحادثات بتتحفظ؟ وفين؟ ولمدة قد إيه؟\n🧹 امسح اللي مش محتاجه، خصوصًا لو فيه تفاصيل شغل\n🙅 وفي كل الأحوال: متكتبش بيانات موكلينك\n\nسرّ موكلك أمانة 🤍\nmezan.pro'+TAGS,
 idea='نصيحة ذكاء اصطناعي بأمان: راجع إعدادات الخصوصية وحفظ المحادثات قبل ما تستخدم الأداة')

video('sv26_1100','''
<div class="sc" data-a="0" data-b="3.8">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🔔</div>
 <div style="font-size:80px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">بترد على الرسايل<br><span class="gold">طول اليوم؟</span></div>
</div>
<div class="sc" data-a="3.6" data-b="8.6">
 <div style="font-size:70px;font-weight:900;line-height:1.4" data-fx="rise" data-at=".1">خصّص <span class="gold">وقتين</span> بس 👇</div>
 <div style="display:flex;gap:30px;margin-top:50px">
  <div class="glass" data-fx="pop" data-at=".6" style="padding:40px 46px;font-size:56px;font-weight:900">☀️<br>الضهر</div>
  <div class="glass" data-fx="pop" data-at="1.1" style="padding:40px 46px;font-size:56px;font-weight:900">🌇<br>آخر اليوم</div>
 </div>
</div>
'''+END_S.format(a='8.4',line='وباقي اليوم…<br><span class="gold">للتركيز</span>'),D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv26_1100',D=12,preset='em',seed=2611,bpm=108,trans='3.6,8.4',pat=2),media=['sv26_1100.mp4'],idea='قصة فيديو تنظيم وقت: رد على الرسايل في وقتين ثابتين بدل طول اليوم')

sflow('s26_1500','''
<div style="font-size:66px;font-weight:900;line-height:1.4">المذكرة…<br>بتكتبها <span class="gold">إزاي؟</span> ✍️</div>
<div class="glass" style="padding:40px"><div style="font-size:100px">⚡</div><div style="font-size:56px;font-weight:900;margin-top:6px">مرة واحدة</div></div>
<div class="glass" style="padding:40px"><div style="font-size:100px">🧱</div><div style="font-size:56px;font-weight:900;margin-top:6px">على مراحل</div></div>''',gap=40)
add(date=D,time='15:00',kind='story',media=['s26_1500.png'],idea='قصة سؤال: المذكرة بتكتبها مرة واحدة ولا على مراحل؟')

sflow('s26_2030','''
<div class="tag" style="font-size:36px;align-self:center">من مزايا ميزان برو ✨</div>
<div class="glass" style="padding:34px;font-size:54px;font-weight:900">📄 أوراق ومستندات القضية</div>
<div style="font-size:70px;color:var(--gold);line-height:1">↓</div>
<div class="glass" style="padding:34px;font-size:54px;font-weight:900">🤖 ملخص بالذكاء الاصطناعي</div>
<div style="font-size:70px;color:var(--gold);line-height:1">↓</div>
<div class="glass" style="padding:34px;font-size:54px;font-weight:900;border-color:rgba(217,178,95,.8)">📁 مربوط <span class="gold">بملف القضية</span></div>''',gap=26)
add(date=D,time='20:30',kind='story',media=['s26_2030.png'],idea='قصة ميزة بأسهم: أوراق القضية ← ملخص بالذكاء الاصطناعي ← مربوط بملف القضية')

# ======================= FRI 2026-11-27 =======================
D='2026-11-27'
video('v27_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="pop" data-at=".1">🤍</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:80px;margin-top:20px">جمعة مباركة<br><span class="gold">يا متر</span></div>
</div>
<div class="sc" data-a="3.2" data-b="12.4">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:60px;margin-bottom:40px">3 حاجات المحامي الشاطر<br><span class="gold">بيحافظ عليها</span> 👇</div>
 <div style="display:flex;gap:26px">
  <div class="glass" data-fx="pop" data-at=".8" style="width:270px;padding:36px 10px"><div style="font-size:90px">⏰</div><div style="font-size:52px;font-weight:900">وقته</div></div>
  <div class="glass" data-fx="pop" data-at="1.8" style="width:270px;padding:36px 10px"><div style="font-size:90px">🤝</div><div style="font-size:52px;font-weight:900">كلمته</div></div>
  <div class="glass" data-fx="pop" data-at="2.8" style="width:270px;padding:36px 10px;border-color:rgba(217,178,95,.8)"><div style="font-size:90px">📁</div><div style="font-size:52px;font-weight:900">ملفه</div></div>
 </div>
</div>
'''+END_P.format(a='12.2',line='وإحنا معاك في الأخيرة 😉'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v27_1000',D=16,preset='f',seed=2710,bpm=84,trans='3.2,12.2',pat=1),media=['v27_1000.mp4'],title='جمعة مباركة يا متر | ميزان برو',
 text='جمعة مباركة يا متر 🤍\n\n3 حاجات المحامي الشاطر بيحافظ عليها:\n⏰ وقته\n🤝 كلمته\n📁 ملفه\n\nوإحنا معاك في الأخيرة 😉\nشاركها مع زميل 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن جملة تحفيزية للجمعة: 3 حاجات المحامي بيحافظ عليها (وقته · كلمته · ملفه)')

post('p27_1400','''
<div class="box" style="top:150px"><div class="h1" style="font-size:56px">قضية جديدة شبه قضية قديمة…<br>والمذكرة القديمة <span class="gold">مش لاقيها</span> 🤦</div></div>
<div class="box" style="top:400px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
 <div class="glass" style="padding:30px;border-color:rgba(252,165,165,.4)"><div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5;font-size:30px">المشكلة</div><div style="font-size:32px;font-weight:800;line-height:1.7;margin-top:16px">فلاشة؟ إيميل؟<br>كمبيوتر المكتب القديم؟<br>وفي الآخر تكتبها من الأول ✍️</div></div>
 <div class="glass" style="padding:30px;border-color:rgba(217,178,95,.75)"><div class="tag" style="font-size:30px">الحل ✨</div><div style="font-size:32px;font-weight:800;line-height:1.7;margin-top:16px">كل مذكرة في<br><span class="gold">ملف قضيتها</span><br>على نظام واحد لمكتبك</div></div>
</div>
<div class="box center" style="top:820px;font-size:30px;font-weight:800">ميزان برو: نظام إدارة متكامل لمكاتب المحاماة 🖥️</div>''',pill='مشكلة وحلها 💡')
add(date=D,time='14:00',kind='post',media=['p27_1400.png'],
 text='قضية جديدة شبه قضية قديمة… والمذكرة القديمة مش لاقيها؟ 🤦\nفلاشة؟ إيميل؟ كمبيوتر المكتب القديم؟ وفي الآخر تكتبها من الأول ✍️\n\nالحل ✨\nكل مذكرة تبقى في ملف قضيتها، على نظام واحد لمكتبك كله.\n\nميزان برو: نظام إدارة متكامل لمكاتب المحاماة.\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='مشكلة وحلها: قضية شبه قضية قديمة والمذكرة القديمة مش لاقيها ← كل مذكرة في ملف قضيتها على نظام واحد')

post('p27_1900','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:150px"></div>
<div class="box" style="top:170px">
 <div style="display:flex;align-items:baseline;gap:24px"><span class="gold" style="font-family:Messiri;font-size:96px">ميزان برو</span><span style="font-size:34px;color:var(--mute);font-weight:700">(اسم)</span></div>
 <div class="line" style="margin:20px 0 30px"></div>
 <div style="font-size:38px;font-weight:800;line-height:1.9">
  <span class="gold">١.</span> نظام إدارة متكامل (ERP) لمكاتب المحاماة.<br>
  <span class="gold">٢.</span> بيلخّص أوراق ومستندات القضايا بالذكاء الاصطناعي، ويربط الملخص بملف القضية.<br>
  <span class="gold">٣.</span> حماية البيانات وسريتها أولوية فيه.
 </div>
 <div style="font-size:30px;color:var(--mute);margin-top:26px"><b style="color:var(--ink)">مرادفات:</b> مكتب مرتّب · ملف لكل قضية · راحة بال 😉</div>
</div>''',pill='تعريف 📖')
add(date=D,time='19:00',kind='post',media=['p27_1900.png'],
 text='ميزان برو (اسم) 📖\n\n1️⃣ نظام إدارة متكامل (ERP) لمكاتب المحاماة\n2️⃣ بيلخّص أوراق ومستندات القضايا بالذكاء الاصطناعي، ويربط الملخص بملف القضية\n3️⃣ حماية البيانات وسريتها أولوية فيه\n\nجرّبه 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='ميزة بشكل تعريف قاموس: «ميزان برو (اسم)» — ERP لمكاتب المحاماة + تلخيص مربوط بالملف + سرية البيانات')

sflow('s27_1100','''
<div style="font-size:160px">🕌🤍</div>
<div style="font-size:100px;font-weight:900;line-height:1.4">جمعة مباركة<br><span class="gold">يا متر</span></div>
<div style="font-size:50px;font-weight:700;color:var(--mute);line-height:1.6">ريّح دماغك النهارده…<br>وارجع بطاقة جديدة ✨</div>''',gap=60)
add(date=D,time='11:00',kind='story',media=['s27_1100.png'],idea='قصة تهنئة: جمعة مباركة يا متر… ريّح دماغك وارجع بطاقة جديدة')

video('sv27_1500','''
<div class="sc" data-a="0" data-b="4.6">
 <div style="font-size:76px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">جرّب ميزان برو</div>
 <div class="gold" style="font-family:CairoL;font-weight:700;font-size:340px;line-height:1.1;margin-top:20px" data-fx="count" data-to="14" data-at=".5" data-d="1.8">0</div>
 <div style="font-size:80px;font-weight:900" data-fx="rise" data-at="1.2">يوم <span class="gold">مجانًا</span> 🎁</div>
</div>
<div class="sc" data-a="4.4" data-b="8.6">
 <div style="font-size:64px;font-weight:900" data-fx="rise" data-at=".1">وبعدها اختار 👇</div>
 <div class="col" style="width:100%;gap:30px;margin-top:40px">
  <div class="glass" data-fx="right" data-at=".5" style="padding:36px;font-size:58px;font-weight:900">شهري · <span class="gold">200 ج</span></div>
  <div class="glass" data-fx="right" data-at="1.1" style="padding:36px;font-size:58px;font-weight:900">سنوي · <span class="gold">2000 ج</span></div>
 </div>
</div>
'''+END_S.format(a='8.4',line='ابدأ تجربتك<br><span class="gold">النهارده</span>'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv27_1500',D=12,preset='g',seed=2715,bpm=128,trans='4.4,8.4',pat=0),media=['sv27_1500.mp4'],idea='قصة فيديو أسعار: عدّاد لحد 14 يوم مجانًا ← شهري 200 ج / سنوي 2000 ج')

sflow('s27_2030','''
<div style="font-size:64px;font-weight:900;line-height:1.4">الأسبوع الجاي<br>هتبدأه <span class="gold">بإيه؟</span> 🚀</div>
'''+''.join(f'<div class="glass" style="padding:36px;font-size:54px;font-weight:900">{x}</div>' for x in ['📚 ملف تقيل','✍️ مذكرة','🗂️ ترتيب المكتب'])+'''
<div style="font-size:42px;font-weight:700;color:var(--gold2)">ابعتلنا إجابتك 📩</div>''',gap=40)
add(date=D,time='20:30',kind='story',media=['s27_2030.png'],idea='قصة سؤال: الأسبوع الجاي هتبدأه بإيه؟ (ملف تقيل / مذكرة / ترتيب المكتب)')

json.dump(M,open('mw5b.json','w'),ensure_ascii=False,indent=1);print(len(M))
