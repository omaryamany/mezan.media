import sys
from PIL import Image
ims=[Image.open(f'out/{n}.png').convert('RGB') for n in sys.argv[2:]]
s=float(sys.argv[1]);ws=[int(i.width*s) for i in ims];h=max(int(i.height*s) for i in ims)
S=Image.new('RGB',(sum(ws)+10*len(ims),h),'white');x=0
for i,w in zip(ims,ws):S.paste(i.resize((w,int(i.height*s))),(x,0));x+=w+10
S.save('out/sheet.jpg',quality=88)
