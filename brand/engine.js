// Generic motion engine: scenes = .sc[data-a][data-b]; animated children have data-fx + data-at (sec after scene start)
(function(){
const $=s=>document.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const eo=x=>1-Math.pow(1-x,3), eb=x=>{const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const p=(t,a,d)=>cl((t-a)/d);
const inOut=(t,a,b,f=.4)=>Math.min(eo(p(t,a,f)),1-eo(p(t,b-f,f)));
const D=parseFloat(document.body.dataset.d||16);
const scenes=$$('.sc').map(s=>({el:s,a:+s.dataset.a,b:+s.dataset.b,fx:$$('[data-fx]',s)}));
$$('[data-fx=draw]').forEach(e=>{const L=e.getTotalLength?e.getTotalLength():600;e.style.strokeDasharray=L;e.dataset.len=L});
function fx(e,t,a){
 const at=a+parseFloat(e.dataset.at||0),f=e.dataset.fx,d=parseFloat(e.dataset.d||.6),dist=parseFloat(e.dataset.dist||0);
 let k;
 switch(f){
  case 'rise':k=eo(p(t,at,d));e.style.opacity=k;e.style.transform=`translateY(${(1-k)*(dist||50)}px)`;break;
  case 'drop':k=eo(p(t,at,d));e.style.opacity=k;e.style.transform=`translateY(${-(1-k)*(dist||50)}px)`;break;
  case 'left':k=eo(p(t,at,d));e.style.opacity=k;e.style.transform=`translateX(${-(1-k)*(dist||160)}px)`;break;
  case 'right':k=eo(p(t,at,d));e.style.opacity=k;e.style.transform=`translateX(${(1-k)*(dist||160)}px)`;break;
  case 'pop':k=eb(p(t,at,d));e.style.opacity=cl(k);e.style.transform=`scale(${.4+.6*k})`;break;
  case 'stamp':k=eo(p(t,at,d*.7));e.style.opacity=k;e.style.transform=`scale(${1.7-.7*k}) rotate(${(1-k)*-8}deg)`;break;
  case 'spin':k=eb(p(t,at,d+.2));e.style.opacity=cl(k);e.style.transform=`scale(${.4+.6*k}) rotate(${(1-k)*-30}deg)`;break;
  case 'bar':k=eo(p(t,at,d));e.style.transform=`scaleX(${k})`;break;
  case 'fade':k=eo(p(t,at,d));e.style.opacity=k;break;
  case 'pulse':k=eb(p(t,at,d));e.style.opacity=cl(k);e.style.transform=`scale(${(.6+.4*k)*(1+.03*Math.sin(t*5)*cl(k))})`;break;
  case 'strike':k=eo(p(t,at,d));e.style.transform=`scaleX(${k})`;break;
  case 'count':{k=eo(p(t,at,d||1));const to=+e.dataset.to;e.textContent=Math.round(to*k);break}
  case 'draw':k=eo(p(t,at,d));e.style.strokeDashoffset=(1-k)*e.dataset.len;break;
  case 'float':k=eo(p(t,at,d));e.style.opacity=k;e.style.transform=`translateY(${(1-k)*40+6*Math.sin(t*2+at)}px)`;break;
 }
}
function seek(t){
 const g=$('#grid');if(g)g.style.transform=`translateY(${(t*9)%60}px)`;
 const gl=$('#glow');if(gl)gl.style.transform=`scale(${1+.08*Math.sin(t*1.3)})`;
 $$('.ring').forEach((r,i)=>{r.style.transform=`translate(-50%,-50%) scale(${1+.04*Math.sin(t*1.6+i)}) rotate(${t*(i?-6:8)}deg)`});
 const b=$('#bar');if(b)b.style.width=(t/D*100)+'%';
 const wm=$('#wm');if(wm){const a=wm.dataset.a!==undefined?+wm.dataset.a:3,z=wm.dataset.b!==undefined?+wm.dataset.b:(D-3.2);wm.style.opacity=inOut(t,a,z,.5)}
 for(const s of scenes){const o=inOut(t,s.a,s.b,.4);s.el.style.opacity=o;s.el.style.visibility=o>0.001?'visible':'hidden';if(o>0)s.fx.forEach(e=>fx(e,t,s.a))}
 $('#st').style.filter=`brightness(${1-.85*eo(p(t,D-.45,.45))})`;
}
window.seek=seek;seek(0);
})();
