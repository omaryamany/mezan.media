"""python3 rend.py img name...      -> out/name.png
   python3 rend.py prev name t1,t2..  -> out/prev_name.png (contact sheet)
   python3 rend.py vid name D        -> out/name.mp4 (needs out/name.wav)"""
import sys,asyncio,os,subprocess,shutil
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__));OUT=os.path.join(HERE,'out');os.makedirs(OUT,exist_ok=True)
def size(name):
    return (1080,1920) if 'class="story"' in open(f'{HERE}/{name}.html').read() else (1080,1080)
async def page(b,name):
    W,H=size(name);pg=await b.new_page(viewport={'width':W,'height':H})
    await pg.goto(f'file://{HERE}/{name}.html');await pg.evaluate('document.fonts.ready');await pg.wait_for_timeout(700);return pg
async def main():
    mode=sys.argv[1]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        if mode=='img':
            async def one(n):
                pg=await page(b,n);await pg.screenshot(path=f'{OUT}/{n}.png');await pg.close()
            await asyncio.gather(*[one(n) for n in sys.argv[2:]])
        elif mode=='prev':
            n=sys.argv[2];ts=sys.argv[3].split(',');pg=await page(b,n)
            for t in ts:
                await pg.evaluate(f'seek({t})');await pg.screenshot(path=f'{OUT}/_{n}_{t}.png')
            from PIL import Image
            ims=[Image.open(f'{OUT}/_{n}_{t}.png') for t in ts];W,H=ims[0].size;s=0.33
            S=Image.new('RGB',(int(W*s)*len(ims),int(H*s)))
            for i,im in enumerate(ims):S.paste(im.convert('RGB').resize((int(W*s),int(H*s))),(i*int(W*s),0))
            S.save(f'{OUT}/prev_{n}.jpg',quality=85)
            for t in ts: os.remove(f'{OUT}/_{n}_{t}.png')
        elif mode=='vid':
            n=sys.argv[2];D=float(sys.argv[3]);fd=f'{OUT}/fr_{n}';os.makedirs(fd,exist_ok=True);pg=await page(b,n)
            for i in range(int(D*30)):
                await pg.evaluate(f'seek({i/30})');await pg.screenshot(path=f'{fd}/{i:04d}.jpg',type='jpeg',quality=93)
            await b.close()
            subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',f'{fd}/%04d.jpg','-i',f'{OUT}/{n}.wav','-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',f'{OUT}/{n}.mp4'],check=True)
            shutil.rmtree(fd);print('video',n);return
        await b.close()
asyncio.run(main())
