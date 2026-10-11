import sys,asyncio,os
from playwright.async_api import async_playwright
FPS=30;D=16
async def main():
    os.makedirs('fr',exist_ok=True)
    only=[float(x) for x in sys.argv[1:]]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1080,'height':1080})
        await pg.goto('file:///home/claude/mezan.media/brand/video.html'); await pg.wait_for_timeout(800)
        ts=only or [i/FPS for i in range(FPS*D)]
        for i,t in enumerate(ts):
            await pg.evaluate(f'seek({t})')
            name=f'prev_{t}.png' if only else f'fr/{i:04d}.jpg'
            await pg.screenshot(path=name,type='png' if only else 'jpeg',quality=None if only else 95)
        await b.close()
asyncio.run(main())
