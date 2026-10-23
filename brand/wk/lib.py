import os
HERE=os.path.dirname(os.path.abspath(__file__))
HEAD='<!doctype html><html lang="ar" dir="rtl"{cls}><head><meta charset="utf-8"><link rel="stylesheet" href="../base.css"><link rel="stylesheet" href="../kit.css"><style>{css}</style></head>'
LOGO='<div class="brand"><img src="../logo.svg" width="{w}"><span class="name gold" style="font-family:Messiri">ميزان برو</span></div>'

def write(name,html):
    p=os.path.join(HERE,name+'.html');open(p,'w').write(html);return p

def post(name,body,css='',pill='',foot='نظام إدارة متكامل لمكاتب المحاماة',dots=None,bg=''):
    hdr=f'<div class="hdr">{LOGO.format(w=62)}{f"<span class=pill>{pill}</span>" if pill else ""}</div>'
    d=''
    if dots: d='<div class="dots">'+''.join('<i class="on"></i>' if i==dots[0] else '<i></i>' for i in range(1,dots[1]+1))+'</div>'
    ftr=f'<div class="ftr"><span>{foot}</span><span class="url">mezan.pro</span></div>' if not dots else f'<div class="ftr" style="justify-content:flex-start"><span>{foot}</span></div>'
    html=HEAD.format(cls='',css=css)+f'<body><div class="stage" id="st"><div class="grid"></div>{bg}{hdr}{body}{d}{ftr}</div></body></html>'
    return write(name,html)

def story(name,body,css='',top=True,bg=''):
    # safe zone: nothing important above y=230 or below y=1690
    hdr=f'<div style="position:absolute;top:240px;left:0;right:0;display:flex;justify-content:center">{LOGO.format(w=64)}</div>' if top else ''
    html=HEAD.format(cls=' class="story"',css='.hdr .name,.brand .name{font-size:40px}'+css)+f'<body><div class="stage" id="st"><div class="grid"></div>{bg}{hdr}{body}</div></body></html>'
    return write(name,html)

def video(name,scenes,css='',D=16,story=False,wm=True):
    rings='<div class="ring" style="width:520px;height:520px"></div><div class="ring" style="width:760px;height:760px;opacity:.25"></div>'
    if story:
        glow='<div class="glow" id="glow" style="position:absolute;width:1200px;height:1200px;left:-60px;top:360px;border-radius:50%;background:radial-gradient(circle,rgba(217,178,95,.2),transparent 60%)"></div>'
        wmh=f'<div id="wm" data-a="0" data-b="{D-2.6}" style="position:absolute;top:230px;left:0;right:0;display:flex;justify-content:center;opacity:0">{LOGO.format(w=56)}</div>' if wm else ''
        bar='<div id="bar" style="position:absolute;top:0;right:0;height:8px;background:linear-gradient(90deg,var(--gold),var(--gold2))"></div>'
        base='.sc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:330px 70px 300px}'
        cls=' class="story"'
    else:
        glow='<div class="glow" id="glow" style="position:absolute;width:900px;height:900px;left:90px;top:90px;border-radius:50%;background:radial-gradient(circle,rgba(217,178,95,.2),transparent 60%)"></div>'
        wmh=f'<div id="wm" data-a="3" data-b="{D-3.2}" style="position:absolute;top:50px;right:60px;opacity:0">{LOGO.format(w=50)}</div>' if wm else ''
        bar='<div id="bar" style="position:absolute;bottom:0;right:0;height:6px;background:linear-gradient(90deg,var(--gold),var(--gold2))"></div>'
        base='.sc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:120px 80px}';cls=''
    css=base+'.ring{position:absolute;left:50%;top:50%;border:2px dashed rgba(217,178,95,.28);border-radius:50%;opacity:.5}'+css
    html=HEAD.format(cls=cls,css=css)+f'<body data-d="{D}"><div class="stage" id="st"><div class="grid" id="grid"></div>{glow}{rings}{wmh}{scenes}{bar}</div><script src="../engine.js"></script></body></html>'
    return write(name,html)
