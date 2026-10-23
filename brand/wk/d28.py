from lib import *
import json
M=[];D8='2026-10-28'
TAGS='\n\n#ميزان_برو #محاماة'
# ---------- POST 10:00 — problem/solution: duplicate files
post('p28_1000','''
<div class="box center" style="top:160px"><div class="h1" style="font-size:68px">أنهي فيهم <span class="gold">الأحدث؟</span> 🤔</div></div>
<div class="box row" style="top:320px;justify-content:center;gap:28px;direction:ltr">
 <div class="paper" style="width:270px;padding:26px 22px;transform:rotate(-5deg)"><div style="font-size:54px">📄</div><div style="font-family:CairoL,Cairo;font-size:22px;font-weight:700;margin-top:8px;direction:ltr">mozakra_final.docx</div></div>
 <div class="paper" style="width:270px;padding:26px 22px;transform:rotate(2deg)"><div style="font-size:54px">📄</div><div style="font-family:CairoL,Cairo;font-size:22px;font-weight:700;margin-top:8px;direction:ltr">mozakra_final_2.docx</div></div>
 <div class="paper" style="width:270px;padding:26px 22px;transform:rotate(6deg)"><div style="font-size:54px">📄</div><div style="font-family:CairoL,Cairo;font-size:22px;font-weight:700;margin-top:8px;direction:ltr">final_FINAL.docx</div></div>
</div>
<div class="box glass" style="top:640px;padding:30px 36px;display:flex;align-items:center;gap:26px;border-color:rgba(217,178,95,.6)">
 <img src="../logo.svg" width="90">
 <div><div style="font-size:36px;font-weight:900">في ميزان برو: <span class="gold">كل قضية ليها ملف واحد</span></div><div class="lead" style="font-size:27px">بمستنداتها وملخصاتها… في مكان واحد</div></div>
</div>''',pill='مشكلة وحلها 💡',foot='حصلت معاك؟ 😅')
M.append(dict(date=D8,time='10:00',kind='post',media=['p28_1000.png'],
 text='final… final_2… final_FINAL 😅\nأنهي فيهم الأحدث؟\n\nلما نفس الملف يبقى منه كذا نسخة، الوقت بيضيع في المقارنة بدل الشغل.\n\nفي ميزان برو كل قضية ليها ملف واحد بمستنداتها وملخصاتها… في مكان واحد.\nحصلت معاك؟ قولنا في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='مشكلة وحلها: كذا نسخة من نفس الملف (final_2 / final_FINAL) ← ملف واحد لكل قضية'))

# ---------- POST 12:00 — VIDEO trial steps + prices
video('v28_1200','''
<div class="sc" data-a="0" data-b="3.2">
 <div class="h1" data-fx="rise" data-at=".2" style="font-size:88px">تبدأ مع<br><span class="gold">ميزان برو</span> إزاي؟</div>
 <div class="lead" data-fx="rise" data-at=".8" style="font-size:42px;margin-top:20px">3 خطوات بس 👇</div>
</div>
<div class="sc" data-a="3" data-b="9.4">
 <div class="col" style="width:820px;gap:26px">
  <div class="glass li" data-fx="right" data-at=".2" style="padding:28px 32px"><div class="num" style="width:70px;height:70px;font-size:38px">1</div><div class="t" style="font-size:42px">ادخل على <span class="url gold">mezan.pro</span></div></div>
  <div class="glass li" data-fx="right" data-at="1.6" style="padding:28px 32px"><div class="num" style="width:70px;height:70px;font-size:38px">2</div><div class="t" style="font-size:42px">ابدأ <span class="gold">التجربة المجانية</span></div></div>
  <div class="glass li" data-fx="right" data-at="3" style="padding:28px 32px"><div class="num" style="width:70px;height:70px;font-size:38px">3</div><div class="t" style="font-size:42px">جرّب تلخيص مستندات قضية 🤖</div></div>
 </div>
</div>
<div class="sc" data-a="9.2" data-b="13.2">
 <div class="lead" data-fx="rise" data-at=".1" style="font-size:42px">وبعد الـ 14 يوم… اختار اللي يناسبك</div>
 <div class="row" style="margin-top:44px;gap:30px">
  <div class="glass" data-fx="pop" data-at=".5" style="width:330px;padding:34px 20px"><div style="font-size:30px;color:#c9d4ea;font-weight:700">اشتراك شهري</div><div class="gold" style="font-family:CairoL;font-size:90px;font-weight:700">200<small style="font-family:Cairo;font-size:36px"> ج</small></div></div>
  <div class="glass" data-fx="pop" data-at=".8" style="width:330px;padding:34px 20px;border-color:rgba(217,178,95,.7);background:linear-gradient(160deg,rgba(217,178,95,.2),rgba(217,178,95,.05))"><div style="font-size:30px;color:#c9d4ea;font-weight:700">اشتراك سنوي</div><div class="gold" style="font-family:CairoL;font-size:90px;font-weight:700">2000<small style="font-family:Cairo;font-size:36px"> ج</small></div></div>
 </div>
</div>
<div class="sc" data-a="13" data-b="16.4">
 <img src="../logo.svg" width="140" data-fx="spin" data-at=".1">
 <div class="btn" data-fx="pulse" data-at=".5" style="margin-top:34px;font-size:46px;padding:18px 54px">ابدأ النهارده مجانًا</div>
 <div class="url" data-fx="rise" data-at=".9" style="margin-top:32px;font-size:58px;color:var(--gold2)">mezan.pro</div>
</div>''',D=16)
M.append(dict(date=D8,time='12:00',kind='post',video=dict(src='v28_1200',D=16,preset='f',seed=28,bpm=120,trans='3,9.2,13',pat=4),media=['v28_1200.mp4'],title='تبدأ إزاي؟ | ميزان برو',
 text='تبدأ مع ميزان برو إزاي؟ 3 خطوات بس 👇\n\n1️⃣ ادخل على mezan.pro\n2️⃣ ابدأ التجربة المجانية 14 يوم\n3️⃣ جرّب تلخيص مستندات قضية بالذكاء الاصطناعي\n\nوبعد التجربة اختار اللي يناسبك: الشهري 200 ج أو السنوي 2000 ج.\nابدأ النهارده 👈 mezan.pro'+TAGS,
 idea='فيديو موشن: 3 خطوات تبدأ بيها التجربة المجانية + الأسعار'))

# ---------- POST 18:00 — legal: distance period (Art 16)
post('p28_1800','''
<div class="box" style="top:160px"><div class="lead" style="font-size:30px;color:var(--gold2)">ميعاد المسافة</div><div class="h1" style="font-size:66px;margin-top:4px">الميعاد بيزيد <span class="gold">يوم</span><br>لكل <span class="gold">50 كم</span></div></div>
<div class="box" style="top:450px;height:120px">
 <div style="position:absolute;top:56px;left:0;right:0;height:8px;border-radius:8px;background:repeating-linear-gradient(90deg,var(--gold) 0 40px,transparent 40px 60px)"></div>
 <div style="position:absolute;right:0;top:20px;font-size:60px">📍</div>
 <div style="position:absolute;left:0;top:20px;font-size:60px">🏛️</div>
 <div class="tag" style="position:absolute;right:28%;top:-2px;font-size:22px">50 كم: يوم</div>
 <div class="tag" style="position:absolute;right:58%;top:-2px;font-size:22px">100 كم: يومين</div>
</div>
<div class="box row" style="top:600px;gap:20px">
 <div class="glass card" style="flex:1"><div style="font-size:40px">➕</div><div style="font-size:27px;font-weight:800;margin-top:6px;line-height:1.5">الكسر اللي يزيد على 30 كم<br>يزوّد يوم</div></div>
 <div class="glass card" style="flex:1;border-color:rgba(217,178,95,.6)"><div style="font-size:40px">🛑</div><div style="font-size:27px;font-weight:800;margin-top:6px;line-height:1.5">وبحد أقصى<br><span class="gold">4 أيام</span></div></div>
</div>
<div class="box small" style="top:850px;font-size:23px">📌 المادة 16 — قانون المرافعات المدنية والتجارية (وفيها حكم خاص لمن موطنه في مناطق الحدود)</div>''',pill='معلومة إجرائية ⚖️',foot='احفظها وشاركها 🔖')
M.append(dict(date=D8,time='18:00',kind='post',media=['p28_1800.png'],
 text='معلومة إجرائية: ميعاد المسافة ⚖️\n\nلو الإجراء محتاج انتقال، المادة 16 من قانون المرافعات بتزوّد على الميعاد «يوم لكل مسافة مقدارها خمسون كيلو مترًا» بين المكانين.\n➕ والكسر اللي يزيد على 30 كم يزوّد يوم كمان.\n🛑 وبحد أقصى 4 أيام.\n(والمادة فيها حكم خاص لمن موطنه في مناطق الحدود.)\n\nاحفظ البوست وشاركه مع زمايلك 🔖'+TAGS,
 idea='معلومة إجرائية: ميعاد المسافة يوم لكل 50 كم وبحد أقصى 4 أيام (م.16 مرافعات)'))

# ---------- STORY 11:00 — poll
story('s28_1100','''
<div class="pill" style="position:absolute;top:390px;left:50%;transform:translateX(-50%);font-size:30px">سؤال الصبح ☀️</div>
<div class="center" style="position:absolute;top:500px;left:60px;right:60px"><div style="font-size:84px;font-weight:900;line-height:1.3">عندك كام قضية<br><span class="gold">مفتوحة</span> دلوقتي؟</div></div>
<div style="position:absolute;top:860px;left:110px;right:110px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px">
 <div class="glass center" style="padding:44px 10px"><div style="font-size:76px">📁</div><div style="font-size:34px;font-weight:800;margin-top:6px">أقل من 10</div></div>
 <div class="glass center" style="padding:44px 10px"><div style="font-size:76px">📂</div><div style="font-size:34px;font-weight:800;margin-top:6px">من 10 لـ 30</div></div>
 <div class="glass center" style="padding:44px 10px"><div style="font-size:76px">🗄️</div><div style="font-size:34px;font-weight:800;margin-top:6px">أكتر من 30</div></div>
</div>
<div class="center" style="position:absolute;top:1230px;left:60px;right:60px;font-size:46px;font-weight:800;color:#c9d4ea">ابعتلنا الرقم في رسالة 📩</div>
<div class="url center" style="position:absolute;top:1520px;left:0;right:0;font-size:60px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='11:00',kind='story',media=['s28_1100.png'],idea='قصة سؤال تفاعلي: عندك كام قضية مفتوحة دلوقتي؟'))

# ---------- STORY 15:00 — ORG: phone photos
story('s28_1500','''
<div style="position:absolute;top:400px;left:50%;margin-left:-190px;width:380px;height:620px;border-radius:56px;border:10px solid #2a3a5e;background:#0f1d3d;box-shadow:0 40px 100px rgba(0,0,0,.5);padding:40px 22px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;align-content:start">
 <div style="aspect-ratio:1;border-radius:12px;background:#34507e"></div><div style="aspect-ratio:1;border-radius:12px;background:#6b4f7e;display:grid;place-items:center;font-size:40px">🎂</div><div style="aspect-ratio:1;border-radius:12px;background:#f4f1e8;display:grid;place-items:center;font-size:40px">📄</div>
 <div style="aspect-ratio:1;border-radius:12px;background:#4b6b4f;display:grid;place-items:center;font-size:40px">🌳</div><div style="aspect-ratio:1;border-radius:12px;background:#f4f1e8;display:grid;place-items:center;font-size:40px">📄</div><div style="aspect-ratio:1;border-radius:12px;background:#7e5a34;display:grid;place-items:center;font-size:40px">🍽️</div>
 <div style="aspect-ratio:1;border-radius:12px;background:#34507e;display:grid;place-items:center;font-size:40px">👨‍👩‍👧</div><div style="aspect-ratio:1;border-radius:12px;background:#f4f1e8;display:grid;place-items:center;font-size:40px">📄</div><div style="aspect-ratio:1;border-radius:12px;background:#5b3a5e"></div>
 <div style="aspect-ratio:1;border-radius:12px;background:#2f5f6b;display:grid;place-items:center;font-size:40px">🏖️</div><div style="aspect-ratio:1;border-radius:12px;background:#6b2f3a"></div><div style="aspect-ratio:1;border-radius:12px;background:#f4f1e8;display:grid;place-items:center;font-size:40px">📄</div>
</div>
<div class="center" style="position:absolute;top:1090px;left:60px;right:60px">
 <div style="font-size:70px;font-weight:900;line-height:1.35">صوّرت مستند<br>على الموبايل؟ 📸</div>
 <div class="gold" style="font-size:64px;font-weight:900;line-height:1.35;margin-top:8px">نزّله في ملف قضيته<br>النهارده</div>
 <div style="font-size:40px;color:#c9d4ea;font-weight:700;margin-top:18px">قبل ما يتوه وسط صور العيلة 😅</div>
</div>
<div class="url center" style="position:absolute;top:1590px;left:0;right:0;font-size:56px;color:var(--gold2)">mezan.pro</div>''')
M.append(dict(date=D8,time='15:00',kind='story',media=['s28_1500.png'],idea='قصة تنظيم: صوّرت مستند على الموبايل؟ نزّله في ملف قضيته النهارده'))

# ---------- STORY 20:30 — VIDEO AI check
video('sv28_2030','''
<div class="sc" data-a="0" data-b="3.6">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🤖</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">قبل ما تعتمد<br>على رد <span class="gold">الذكاء الاصطناعي</span></div>
</div>
<div class="sc" data-a="3.4" data-b="8.6">
 <div style="font-size:70px;font-weight:900" data-fx="rise" data-at=".1">راجع على <span class="gold">الأصل</span>:</div>
 <div class="col" style="width:100%;gap:30px;margin-top:50px">
  <div class="glass" data-fx="pop" data-at=".6" style="padding:36px;display:flex;align-items:center;gap:30px;justify-content:center"><span style="font-size:80px">👤</span><span style="font-size:64px;font-weight:900">الأسماء</span><span data-fx="pop" data-at="1.0" style="font-size:60px">✅</span></div>
  <div class="glass" data-fx="pop" data-at="1.5" style="padding:36px;display:flex;align-items:center;gap:30px;justify-content:center"><span style="font-size:80px">📅</span><span style="font-size:64px;font-weight:900">التواريخ</span><span data-fx="pop" data-at="1.9" style="font-size:60px">✅</span></div>
  <div class="glass" data-fx="pop" data-at="2.4" style="padding:36px;display:flex;align-items:center;gap:30px;justify-content:center"><span style="font-size:80px">🔢</span><span style="font-size:64px;font-weight:900">الأرقام</span><span data-fx="pop" data-at="2.8" style="font-size:60px">✅</span></div>
 </div>
</div>
<div class="sc" data-a="8.4" data-b="12.3">
 <div style="font-size:80px;font-weight:900;line-height:1.35" data-fx="rise" data-at=".1">هو بيوفّر وقتك…<br><span class="gold">والمراجعة عليك</span> ⚖️</div>
 <img src="../logo.svg" width="150" data-fx="spin" data-at=".6" style="margin-top:70px">
 <div class="url" data-fx="pulse" data-at="1" style="margin-top:40px;font-size:72px;color:var(--gold2)">mezan.pro</div>
</div>''',D=12,story=True)
M.append(dict(date=D8,time='20:30',kind='story',video=dict(src='sv28_2030',D=12,preset='am2',seed=282,bpm=96,trans='3.4,8.4',pat=0),media=['sv28_2030.mp4'],idea='قصة فيديو ذكاء اصطناعي: راجع الأسماء والتواريخ والأرقام على الأصل'))
json.dump(M,open('m28.json','w'),ensure_ascii=False,indent=1);print('ok')
