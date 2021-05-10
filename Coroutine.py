import time
from lxml import etree
import aiohttp
import asyncio
import nest_asyncio

nest_asyncio.apply()

urls = [
    'https://hacks.mozilla.org/2020/04/experimental-webgpu-in-firefox/',
    'https://hacks.mozilla.org/2020/04/fuzzing-with-webidl/',
    'https://hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/',
    'https://hacks.mozilla.org/2020/05/high-performance-web-audio-with-audioworklet-in-firefox/',
    'https://hacks.mozilla.org/2020/05/building-functiontrace-a-graphical-python-profiler/'
]

sem = asyncio.Semaphore(5) 

async def get_title(url):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.request('GET', url) as resp:
                html = await resp.read()
                title = etree.HTML(html).xpath('//h1[@class="post__title"]/text()')
                print(''.join(title))

def main():
    print("开始python协程测试")
    loop = asyncio.get_event_loop()
    tasks = [get_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    startTime = time.time()
    main()
    print('总耗时：%f秒' % float(time.time()-startTime))