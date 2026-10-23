from lib import *
import json
M=[];D8='2026-10-25'
TAGS='\n\n#ميزان_برو #محاماة'
# ---------- POST 10:00 — carousel ORG: waiting-for list
post('p25_1000_1','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:200px"></div>
<div class="center" style="position:absolute;top:230px;left:60px;right:60px">
 <div style="font-size:120px">⏳</div>
 <div class="h1" style="font-size:84px;margin-top:10px">عندك قايمة<br><span class="gold">«مستني رد»؟</span></div>
 <div class="lead" style="margin-top:26px">أكتر حاجة بتتأخر في المكتب…<br>مش اللي في إيدك، اللي <span class="gold">مستنيها من حد تاني</span></div>
</div>''',pill='نصيحة تنظيم 🗂️',foot='اسحب ← خطوتين بس',dots=(1,3))
post('p25_1000_2','''
<div class="box" style="top:160px"><div class="tag" style="font-size:26px">الخطوة 1</div><div class="h2" style="margin-top:14px">اكتب أي حاجة <span class="gold">مستنيها</span> من حد</div></div>
<div class="box" style="top:400px">
 <div class="glass" style="padding:10px 26px">
  <div style="display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:0;font-size:26px">
   <div style="padding:18px 6px;color:var(--gold2);font-weight:800;border-bottom:1px solid rgba(255,255,255,.12)">مستني إيه؟</div><div style="padding:18px 6px;color:var(--gold2);font-weight:800;border-bottom:1px solid rgba(255,255,255,.12)">من مين؟</div><div style="padding:18px 6px;color:var(--gold2);font-weight:800;border-bottom:1px solid rgba(255,255,255,.12)">من إمتى؟</div>
   <div style="padding:20px 6px;font-weight:700;border-bottom:1px solid rgba(255,255,255,.07)">📄 صورة العقد الأصلي</div><div style="padding:20px 6px;border-bottom:1px solid rgba(255,255,255,.07)">الموكل</div><div style="padding:20px 6px;border-bottom:1px solid rgba(255,255,255,.07)">من 3 أيام</div>
   <div style="padding:20px 6px;font-weight:700;border-bottom:1px solid rgba(255,255,255,.07)">✉️ رد على عرض الصلح</div><div style="padding:20px 6px;border-bottom:1px solid rgba(255,255,255,.07)">الطرف التاني</div><div style="padding:20px 6px;border-bottom:1px solid rgba(255,255,255,.07)">من أسبوع</div>
   <div style="padding:20px 6px;font-weight:700">🧾 إيصالات السداد</div><div style="padding:20px 6px">الموكل</div><div style="padding:20px 6px">من يومين</div>
  </div>
 </div>
 <div class="lead" style="margin-top:30px;font-size:28px">ورقة، ملف على الكمبيوتر… المهم تكون <span class="gold">مكتوبة</span> مش في دماغك.</div>
</div>''',foot='اسحب ←',dots=(2,3))
post('p25_1000_3','''
<div class="box" style="top:160px"><div class="tag" style="font-size:26px">الخطوة 2</div><div class="h2" style="margin-top:14px">راجعها كل يوم الصبح<br>في <span class="gold">دقيقتين</span></div></div>
<div class="box col" style="top:450px;gap:20px">
 <div class="glass li" style="padding:22px 28px"><div class="ic">📞</div><div><div class="t">اتأخرت؟ تابع وفكّر صاحبها</div></div></div>
 <div class="glass li" style="padding:22px 28px"><div class="ic">✅</div><div><div class="t">وصلت؟ اشطبها من القايمة</div></div></div>
 <div class="glass li" style="padding:22px 28px"><div class="ic">📂</div><div><div class="t">وحطها فورًا في ملف قضيتها</div></div></div>
</div>
<div class="box center" style="top:880px"><span style="font-size:30px;font-weight:800">احفظ البوست 🔖 <span class="url gold" style="margin-right:14px">mezan.pro</span></span></div>''',foot='',dots=(3,3))
M.append(dict(date=D8,time='10:00',kind='post',media=['p25_1000_1.png','p25_1000_2.png','p25_1000_3.png'],
 text='قايمة «مستني رد» ⏳\n\nأكتر حاجات بتتأخر في المكتب مش اللي في إيدك… اللي مستنيها من حد تاني.\n\n1️⃣ اكتب كل حاجة مستنيها: إيه؟ من مين؟ من إمتى؟\n2️⃣ راجع القايمة كل يوم الصبح في دقيقتين: اللي اتأخر تابعه، واللي وصل اشطبه وحطه في ملف قضيته.\n\nاحفظ البوست 🔖 وقولنا: إيه أكتر حاجة بتفضل مستنيها؟ 👇\nmezan.pro'+TAGS,
 idea='كاروسيل 3 صور: نصيحة تنظيم «قايمة مستني رد»'))

# ---------- POST 12:00 — VIDEO AI tip
video('v25_1200','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:120px" data-fx="pop" data-at=".1">🤖</div>
 <div class="h1" data-fx="rise" data-at=".5" style="font-size:80px;margin-top:20px">الذكاء الاصطناعي<br>في مكتبك</div>
 <div class="h1 gold" data-fx="stamp" data-at="1.3" style="font-size:88px;margin-top:8px">مساعد… مش بديل</div>
</div>
<div class="sc" data-a="3.2" data-b="7.2">
 <div class="h2" data-fx="rise" data-at=".2" style="font-size:64px">استخدمه في 👇</div>
 <div class="col" style="margin-top:44px;width:780px;gap:22px">
  <div class="glass li" data-fx="right" data-at=".5" style="padding:24px 30px"><div class="ic">📑</div><div class="t" style="font-size:38px">تلخيص المستندات الطويلة</div></div>
  <div class="glass li" data-fx="right" data-at=".8" style="padding:24px 30px"><div class="ic">🗓️</div><div class="t" style="font-size:38px">ترتيب الوقائع بالتاريخ</div></div>
  <div class="glass li" data-fx="right" data-at="1.1" style="padding:24px 30px"><div class="ic">✍️</div><div class="t" style="font-size:38px">مسودة أولى لرسالة</div></div>
 </div>
</div>
<div class="sc" data-a="7" data-b="10.6">
 <div class="h2" data-fx="rise" data-at=".2" style="font-size:64px">وسيب لنفسك 👇</div>
 <div class="glass" data-fx="pop" data-at=".6" style="margin-top:40px;padding:40px 60px;border-color:rgba(217,178,95,.7)"><div style="font-size:80px">⚖️</div><div class="gold" style="font-size:60px;font-weight:900">القرار القانوني</div></div>
 <div class="lead" data-fx="rise" data-at="1.2" style="margin-top:34px;font-size:40px">وراجع أي نتيجة على <span class="gold">الأصل</span> ✔️</div>
</div>
<div class="sc" data-a="10.4" data-b="13.4">
 <div class="pill" data-fx="rise" data-at=".1" style="font-size:28px">في ميزان برو</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:70px;margin-top:30px">الذكاء الاصطناعي بيلخّص<br><span class="gold">أوراق القضية</span></div>
 <div class="row" style="margin-top:40px;align-items:center;gap:24px">
  <div class="tag" data-fx="pop" data-at="1" style="font-size:34px;padding:12px 24px">📄 الملخص</div>
  <div data-fx="fade" data-at="1.2" style="font-size:44px;color:var(--gold2)">⟵</div>
  <div class="tag" data-fx="pop" data-at="1.4" style="font-size:34px;padding:12px 24px">⚖️ ملف القضية</div>
 </div>
</div>
<div class="sc" data-a="13.2" data-b="16.4">
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".1">
 <div class="h2" data-fx="rise" data-at=".4" style="margin-top:20px">جرّب بنفسك</div>
 <div class="btn" data-fx="pulse" data-at=".8" style="margin-top:28px;font-size:44px;padding:16px 50px">14 يوم مجانًا</div>
 <div class="url" data-fx="rise" data-at="1.2" style="margin-top:30px;font-size:52px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
M.append(dict(date=D8,time='12:00',kind='post',video=dict(src='v25_1200',D=16,preset='dm',seed=25,bpm=110,trans='3.2,7,10.4,13.2',pat=0),media=['v25_1200.mp4'],title='مساعد مش بديل | ميزان برو',
 text='الذكاء الاصطناعي في مكتبك… مساعد، مش بديل 🤖\n\nاستخدمه في:\n📑 تلخيص المستندات الطويلة\n🗓️ ترتيب الوقائع بالتاريخ\n✍️ مسودة أولى لرسالة\n\nوسيب لنفسك القرار القانوني ⚖️، وراجع أي نتيجة على الأصل.\n\nوفي ميزان برو الذكاء الاصطناعي بيلخّص أوراق القضية والملخص بيتربط بملفها.\nجرّب 14 يوم مجانًا 👈 mezan.pro'+TAGS,
 idea='فيديو موشن: نصيحة استخدام الذكاء الاصطناعي بأمان «مساعد مش بديل»'))

# ---------- POST 18:00 — price math
post('p25_1800','''
<div class="box center" style="top:180px"><div class="h1" style="font-size:76px">شهري ولا <span class="gold">سنوي؟</span></div><div class="lead" style="font-size:30px;margin-top:6px">احسبها بنفسك 🧮</div></div>
<div class="box" style="top:400px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
 <div class="glass center" style="padding:34px 20px">
  <div style="font-size:30px;font-weight:800;color:#c9d4ea">اشتراك شهري</div>
  <div class="gold" style="font-family:CairoL;font-size:96px;font-weight:700;line-height:1.2">200<small style="font-family:Cairo;font-size:38px"> ج</small></div>
  <div class="line" style="margin:14px 30px"></div>
  <div style="font-size:28px;color:var(--mute);font-weight:700">يعني <span style="color:var(--ink)">2400 ج</span> في السنة</div>
 </div>
 <div class="glass center" style="padding:34px 20px;border-color:rgba(217,178,95,.75);background:linear-gradient(160deg,rgba(217,178,95,.22),rgba(217,178,95,.05))">
  <div style="font-size:30px;font-weight:800;color:#c9d4ea">اشتراك سنوي</div>
  <div class="gold" style="font-family:CairoL;font-size:96px;font-weight:700;line-height:1.2">2000<small style="font-family:Cairo;font-size:38px"> ج</small></div>
  <div class="line" style="margin:14px 30px"></div>
  <div style="font-size:28px;color:var(--mute);font-weight:700">مرة واحدة <span style="color:var(--ink)">للسنة كلها</span></div>
 </div>
</div>
<div class="box center" style="top:830px"><span class="btn" style="font-size:34px">وقبل ما تختار: 14 يوم تجربة مجانية</span></div>''',pill='الأسعار 💼',foot='اختار اللي يناسب مكتبك')
M.append(dict(date=D8,time='18:00',kind='post',media=['p25_1800.png'],
 text='شهري ولا سنوي؟ احسبها بنفسك 🧮\n\n• الشهري: 200 ج × 12 شهر = 2400 ج في السنة\n• السنوي: 2000 ج مرة واحدة للسنة كلها\n\nوقبل ما تختار، جرّب ميزان برو 14 يوم مجانًا.\nابدأ من هنا 👈 mezan.pro'+TAGS,
 idea='تذكير بالأسعار بحسبة: 12×200 = 2400 مقابل السنوي 2000 + التجربة المجانية'))

# ---------- STORY 11:00 — client tip: recap before ending call
story('s25_1100','''
<div class="pill" style="position:absolute;top:390px;left:50%;transform:translateX(-50%);font-size:30px">مع الموكلين 📞</div>
<div class="center" style="position:absolute;top:500px;left:60px;right:60px">
 <div style="font-size:82px;font-weight:900;line-height:1.3">قبل ما تقفل<br>المكالمة…</div>
 <div class="gold" style="font-size:90px;font-weight:900;line-height:1.3;margin-top:6px">لخّص اللي<br>اتفقتوا عليه</div>
</div>
<div class="paper" style="position:absolute;top:1000px;left:150px;right:150px;padding:40px 46px;transform:rotate(-2deg)">
 <div style="font-size:34px;font-weight:900;color:#8a6a2c;margin-bottom:16px">«يعني إحنا اتفقنا إن…»</div>
 <div style="font-size:36px;font-weight:700;line-height:1.75">✔️ حضرتك هتبعت الورق<br>✔️ وأنا هراجعه وأرد عليك</div>
</div>
<div class="center" style="position:absolute;top:1400px;left:80px;right:80px;font-size:44px;font-weight:800;color:#c9d4ea">جملة واحدة <span class="gold">تمنع سوء فهم</span></div>
<div class="url center" style="position:absolute;top:1530px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='11:00',kind='story',media=['s25_1100.png'],idea='قصة تعامل مع الموكلين: لخّص اللي اتفقتوا عليه قبل ما تقفل المكالمة'))

# ---------- STORY 15:00 — VIDEO feature flow
video('sv25_1500','''
<div class="sc" data-a="0" data-b="4">
 <div class="row" style="position:relative;height:420px;width:600px;justify-content:center">
  <div class="paper" data-fx="drop" data-at=".1" data-dist="300" style="position:absolute;width:300px;height:380px;right:150px;top:20px;transform:rotate(-8deg)"></div>
  <div class="paper" data-fx="drop" data-at=".3" data-dist="300" style="position:absolute;width:300px;height:380px;right:140px;top:10px"></div>
  <div class="paper" data-fx="drop" data-at=".5" data-dist="300" style="position:absolute;width:300px;height:380px;right:130px;top:0;padding:40px 34px"><i style="display:block;height:16px;border-radius:8px;background:#8a7d5c;width:70%;margin-bottom:26px"></i><i style="display:block;height:13px;border-radius:7px;background:#c9c3b2;margin-bottom:18px"></i><i style="display:block;height:13px;border-radius:7px;background:#c9c3b2;margin-bottom:18px"></i><i style="display:block;height:13px;border-radius:7px;background:#c9c3b2;width:60%"></i></div>
 </div>
 <div style="font-size:90px;font-weight:900;line-height:1.3;margin-top:40px" data-fx="rise" data-at=".9">ورق القضية<br><span class="gold">كتير؟</span></div>
</div>
<div class="sc" data-a="3.8" data-b="8">
 <div style="width:200px;height:200px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle,#f3d998 0%,#d9b25f 55%,#9c7530 100%);box-shadow:0 0 0 20px rgba(217,178,95,.12),0 0 100px rgba(217,178,95,.55);font-family:CairoL;font-size:64px;font-weight:700;color:var(--navy)" data-fx="pulse" data-at=".2">AI</div>
 <div style="font-size:88px;font-weight:900;line-height:1.3;margin-top:70px" data-fx="rise" data-at=".6">الذكاء الاصطناعي<br><span class="gold">يلخّصه</span></div>
 <div class="glass" data-fx="rise" data-at="1.2" style="margin-top:50px;width:760px;padding:34px 40px;text-align:right">
  <div style="font-size:40px;font-weight:800;margin-bottom:20px">🟢 الملخص</div>
  <i data-fx="bar" data-at="1.5" style="display:block;height:16px;border-radius:8px;background:rgba(243,217,152,.6);margin-bottom:18px;transform-origin:right"></i>
  <i data-fx="bar" data-at="1.7" style="display:block;height:16px;border-radius:8px;background:rgba(243,217,152,.6);margin-bottom:18px;width:80%;transform-origin:right"></i>
  <i data-fx="bar" data-at="1.9" style="display:block;height:16px;border-radius:8px;background:rgba(243,217,152,.6);width:60%;transform-origin:right"></i>
 </div>
</div>
<div class="sc" data-a="7.8" data-b="12.3">
 <div style="font-size:150px" data-fx="pop" data-at=".1">📂</div>
 <div style="font-size:84px;font-weight:900;line-height:1.3;margin-top:30px" data-fx="rise" data-at=".4">والملخص يتربط<br><span class="gold">بملف القضية</span></div>
 <div class="url" data-fx="pulse" data-at="1.2" style="margin-top:80px;font-size:76px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
M.append(dict(date=D8,time='15:00',kind='story',video=dict(src='sv25_1500',D=12,preset='a',seed=251,bpm=122,trans='3.8,7.8',pat=3),media=['sv25_1500.mp4'],idea='قصة فيديو: ورق كتير ← الذكاء الاصطناعي يلخّصه ← الملخص يتربط بملف القضية'))

# ---------- STORY 20:30 — quote
story('s25_2030','''
<div class="glowc" style="width:1200px;height:1200px;left:-60px;top:360px"></div>
<div class="center" style="position:absolute;top:470px;left:70px;right:70px">
 <div class="gold" style="font-family:Messiri;font-size:260px;line-height:.8;height:170px">“</div>
 <div style="font-size:92px;font-weight:900;line-height:1.35;margin-top:30px">كل ورقة<br>في مكانها…</div>
 <div class="gold" style="font-size:92px;font-weight:900;line-height:1.35">دقيقة زيادة<br>لموكلك</div>
 <div class="line" style="width:300px;margin:60px auto 30px"></div>
 <div style="font-size:42px;color:#c9d4ea;font-weight:700">تصبح على خير يا متر 🌙</div>
</div>
<div class="url center" style="position:absolute;top:1520px;left:0;right:0;font-size:62px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='20:30',kind='story',media=['s25_2030.png'],idea='قصة اقتباس: «كل ورقة في مكانها… دقيقة زيادة لموكلك»'))
json.dump(M,open('m25.json','w'),ensure_ascii=False,indent=1);print('ok')
