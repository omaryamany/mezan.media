from w4c import *

# ======================= SAT 2026-11-14 =======================
D='2026-11-14'
video('v14_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="drop" data-at=".1">📚</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:80px;margin-top:20px">قدامك ملف <span class="gold">تقيل</span>…</div>
 <div class="lead" data-fx="rise" data-at=".8" style="font-size:44px;margin-top:10px">والجلسة قرّبت ⏳</div>
</div>
<div class="sc" data-a="3.2" data-b="6.6">
 <div class="h1" data-fx="rise" data-at=".1" style="font-size:70px">تبدأ منين؟ 🤔</div>
 <div class="glass" data-fx="pop" data-at=".6" style="padding:34px 50px;margin-top:40px;font-size:46px;font-weight:800;line-height:1.6">صفحة صفحة…<br>وانت مش عارف <span class="gold">المهم فين</span></div>
</div>
<div class="sc" data-a="6.4" data-b="12.4">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:34px">الحل مع ميزان برو ✨</div>
 <div class="col" style="gap:26px;width:880px;margin-top:40px">
  '''+li('🤖','ملخص أوراق ومستندات القضية','بالذكاء الاصطناعي',at='.5',ts=42)+'''
  '''+li('🔗','الملخص مربوط بملف القضية','تلاقيه وقت ما تحتاجه',at='1.3',ts=42)+'''
  '''+li('✅','وإنت تراجع… وتقرّر','الملخص بيوفّر وقتك',at='2.1',ts=42,extra='border-color:rgba(217,178,95,.7)')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='ابدأ من الملخص… وركّز في الدفاع'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v14_1000',D=16,preset='bm',seed=1401,bpm=100,trans='3.2,6.4,12.2',pat=3),media=['v14_1000.mp4'],title='قدامك ملف تقيل؟ | ميزان برو',
 text='قدامك ملف تقيل… والجلسة قرّبت؟ 📚⏳\n\nبدل ما تبدأ من أول صفحة وانت مش عارف المهم فين:\n🤖 ميزان برو بيلخّص أوراق ومستندات القضية بالذكاء الاصطناعي\n🔗 والملخص بيتربط بملف القضية… تلاقيه وقت ما تحتاجه\n✅ وإنت تراجع وتقرّر\n\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='فيديو موشن مشكلة وحلها: ملف تقيل والجلسة قرّبت ← ملخص بالذكاء الاصطناعي مربوط بملف القضية')

def tile(l,t):
    return f'<div class="glass center" style="padding:30px 20px;display:flex;flex-direction:column;align-items:center;gap:12px"><div class="num" style="width:86px;height:86px;font-size:46px;font-family:Cairo;font-weight:900">{l}</div><div style="font-size:40px;font-weight:900">{t}</div></div>'
post('p14_1400','''
<div class="box center" style="top:170px"><div class="h1" style="font-size:66px">📂 كام قضية <span class="gold">شغال عليها</span><br>دلوقتي؟</div></div>
<div class="box" style="top:420px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 '''+tile('أ','أقل من 10')+tile('ب','من 10 لـ 30')+tile('ج','من 30 لـ 60')+tile('د','أكتر من 60 😅')+'''
</div>''',pill='سؤال للمحامين 💬',foot='اكتب حرفك في الكومنتات 👇')
add(date=D,time='14:00',kind='post',media=['p14_1400.png'],
 text='سؤال للمحامين 💬\nكام قضية شغال عليها دلوقتي؟ 📂\n\nأ) أقل من 10\nب) من 10 لـ 30\nج) من 30 لـ 60\nد) أكتر من 60 😅\n\nاكتب حرفك في الكومنتات 👇\nmezan.pro'+TAGS,
 idea='سؤال تفاعلي: كام قضية شغال عليها دلوقتي؟ (أ/ب/ج/د)')

post('p14_1900','''
<div class="box" style="top:150px"><div class="h1" style="font-size:62px">بعد أي مقابلة مع موكل…<br><span class="gold">ابعتله ملخص في رسالة</span> ✉️</div></div>
<div class="box" style="top:395px;display:flex;justify-content:flex-start">
 <div style="width:640px;padding:30px 36px;border-radius:30px 30px 30px 8px;background:#f4f1e8;color:#1b2440;box-shadow:0 20px 50px rgba(0,0,0,.4);font-size:31px;font-weight:700;line-height:1.75">
  متشكر على وقتك النهارده 🤝<br>
  <b style="color:#8a6a2c">✅ اتفقنا على:</b> …<br>
  <b style="color:#8a6a2c">📎 محتاجين منك:</b> …<br>
  <b style="color:#8a6a2c">➡️ الخطوة الجاية:</b> …
 </div>
</div>
<div class="box" style="top:790px;display:flex;gap:16px;justify-content:center">
 <span class="tag" style="font-size:28px">مفيش سوء فهم</span><span class="tag" style="font-size:28px">موكلك يطمّن</span><span class="tag" style="font-size:28px">مرجع ليك بعدين</span>
</div>''',pill='تعامل مع الموكلين 🤝')
add(date=D,time='19:00',kind='post',media=['p14_1900.png'],
 text='بعد أي مقابلة مع موكل… ابعتله ملخص في رسالة ✉️\n\n✅ اتفقنا على إيه\n📎 محتاجين منه إيه\n➡️ الخطوة الجاية إيه\n\nرسالة قصيرة بتمنع سوء الفهم، وتطمّن موكلك، وتبقى مرجع ليك بعدين.\nإنت بتعملها؟ 👇\nmezan.pro'+TAGS,
 idea='نصيحة تواصل مع الموكلين: ابعت ملخص مكتوب للموكل بعد كل مقابلة (اتفقنا/محتاجين/الخطوة الجاية)')

sflow('s14_1100','''
<div style="font-size:68px;font-weight:900;line-height:1.35">تلخيص أوراق القضية</div>
<div class="glass" style="padding:36px 40px;border-color:rgba(252,165,165,.35)"><div class="tag" style="background:rgba(252,165,165,.15);color:#fca5a5;font-size:34px">قبل</div><div style="font-size:96px;margin-top:10px">✍️😓</div><div style="font-size:46px;font-weight:800;line-height:1.5">تقرا وتلخّص بإيدك<br>وتدوّر على الملخص بعدين</div></div>
<div style="display:flex;justify-content:center;margin:-20px 0"><div class="num" style="width:110px;height:110px;border-radius:50%;font-size:40px;font-family:Cairo;font-weight:900">VS</div></div>
<div class="glass" style="padding:36px 40px;border-color:rgba(217,178,95,.7)"><div class="tag" style="font-size:34px">بعد</div><div style="font-size:96px;margin-top:10px">🤖📁</div><div style="font-size:46px;font-weight:800;line-height:1.5">ملخص بالذكاء الاصطناعي<br><span class="gold">مربوط بملف القضية</span></div></div>''',gap=36)
add(date=D,time='11:00',kind='story',media=['s14_1100.png'],idea='قصة قبل/بعد: تلخيص الأوراق بإيدك ضد ملخص بالذكاء الاصطناعي مربوط بملف القضية')

video('sv14_1500','''
<div class="sc" data-a="0" data-b="4.2">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🧠</div>
 <div style="font-size:100px;font-weight:900;line-height:1.3;margin-top:30px" data-fx="rise" data-at=".5">اشتغل<br><span class="gold">بذكاء</span>…</div>
</div>
<div class="sc" data-a="4" data-b="8.6">
 <div style="font-size:150px" data-fx="pop" data-at=".1">💪</div>
 <div style="font-size:90px;font-weight:900;line-height:1.3;margin-top:30px" data-fx="rise" data-at=".4">مش بس<br><span class="gold">بجهد</span></div>
</div>
'''+END_S.format(a='8.4',line='نظّم شغلك…<br><span class="gold">وريّح دماغك</span>'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv14_1500',D=12,preset='g',seed=1415,bpm=112,trans='4,8.4',pat=4),media=['sv14_1500.mp4'],idea='قصة فيديو اقتباس: «اشتغل بذكاء… مش بس بجهد»')

sflow('s14_2030','''
<div style="font-size:60px;font-weight:900">جرّب ميزان برو بنفسك</div>
<div style="position:relative;margin:0 auto;width:520px;height:520px;border-radius:50%;border:6px solid rgba(217,178,95,.6);display:grid;place-items:center;background:radial-gradient(circle,rgba(217,178,95,.18),transparent 70%)">
 <div><div class="gold" style="font-family:CairoL;font-weight:700;font-size:260px;line-height:1">14</div><div style="font-size:64px;font-weight:900">يوم مجانًا 🎁</div></div>
</div>
<div class="glass" style="padding:34px;margin:0 30px;font-size:44px;font-weight:800;line-height:1.6">وبعدها:<br><span class="gold">200 ج</span> شهري · <span class="gold">2000 ج</span> سنوي</div>''',gap=56)
add(date=D,time='20:30',kind='story',media=['s14_2030.png'],idea='قصة أسعار: دايرة كبيرة «14 يوم مجانًا» + 200 ج شهري / 2000 ج سنوي')

# ======================= SUN 2026-11-15 =======================
D='2026-11-15'
def q4(c,t,d,ex):
    return f'<div class="glass" style="padding:26px 28px;border-top:6px solid {c}"><div style="font-size:34px;font-weight:900">{t}</div><div style="font-size:30px;font-weight:800;color:var(--gold2);margin-top:8px">{d}</div><div class="small" style="font-size:24px;margin-top:6px">{ex}</div></div>'
post('p15_1000','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:62px">رتّب مهامك في <span class="gold">4 خانات</span> 🗂️</div></div>
<div class="box" style="top:280px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
 '''+q4('#f87171','🔴 مستعجل ومهم','اعمله دلوقتي','مذكرة جلسة بكرة')+q4('#fbbf24','🟡 مهم ومش مستعجل','حدّدله ميعاد','مراجعة ملف قضية')+q4('#60a5fa','🔵 مستعجل ومش مهم','خلّصه بسرعة أو فوّضه','مكالمة روتينية')+q4('#cbd5e1','⚪ لا ده ولا ده','أجّله أو سيبه','تصفّح الموبايل')+'''
</div>
<div class="box center" style="top:850px;font-size:30px;font-weight:800">الخانة <span class="gold">الصفرا</span> هي اللي بتفرق على المدى الطويل 👌</div>''',pill='نصيحة تنظيم ⏱️')
add(date=D,time='10:00',kind='post',media=['p15_1000.png'],
 text='قبل ما تبدأ يومك… رتّب مهامك في 4 خانات 🗂️\n\n🔴 مستعجل ومهم ← اعمله دلوقتي\n🟡 مهم ومش مستعجل ← حدّدله ميعاد\n🔵 مستعجل ومش مهم ← خلّصه بسرعة أو فوّضه\n⚪ لا مستعجل ولا مهم ← أجّله أو سيبه\n\nالخانة الصفرا هي اللي بتفرق على المدى الطويل 👌\nجرّبها بكرة الصبح وقولنا 👇\nmezan.pro'+TAGS,
 idea='نصيحة تنظيم وقت: مصفوفة 4 خانات (مستعجل/مهم) لترتيب المهام')

def vstep(a,b,ic,q,ans):
    return f'''<div class="sc" data-a="{a}" data-b="{b}">
 <div style="font-size:120px" data-fx="pop" data-at=".1">{ic}</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:62px;margin-top:20px">{q}</div>
 <div class="glass" data-fx="rise" data-at=".9" style="padding:26px 44px;margin-top:34px;font-size:46px;font-weight:900;border-color:rgba(217,178,95,.7)">{ans}</div>
</div>'''
video('v15_1400','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🤖</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:80px;margin-top:20px">الذكاء الاصطناعي<br><span class="gold">مساعد… مش مرجع</span></div>
</div>
'''+vstep(3.2,6.4,'⚖️','طلّعلك رقم مادة؟','ارجع <span class="gold">للنص</span> بنفسك')+vstep(6.2,9.4,'📚','ذكر حكم أو مبدأ؟','اتأكد من <span class="gold">مصدره الرسمي</span>')+vstep(9.2,12.4,'✍️','كتبلك صياغة؟','راجعها وعدّلها <span class="gold">بأسلوبك</span>')+END_P.format(a='12.2',line='هو بيوفّر وقتك… والقرار ليك إنت'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v15_1400',D=16,preset='cm',seed=1514,bpm=92,trans='3.2,6.2,9.2,12.2',pat=4),media=['v15_1400.mp4'],title='مساعد… مش مرجع | ميزان برو',
 text='الذكاء الاصطناعي مساعد… مش مرجع 🤖\n\n⚖️ طلّعلك رقم مادة؟ ارجع للنص بنفسك\n📚 ذكر حكم أو مبدأ؟ اتأكد من مصدره الرسمي\n✍️ كتبلك صياغة؟ راجعها وعدّلها بأسلوبك\n\nهو بيوفّر وقتك… لكن القرار والمسؤولية عليك إنت.\nmezan.pro'+TAGS,
 idea='فيديو موشن ذكاء اصطناعي بأمان: مساعد مش مرجع — راجع أرقام المواد والأحكام والصياغة بنفسك')

post('p15_1900','''
<div class="box center" style="top:150px"><div class="h1" style="font-size:66px">حسبة بسيطة 🧮</div></div>
<div class="box glass center" style="top:290px;padding:34px">
 <div style="font-size:36px;font-weight:800;color:var(--mute)">شهري لمدة سنة</div>
 <div style="position:relative;display:inline-block;font-size:64px;font-weight:900;margin-top:6px">12 × 200 ج = 2400 ج<div style="position:absolute;left:-10px;right:-10px;top:52%;height:6px;background:#fca5a5;border-radius:4px;transform:rotate(-3deg)"></div></div>
</div>
<div class="box center" style="top:545px;padding:34px;border-radius:28px;border:2px solid rgba(217,178,95,.8);background:rgba(217,178,95,.1)">
 <div style="font-size:36px;font-weight:800;color:var(--gold2)">الاشتراك السنوي</div>
 <div style="font-size:96px;font-weight:900;line-height:1.2"><span class="gold">2000</span> ج</div>
 <div class="btn" style="position:absolute;left:30px;bottom:-30px;font-size:30px;padding:10px 26px;transform:rotate(-4deg)">وفّرت 400 ج ✅</div>
</div>
<div class="box center" style="top:880px;font-size:32px;font-weight:800">ولسه بتفكر؟ ابدأ بـ <span class="gold">14 يوم مجانًا</span> 🎁</div>''',pill='الأسعار 🏷️')
add(date=D,time='19:00',kind='post',media=['p15_1900.png'],
 text='حسبة بسيطة 🧮\n\n12 شهر × 200 ج = 2400 ج\nالاشتراك السنوي = 2000 ج\nيعني السنوي بيوفّرلك 400 ج ✅\n\nولسه بتفكر؟ ابدأ بـ 14 يوم تجربة مجانية 🎁\n👈 mezan.pro'+TAGS,
 idea='تذكير بالأسعار: حسبة 12×200=2400 ضد السنوي 2000 (وفّر 400 ج) + 14 يوم مجانًا')

video('sv15_1100','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:140px" data-fx="drop" data-at=".1">📅</div>
 <div style="font-size:84px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">الجلسة بكرة؟<br><span class="gold">ابعت لموكلك</span><br>3 حاجات</div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:30px">
  '''+opt(1,'🕘 الميعاد والساعة','.3')+opt(2,'📍 المحكمة والدايرة','1')+opt(3,'🗂️ يجيب معاه إيه','1.7')+'''
 </div>
</div>
'''+END_S.format(a='8.4',line='موكل عارف…<br><span class="gold">موكل مطمّن</span>'),D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv15_1100',D=12,preset='c',seed=1511,bpm=120,trans='3.2,8.4',pat=1),media=['sv15_1100.mp4'],idea='قصة فيديو تعامل مع الموكلين: الجلسة بكرة؟ ابعت لموكلك الميعاد والمكان ويجيب إيه')

sflow('s15_1500','''
<div class="tag" style="align-self:center;font-size:38px">أسئلة شائعة ❓</div>
<div class="glass" style="padding:40px;margin-left:120px;border-radius:40px 40px 40px 10px;font-size:62px;font-weight:900;line-height:1.4;text-align:right">ميزان برو<br>بيلخّص <span class="gold">إيه</span>؟ 🤔</div>
<div style="padding:44px;margin-right:60px;border-radius:40px 40px 10px 40px;font-size:52px;font-weight:900;line-height:1.55;color:var(--navy);text-align:right;background:linear-gradient(160deg,var(--gold2),var(--gold) 60%,#b88d3a)">📄 أوراق ومستندات القضايا<br>🤖 بالذكاء الاصطناعي<br>🔗 والملخص بيتربط<br>بملف القضية</div>''',gap=50)
add(date=D,time='15:00',kind='story',media=['s15_1500.png'],idea='قصة أسئلة شائعة: ميزان برو بيلخّص إيه؟ أوراق ومستندات القضايا ومربوطة بملف القضية')

def sopt(ic,t):
    return f'<div class="glass" style="padding:36px 30px;display:flex;align-items:center;gap:30px;margin:0 40px"><div style="font-size:90px">{ic}</div><div style="font-size:60px;font-weight:900">{t}</div></div>'
sflow('s15_2030','''
<div style="font-size:76px;font-weight:900;line-height:1.35">بتحفظ مستنداتك<br><span class="gold">إزاي؟</span></div>
'''+sopt('🗄️','ورق')+sopt('💻','ديجيتال')+sopt('🔀','الاتنين')+'''
<div style="font-size:46px;font-weight:800;color:var(--gold2)">ابعتلنا ردّك في رسالة 📩</div>''',gap=44)
add(date=D,time='20:30',kind='story',media=['s15_2030.png'],idea='قصة سؤال: بتحفظ مستنداتك إزاي؟ ورق / ديجيتال / الاتنين')

# ======================= MON 2026-11-16 =======================
D='2026-11-16'
post('p16_1000','''
<div class="glowc" style="width:700px;height:700px;left:-120px;top:200px"></div>
<div style="position:absolute;top:200px;left:66px;width:400px;height:400px;border-radius:50%;border:5px solid rgba(217,178,95,.6);display:grid;place-items:center;background:rgba(217,178,95,.06)">
 <div class="center"><div class="gold" style="font-family:CairoL;font-weight:700;font-size:190px;line-height:1">60</div><div style="font-size:52px;font-weight:900">يوم</div></div>
</div>
<div style="position:absolute;top:210px;right:66px;width:520px">
 <div class="h1" style="font-size:64px">ميعاد الطعن<br><span class="gold">بالنقض</span> ⚖️</div>
 <div class="lead" style="font-size:30px;margin-top:20px">طبقًا للمادة 252 من قانون المرافعات المدنية والتجارية</div>
</div>
<div class="box paper" style="top:660px;padding:30px 40px;font-size:38px;font-weight:800;line-height:1.6;text-align:center">«ميعاد الطعن بطريق النقض <span style="color:#8a6a2c">ستون يومًا</span>»</div>
<div class="box center" style="top:860px;font-size:30px;font-weight:800">📌 اتأكد من تاريخ بداية الميعاد… وسجّله في ملف القضية</div>''',pill='معلومة إجرائية 📚',foot='احفظ البوست 🔖')
add(date=D,time='10:00',kind='post',media=['p16_1000.png'],
 text='معلومة إجرائية ⚖️ ميعاد الطعن بالنقض\n\n⏳ 60 يوم\nطبقًا للمادة 252 من قانون المرافعات المدنية والتجارية: «ميعاد الطعن بطريق النقض ستون يومًا».\n\n📌 اتأكد دايمًا من تاريخ بداية حساب الميعاد في قضيتك، وسجّله في ملفها من أول يوم.\n\nاحفظ البوست ده 🔖\nmezan.pro'+TAGS,
 idea='معلومة إجرائية: ميعاد الطعن بالنقض 60 يوم (م.252 مرافعات)')

def col(title,c,items,at):
    s=''.join(f'<div class="li" style="gap:18px;margin-top:22px"><div style="font-size:52px">{i}</div><div style="font-size:36px;font-weight:800;text-align:right">{t}</div></div>' for i,t in items)
    return f'<div class="glass" data-fx="rise" data-at="{at}" style="flex:1;padding:30px 30px 36px;border-color:{c}"><div class="tag" style="font-size:32px">{title}</div>{s}</div>'
video('v16_1400','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">🗓️</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:84px;margin-top:20px">تحضير<br><span class="gold">جلسة بكرة</span></div>
</div>
<div class="sc" data-a="3.2" data-b="7.8">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:40px;background:rgba(252,165,165,.15);color:#fca5a5">قبل (بالورق)</div>
 <div class="col" style="gap:24px;width:820px;margin-top:36px">
  '''+li('🗄️','تطلّع الملف من الدولاب',at='.4',ts=42)+li('📄','تقلّب الأوراق صفحة صفحة',at='1',ts=42)+li('🧠','وتحاول تفتكر المهم',at='1.6',ts=42)+'''
 </div>
</div>
<div class="sc" data-a="7.6" data-b="12.4">
 <div class="tag" data-fx="pop" data-at=".1" style="font-size:40px">بعد (مع ميزان برو)</div>
 <div class="col" style="gap:24px;width:860px;margin-top:36px">
  '''+li('📁','ملف القضية قدامك',at='.4',ts=42)+li('🤖','ملخص الأوراق مربوط بالملف',at='1',ts=42)+li('✅','ووقتك يروح للدفاع',at='1.6',ts=42,extra='border-color:rgba(217,178,95,.7)')+'''
 </div>
</div>
'''+END_P.format(a='12.2',line='ركّز في الدفاع… والترتيب في ملف القضية'),D=16)
add(date=D,time='14:00',kind='post',video=dict(src='v16_1400',D=16,preset='dm',seed=1614,bpm=108,trans='3.2,7.6,12.2',pat=0),media=['v16_1400.mp4'],title='تحضير جلسة بكرة | ميزان برو',
 text='تحضير جلسة بكرة 🗓️\n\nقبل (بالورق):\n🗄️ تطلّع الملف من الدولاب\n📄 تقلّب الأوراق صفحة صفحة\n🧠 وتحاول تفتكر المهم\n\nبعد (مع ميزان برو):\n📁 ملف القضية قدامك\n🤖 ملخص الأوراق بالذكاء الاصطناعي مربوط بالملف\n✅ ووقتك يروح للدفاع\n\nاعرف أكتر 👈 mezan.pro'+TAGS,
 idea='فيديو موشن قبل/بعد: تحضير جلسة بكرة بالورق ضد ملف القضية والملخص في ميزان برو')

post('p16_1900','''
<div class="glowc" style="width:900px;height:900px;left:90px;top:100px"></div>
<div style="position:absolute;top:190px;left:130px;right:130px;height:640px;transform:rotate(-2deg)">
 <div style="position:absolute;top:-46px;right:40px;width:300px;height:80px;border-radius:20px 20px 0 0;background:#e9dfc4"></div>
 <div class="paper center" style="position:absolute;inset:0;border-radius:0 0 26px 26px;display:flex;flex-direction:column;justify-content:center;padding:50px">
  <div style="font-family:Messiri;font-size:150px;line-height:.6;height:70px;color:#b88d3a">“</div>
  <div style="font-size:64px;font-weight:900;line-height:1.5">القضية الكويسة…</div>
  <div style="font-size:64px;font-weight:900;line-height:1.5">بتبدأ <span style="color:#8a6a2c">بملف مرتّب</span></div>
  <div style="font-size:90px;margin-top:20px">📁</div>
 </div>
</div>''',pill='جملة اليوم ✨',foot='شاركها مع زميل 🤝')
add(date=D,time='19:00',kind='post',media=['p16_1900.png'],
 text='«القضية الكويسة… بتبدأ بملف مرتّب» 📁✨\n\nتتفق؟ 👇\nشاركها مع زميل بيحب الترتيب 🤝\nmezan.pro'+TAGS,
 idea='اقتباس تحفيزي: «القضية الكويسة… بتبدأ بملف مرتّب»')

sflow('s16_1100','''
<div style="font-size:120px">🤖</div>
<div style="font-size:66px;font-weight:900;line-height:1.4">قبل أول مقابلة مع موكل…<br><span class="gold">خلّي الذكاء الاصطناعي<br>يقترح عليك أسئلة</span></div>
<div class="glass" style="padding:34px 40px;margin:0 20px;text-align:right;font-size:44px;font-weight:700;line-height:1.6;border-color:rgba(217,178,95,.6)"><span class="small" style="font-size:32px">اكتب مثلًا:</span><br>«اقترح أسئلة أسألها لموكل في قضية إيجار»</div>
<div style="font-size:48px;font-weight:800;line-height:1.6">✅ إنت تختار وتزوّد من خبرتك<br>🔒 ومن غير أسماء أو بيانات شخصية</div>''',gap=46)
add(date=D,time='11:00',kind='story',media=['s16_1100.png'],idea='قصة ذكاء اصطناعي: خلّيه يقترح أسئلة لأول مقابلة مع موكل — وإنت تختار، ومن غير بيانات شخصية')

video('sv16_1500','''
<div class="sc" data-a="0" data-b="3.2">
 <div style="font-size:160px" data-fx="drop" data-at=".1">📚</div>
 <div style="font-size:88px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">أوراق القضية<br><span class="gold">كتير؟</span></div>
</div>
<div class="sc" data-a="3" data-b="6.2">
 <div style="font-size:160px" data-fx="pop" data-at=".1">🤖</div>
 <div style="font-size:80px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".4">تتلخّص<br><span class="gold">بالذكاء الاصطناعي</span></div>
</div>
<div class="sc" data-a="6" data-b="8.6">
 <div style="font-size:160px" data-fx="pop" data-at=".1">🔗</div>
 <div style="font-size:80px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".4">والملخص يتربط<br><span class="gold">بملف القضية</span></div>
</div>
'''+END_S.format(a='8.4',line='<span class="gold">ميزان برو</span><br>نظام إدارة متكامل<br>لمكتبك'),D=12,story=True)
add(date=D,time='15:00',kind='story',video=dict(src='sv16_1500',D=12,preset='a',seed=1615,bpm=124,trans='3,6,8.4',pat=3),media=['sv16_1500.mp4'],idea='قصة فيديو ميزة: أوراق كتير؟ تتلخّص بالذكاء الاصطناعي وتتربط بملف القضية')

def chip(ic,t):
    return f'<div class="glass center" style="flex:1;padding:36px 10px"><div style="font-size:96px">{ic}</div><div style="font-size:46px;font-weight:900;margin-top:10px">{t}</div></div>'
sflow('s16_2030','''
<div style="font-size:66px;font-weight:900;line-height:1.4">اسأل موكلك<br>من أول يوم:</div>
<div class="glass" style="padding:40px;margin:0 20px;font-size:62px;font-weight:900;line-height:1.4;border-color:rgba(217,178,95,.7)">«تحب أبلّغك<br>بالجديد <span class="gold">إزاي</span>؟»</div>
<div style="display:flex;gap:24px">'''+chip('📞','مكالمة')+chip('💬','رسالة')+chip('✉️','إيميل')+'''</div>
<div style="font-size:50px;font-weight:800;line-height:1.5">سؤال صغير…<br><span class="gold">بيريّح الطرفين</span> 🤝</div>''',gap=50)
add(date=D,time='20:30',kind='story',media=['s16_2030.png'],idea='قصة تعامل مع الموكلين: اسأل موكلك من أول يوم «تحب أبلّغك بالجديد إزاي؟»')

# ======================= TUE 2026-11-17 =======================
D='2026-11-17'
def nstep(a,b,n,t):
    return f'''<div class="sc" data-a="{a}" data-b="{b}">
 <div class="num" data-fx="pop" data-at=".1" style="width:110px;height:110px;font-size:60px">{n}</div>
 <div class="h1" data-fx="rise" data-at=".3" style="font-size:68px;margin-top:34px">{t}</div>
</div>'''
video('v17_1000','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">😔</div>
 <div class="h1" data-fx="rise" data-at=".4" style="font-size:76px;margin-top:20px">إزاي تقول لموكلك<br><span class="gold">خبر مش حلو</span>؟</div>
</div>
'''+nstep(3.2,6.4,1,'قوله <span class="gold">بوضوح</span><br>ومن غير لف ودوران')+nstep(6.2,9.4,2,'اشرح السبب<br><span class="gold">بكلام بسيط</span>')+nstep(9.2,12.4,3,'قول <span class="gold">الخطوة الجاية</span><br>والاختيارات المتاحة')+END_P.format(a='12.2',line='الصراحة ومعاها خطة… بتحافظ على الثقة'),D=16)
add(date=D,time='10:00',kind='post',video=dict(src='v17_1000',D=16,preset='fm',seed=1710,bpm=80,trans='3.2,6.2,9.2,12.2',pat=2),media=['v17_1000.mp4'],title='خبر مش حلو لموكلك؟ | ميزان برو',
 text='إزاي تقول لموكلك خبر مش حلو؟ 😔\n\n1️⃣ قوله بوضوح ومن غير لف ودوران\n2️⃣ اشرح السبب بكلام بسيط\n3️⃣ قول الخطوة الجاية والاختيارات المتاحة\n\nالصراحة ومعاها خطة… بتحافظ على الثقة.\nإنت بتتعامل إزاي مع الموقف ده؟ 👇\nmezan.pro'+TAGS,
 idea='فيديو موشن تعامل مع الموكلين: إزاي تقول لموكلك خبر مش حلو في 3 خطوات')

post('p17_1400_1','''
<div class="glowc" style="width:800px;height:800px;left:140px;top:180px"></div>
<div class="center" style="position:absolute;top:200px;left:60px;right:60px">
 <div style="display:inline-grid;place-items:center;width:210px;height:210px;border-radius:50%;background:rgba(217,178,95,.12);border:3px dashed rgba(217,178,95,.6);font-size:110px">⏳</div>
 <div class="h1" style="font-size:80px;margin-top:30px">اعمل قايمة<br><span class="gold">«مستني رد»</span></div>
 <div class="lead" style="margin-top:14px;font-size:34px">كل حاجة مستنيها من حد… في مكان واحد</div>
</div>''',pill='نصيحة تنظيم 🗂️',foot='اسحب ← للخطوات',dots=(1,3))
def trow(a,b,c,last=False):
    bd='' if last else 'border-bottom:1px solid #e0d8c4;'
    return ''.join(f'<div style="padding:16px;{bd}">{x}</div>' for x in (a,b,c))
post('p17_1400_2','''
<div class="box" style="top:170px"><div class="h2" style="font-size:54px">اكتب فيها 3 حاجات بس 📋</div></div>
<div class="box paper" style="top:290px;padding:26px 30px">
 <div style="display:grid;grid-template-columns:1fr 1.4fr 1fr;font-size:31px;font-weight:800">
  <div style="padding:16px;border-bottom:2px solid #c9bfa6;color:#8a6a2c">👤 مين؟</div><div style="padding:16px;border-bottom:2px solid #c9bfa6;color:#8a6a2c">📄 مستني إيه؟</div><div style="padding:16px;border-bottom:2px solid #c9bfa6;color:#8a6a2c">📅 من إمتى؟</div>
  '''+trow('الموكل','صورة العقد','السبت')+trow('زميل','نسخة المذكرة','الأحد')+trow('الخبير','موعد المعاينة','الاتنين')+trow('…','…','…',True)+'''
 </div>
</div>
<div class="box center" style="top:820px;font-size:32px;font-weight:800">سطر واحد لكل حاجة… <span class="gold">ومتشيلهاش في دماغك</span></div>''',foot='اسحب ←',dots=(2,3))
post('p17_1400_3','''
<div class="box" style="top:170px"><div class="h2" style="font-size:54px">وبعدين؟ ✅</div></div>
<div class="box col" style="top:290px;gap:26px">
 <div class="glass li" style="padding:30px 36px"><div class="num">1</div><div><div class="t" style="font-size:40px">راجعها كل يوم الصبح</div><div class="d" style="font-size:27px">دقيقتين مع القهوة ☕</div></div></div>
 <div class="glass li" style="padding:30px 36px"><div class="num">2</div><div><div class="t" style="font-size:40px">عدّى 3 أيام؟ ابعت تذكير</div><div class="d" style="font-size:27px">رسالة مهذّبة وقصيرة</div></div></div>
 <div class="glass li" style="padding:30px 36px;border-color:rgba(217,178,95,.7)"><div class="num">3</div><div><div class="t" style="font-size:40px">وصلك؟ امسحه من القايمة</div><div class="d" style="font-size:27px">وحطّه في ملف القضية 📁</div></div></div>
</div>''',foot='هتجرّبها؟ قولنا 👇 · mezan.pro',dots=(3,3))
add(date=D,time='14:00',kind='post',media=['p17_1400_1.png','p17_1400_2.png','p17_1400_3.png'],
 text='اعمل قايمة «مستني رد» ⏳\n\nكل حاجة مستنيها من حد تتكتب في مكان واحد:\n👤 مين؟\n📄 مستني منه إيه؟\n📅 من إمتى؟\n\n✅ راجعها كل يوم الصبح\n✅ عدّى 3 أيام؟ ابعت تذكير\n✅ وصلك؟ امسحه وحطّه في ملف القضية\n\nاسحب الصور ← وقولنا هتجرّبها؟ 👇\nmezan.pro'+TAGS,
 idea='كاروسيل 3 صور نصيحة تنظيم: قايمة «مستني رد» (مين/إيه/من إمتى + متابعة يومية)')

post('p17_1900','''
<div class="gold" style="position:absolute;top:110px;left:40px;font-family:Messiri;font-size:420px;line-height:1;opacity:.12">؟</div>
<div class="box" style="top:170px"><div class="tag" style="font-size:28px">أسئلة شائعة ❓</div></div>
<div class="box glass" style="top:260px;padding:34px 40px;display:flex;align-items:center;gap:26px">
 <div class="num" style="width:80px;height:80px;font-size:40px;font-family:Cairo;font-weight:900">س</div>
 <div style="font-size:52px;font-weight:900">أقدر أجرّب الأول<br>قبل ما أشترك؟</div>
</div>
<div class="box" style="top:540px;padding:34px 40px;border-radius:26px;border:2px solid rgba(217,178,95,.8);background:rgba(217,178,95,.1);display:flex;align-items:flex-start;gap:26px">
 <div class="num" style="width:80px;height:80px;font-size:40px;font-family:Cairo;font-weight:900">ج</div>
 <div style="font-size:42px;font-weight:800;line-height:1.55">أكيد 👌 فيه <span class="gold">14 يوم تجربة مجانية</span>.<br>ولما تقرّر: <span class="gold">200 ج</span> شهري<br>أو <span class="gold">2000 ج</span> سنوي.</div>
</div>''')
add(date=D,time='19:00',kind='post',media=['p17_1900.png'],
 text='❓ «أقدر أجرّب ميزان برو الأول قبل ما أشترك؟»\n\nأكيد 👌 فيه فترة تجريبية مجانية 14 يوم.\nولما تقرّر تشترك: 200 ج شهري أو 2000 ج سنوي.\n\nابدأ من هنا 👈 mezan.pro\n\nعندك سؤال تاني؟ اكتبه في الكومنتات 👇'+TAGS,
 idea='أسئلة شائعة: أقدر أجرّب الأول قبل ما أشترك؟ 14 يوم مجانًا + الأسعار')

video('sv17_1100','''
<div class="sc" data-a="0" data-b="3.4">
 <div style="font-size:150px" data-fx="pop" data-at=".1">⏰</div>
 <div style="font-size:86px;font-weight:900;line-height:1.35;margin-top:30px" data-fx="rise" data-at=".5">بتشتغل<br><span class="gold">كام ساعة</span><br>في اليوم؟</div>
</div>
<div class="sc" data-a="3.2" data-b="8.6">
 <div class="col" style="width:100%;gap:28px">
  '''+opt(1,'أقل من 8 ساعات','.3')+opt(2,'من 8 لـ 10','.8')+opt(3,'من 10 لـ 12','1.3')+opt(4,'أكتر… ومش بعدّ 😅','1.8')+'''
 </div>
</div>
'''+END_S.format(a='8.4',line='ابعتلنا <span class="gold">رقمك</span><br>في رسالة 📩'),D=12,story=True)
add(date=D,time='11:00',kind='story',video=dict(src='sv17_1100',D=12,preset='em',seed=1711,bpm=118,trans='3.2,8.4',pat=1),media=['sv17_1100.mp4'],idea='قصة فيديو تفاعلية: بتشتغل كام ساعة في اليوم؟ (4 اختيارات)')

sflow('s17_1500','''
<div style="font-size:130px">🤔</div>
<div style="font-size:72px;font-weight:900;line-height:1.4">قريت المستند…<br>ونسيت كان فيه <span class="gold">إيه</span>؟</div>
<div class="center gold" style="font-size:90px;line-height:1">⬇</div>
<div class="glass" style="padding:44px 40px;margin:0 30px;border-color:rgba(217,178,95,.7)"><div style="font-size:100px">📁</div><div style="font-size:54px;font-weight:900;line-height:1.5">ملخصه بالذكاء الاصطناعي<br><span class="gold">في ملف القضية</span></div></div>
<div style="font-size:48px;font-weight:800">ارجعله في أي وقت 👌</div>''',gap=40)
add(date=D,time='15:00',kind='story',media=['s17_1500.png'],idea='قصة مشكلة وحلها: نسيت المستند كان فيه إيه؟ ملخصه في ملف القضية')

sflow('s17_2030','''
<div style="margin:0 auto;width:300px;height:300px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle,rgba(217,178,95,.3),rgba(217,178,95,.05) 70%);border:4px solid rgba(217,178,95,.6);font-size:160px">🔒</div>
<div style="font-size:70px;font-weight:900;line-height:1.4">شغلك فيه<br><span class="gold">أسرار ناس</span></div>
<div class="glass" style="padding:44px 40px;margin:0 30px;font-size:52px;font-weight:800;line-height:1.6">وعشان كده<br>حماية البيانات وسريتها<br><span class="gold">أولوية في ميزان برو</span></div>''',gap=56)
add(date=D,time='20:30',kind='story',media=['s17_2030.png'],idea='قصة ميزة: شغلك فيه أسرار ناس… حماية البيانات وسريتها أولوية في ميزان برو')

json.dump(M,open('mw4a.json','w'),ensure_ascii=False,indent=1);print(len(M))
