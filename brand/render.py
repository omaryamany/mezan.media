"""استخدام:
  صورة:  python3 render.py img <file.html> <out.png> [W H]
  فيديو: python3 render.py vid <file.html> <frames_dir> <seconds> [W H]
  معاينة فيديو: python3 render.py prev <file.html> <out_prefix> <t1,t2,...> [W H]"""
import sys,asyncio,os
from playwright.async_api import async_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
async def main():
    mode,f=sys.argv[1],sys.argv[2]
    args=sys.argv[3:]
    W,H=1080,1080
    if mode=='img': out=args[0]; rest=args[1:]
    else: out=args[0]; extra=args[1]; rest=args[2:]
    if rest: W,H=int(rest[0]),int(rest[1])
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':W,'height':H})
        await pg.goto('file://'+os.path.join(HERE,f)); await pg.wait_for_timeout(800)
        if mode=='img':
            await pg.screenshot(path=out)
        elif mode=='prev':
            for t in extra.split(','):
                await pg.evaluate(f'seek({t})'); await pg.screenshot(path=f'{out}_{t}.png')
        else:
            os.makedirs(out,exist_ok=True)
            for i in range(int(float(extra)*30)):
                await pg.evaluate(f'seek({i/30})'); await pg.screenshot(path=f'{out}/{i:04d}.jpg',type='jpeg',quality=95)
        await b.close()
asyncio.run(main())
