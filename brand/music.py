import numpy as np
from scipy.signal import butter, sosfilt
SR=44100;D=16.0;N=int(SR*D);t=np.arange(N)/SR
def note(m): return 440*2**((m-69)/12)
def lp(x,fc,o=2): return sosfilt(butter(o,fc,'low',fs=SR,output='sos'),x)
def hp(x,fc,o=2): return sosfilt(butter(o,fc,'high',fs=SR,output='sos'),x)
L=np.zeros(N);R=np.zeros(N)
def add(sig,start,pan=0.0,g=1.0):
    i=int(start*SR);n=min(len(sig),N-i)
    if n<=0:return
    L[i:i+n]+=sig[:n]*g*np.sqrt((1-pan)/2);R[i:i+n]+=sig[:n]*g*np.sqrt((1+pan)/2)
bar=2.0
# Am F C G  (two passes)
chords=[[57,60,64,69],[53,57,60,65],[48,55,60,64],[55,59,62,67]]*2
roots=[45,41,48,43]*2
rng=np.random.default_rng(3)
# pad
for b,ch in enumerate(chords):
    dur=bar+0.6;tt=np.arange(int(dur*SR))/SR
    env=np.minimum(1,tt/0.5)*np.minimum(1,(dur-tt)/0.6)
    for m in ch:
        for det,pan in [(-0.08,-0.6),(0.08,0.6)]:
            f=note(m)*2**(det/12)
            s=sum(np.sin(2*np.pi*f*k*tt+rng.uniform(0,6))/k for k in range(1,7))
            add(lp(s,1400)*env*0.035,b*bar,pan)
# arp (8th notes) from bar 1
pat=[0,1,2,3,2,1,3,2]
for b,ch in enumerate(chords):
    if b<1:continue
    for k in range(8):
        m=ch[pat[k]]+12;st=b*bar+k*0.25;dur=0.5;tt=np.arange(int(dur*SR))/SR
        env=np.exp(-tt*9)*np.minimum(1,tt/0.004)
        s=(np.sin(2*np.pi*note(m)*tt)+0.3*np.sin(2*np.pi*note(m)*2*tt))*env
        pan=0.35 if k%2 else -0.35
        add(s*0.10,st,pan);add(s*0.04,st+0.375,-pan)  # delay echo
# bass
for b,r in enumerate(roots):
    if b<1:continue
    for k in [0,1.5,2,3]:
        st=b*bar+k*0.5;dur=0.45;tt=np.arange(int(dur*SR))/SR
        env=np.minimum(1,tt/0.01)*np.exp(-tt*3)
        s=np.sin(2*np.pi*note(r-12)*tt)+0.25*np.sin(2*np.pi*note(r)*tt)
        add(lp(s,300)*env*0.32,st)
# drums from t=3
def kick():
    tt=np.arange(int(.4*SR))/SR;f=50+110*np.exp(-tt*28)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*9)
def hat():
    tt=np.arange(int(.08*SR))/SR;return hp(rng.standard_normal(len(tt)),7000)*np.exp(-tt*55)
def clap():
    tt=np.arange(int(.25*SR))/SR;return lp(hp(rng.standard_normal(len(tt)),1200),5000)*np.exp(-tt*18)
for beat in range(6,32):
    st=beat*0.5
    if st>=15.4:break
    add(kick(),st,0,0.55)
    add(hat(),st+0.25,0.3,0.10)
    if beat%2==1:add(clap(),st,-0.1,0.13)
# risers before transitions
def riser(d):
    n=int(d*SR);tt=np.arange(n)/SR;x=rng.standard_normal(n)
    out=np.zeros(n);seg=2048
    for i in range(0,n,seg):
        fc=300+6000*(i/n)**2;out[i:i+seg]=lp(x[i:i+seg],fc)
    return out*(tt/d)**2
for tr in [3.0,6.6,10.0,12.8]:
    add(riser(0.8),tr-0.8,0,0.12)
# impacts
def impact():
    tt=np.arange(int(2.0*SR))/SR;f=40+60*np.exp(-tt*10)
    boom=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*2.2)
    sh=lp(rng.standard_normal(len(tt)),3000)*np.exp(-tt*6)*0.4
    return boom+sh
add(impact(),0.15,0,0.45);add(impact(),13.0,0,0.40)
# shimmer on logo
tt=np.arange(int(2*SR))/SR
add(sum(np.sin(2*np.pi*note(m)*tt) for m in [81,84,88])*np.exp(-tt*1.5)*0.03,0.2,0.2)
mix=np.stack([L,R],1)
fade=np.ones(N);fs=int(1.0*SR);fade[-fs:]=np.linspace(1,0,fs)**1.5;mix*=fade[:,None]
mix=np.tanh(mix*1.4)/np.tanh(1.4);mix/=np.max(np.abs(mix))*1.12
from scipy.io import wavfile
wavfile.write('music.wav',SR,(mix*32767).astype(np.int16))
print('ok')
