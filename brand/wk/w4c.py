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

def li(ic,t,d='',at=None,pad='26px 34px',ts=40,extra=''):
    a=f' data-fx="right" data-at="{at}"' if at is not None else ''
    dd=f'<div class="d" style="font-size:28px">{d}</div>' if d else ''
    return f'<div class="glass li"{a} style="padding:{pad};{extra}"><div class="ic">{ic}</div><div><div class="t" style="font-size:{ts}px">{t}</div>{dd}</div></div>'
