"""python3 music_gen.py out.wav D preset seed bpm "t1,t2,.." [pat]
Variant of brand/music.py: different progressions / tempo / seed / arp pattern per video."""
import sys,numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
out,D,preset,seed,bpm=sys.argv[1],float(sys.argv[2]),sys.argv[3],int(sys.argv[4]),float(sys.argv[5])
trans=[float(x) for x in sys.argv[6].split(',')] if len(sys.argv)>6 and sys.argv[6] else []
patn=int(sys.argv[7]) if len(sys.argv)>7 else 0
P={ # chord voicings (midi) per bar, bass roots
 'em':([[52,55,59,64],[48,52,55,60],[55,59,62,67],[50,54,57,62]],[40,36,43,38]),            # Em C G D
 'dm':([[50,53,57,62],[46,50,53,58],[48,52,55,60],[45,49,52,57]],[38,34,36,33]),            # Dm Bb C A
 'c' :([[48,52,55,60],[45,48,52,57],[53,57,60,65],[55,59,62,67]],[36,33,41,43]),            # C Am F G
 'fm':([[53,56,60,65],[49,53,56,61],[51,55,58,63],[48,52,55,60]],[41,37,39,36]),            # Fm Db Eb C
 'g' :([[55,59,62,67],[52,55,59,64],[48,52,55,60],[50,54,57,62]],[43,40,36,38]),            # G Em C D
 'bm':([[47,50,54,59],[43,47,50,55],[50,54,57,62],[45,49,52,57]],[35,31,38,33]),            # Bm G D A
 'a' :([[57,61,64,69],[54,57,61,66],[50,54,57,62],[52,56,59,64]],[45,42,38,40]),            # A F#m D E
 'cm':([[48,51,55,60],[44,48,51,56],[46,50,53,58],[43,47,50,55]],[36,32,34,31]),            # Cm Ab Bb G
 'f' :([[53,57,60,65],[50,53,57,62],[46,50,53,58],[48,52,55,60]],[41,38,34,36]),            # F Dm Bb C
 'am2':([[57,60,64,69],[55,59,62,67],[53,57,60,65],[52,56,59,64]],[45,43,41,40]),           # Am G F E
}
SR=44100;N=int(SR*D)
beat=60/bpm;bar=beat*4
chords,roots=P[preset]
nb=int(np.ceil(D/bar))+1
chords=(chords*8)[:nb];roots=(roots*8)[:nb]
def note(m): return 440*2**((m-69)/12)
def lp(x,fc,o=2): return sosfilt(butter(o,fc,'low',fs=SR,output='sos'),x)
def hp(x,fc,o=2): return sosfilt(butter(o,fc,'high',fs=SR,output='sos'),x)
L=np.zeros(N);R=np.zeros(N)
def add(sig,start,pan=0.0,g=1.0):
    i=int(start*SR);n=min(len(sig),N-i)
    if n<=0 or i<0:return
    L[i:i+n]+=sig[:n]*g*np.sqrt((1-pan)/2);R[i:i+n]+=sig[:n]*g*np.sqrt((1+pan)/2)
rng=np.random.default_rng(seed)
bright=rng.uniform(1100,2000)
for b,ch in enumerate(chords):
    dur=bar+0.6;tt=np.arange(int(dur*SR))/SR
    env=np.minimum(1,tt/0.5)*np.minimum(1,np.maximum(0,(dur-tt)/0.6))
    for m in ch:
        for det,pan in [(-0.08,-0.6),(0.08,0.6)]:
            f=note(m)*2**(det/12)
            s=sum(np.sin(2*np.pi*f*k*tt+rng.uniform(0,6))/k for k in range(1,7))
            add(lp(s,bright)*env*0.032,b*bar,pan)
pats=[[0,1,2,3,2,1,3,2],[0,2,1,3,0,2,3,1],[3,2,1,0,1,2,3,2],[0,1,3,1,2,1,3,1],[0,3,2,3,1,3,2,3]]
pat=pats[patn%len(pats)]
step=beat/2;tone=rng.choice([0.25,0.35,0.5])
for b,ch in enumerate(chords):
    if b<1:continue
    for k in range(8):
        m=ch[pat[k]]+12;st=b*bar+k*step;dur=0.5;tt=np.arange(int(dur*SR))/SR
        env=np.exp(-tt*9)*np.minimum(1,tt/0.004)
        s=(np.sin(2*np.pi*note(m)*tt)+tone*np.sin(2*np.pi*note(m)*2*tt))*env
        pan=0.35 if k%2 else -0.35
        add(s*0.10,st,pan);add(s*0.04,st+step*1.5,-pan)
bpat=rng.choice([[0,1.5,2,3],[0,1,2,3],[0,2,2.5,3.5],[0,0.5,2,3]])
for b,r in enumerate(roots):
    if b<1:continue
    for k in bpat:
        st=b*bar+k*beat;dur=beat*0.9;tt=np.arange(int(dur*SR))/SR
        env=np.minimum(1,tt/0.01)*np.exp(-tt*3)
        s=np.sin(2*np.pi*note(r-12)*tt)+0.25*np.sin(2*np.pi*note(r)*tt)
        add(lp(s,300)*env*0.32,st)
def kick():
    tt=np.arange(int(.4*SR))/SR;f=50+110*np.exp(-tt*28)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*9)
def hat():
    tt=np.arange(int(.08*SR))/SR;return hp(rng.standard_normal(len(tt)),7000)*np.exp(-tt*55)
def clap():
    tt=np.arange(int(.25*SR))/SR;return lp(hp(rng.standard_normal(len(tt)),1200),5000)*np.exp(-tt*18)
start=trans[0] if trans else bar
bt=0
while True:
    st=start+bt*beat
    if st>=D-0.6:break
    add(kick(),st,0,0.5)
    add(hat(),st+beat/2,0.3,0.10)
    if patn%2: add(hat(),st+beat*0.75,-0.3,0.05)
    if bt%2==1:add(clap(),st,-0.1,0.13)
    bt+=1
def riser(d):
    n=int(d*SR);tt=np.arange(n)/SR;x=rng.standard_normal(n)
    o=np.zeros(n);seg=2048
    for i in range(0,n,seg):
        fc=300+6000*(i/n)**2;o[i:i+seg]=lp(x[i:i+seg],fc)
    return o*(tt/d)**2
for tr in trans: add(riser(0.8),tr-0.8,0,0.12)
def impact():
    tt=np.arange(int(2.0*SR))/SR;f=40+60*np.exp(-tt*10)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*2.2)+lp(rng.standard_normal(len(tt)),3000)*np.exp(-tt*6)*0.4
add(impact(),0.15,0,0.45)
if trans: add(impact(),trans[-1],0,0.4)
tt=np.arange(int(2*SR))/SR
top=chords[0][-1]+12
add(sum(np.sin(2*np.pi*note(m)*tt) for m in [top,top+3+rng.integers(0,2),top+7])*np.exp(-tt*1.5)*0.03,0.2,0.2)
mix=np.stack([L,R],1)
fade=np.ones(N);fs=int(1.0*SR);fade[-fs:]=np.linspace(1,0,fs)**1.5;mix*=fade[:,None]
mix=np.tanh(mix*1.4)/np.tanh(1.4);mix/=np.max(np.abs(mix))*1.12
wavfile.write(out,SR,(mix*32767).astype(np.int16));print('ok',out)
