from multiprocessing import Pool
import time
import requests
from lxml import etree

urls = [
    'https://hacks.mozilla.org/2020/04/experimental-webgpu-in-firefox/',
    'https://hacks.mozilla.org/2020/04/fuzzing-with-webidl/',
    'https://hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/',
    'https://hacks.mozilla.org/2020/05/high-performance-web-audio-with-audioworklet-in-firefox/',
    'https://hacks.mozilla.org/2020/05/building-functiontrace-a-graphical-python-profiler/'
]

titles = []

def get_title(url):
    response = requests.get(url)
    html = response.content
    title = etree.HTML(html).xpath('//h1[@class="post__title"]/text()')
    titles.append(title)
    
def main():
    print("开始python多进程测试")
    pool = Pool(4)
    for url in urls:
        pool.apply_async(get_title, (url,))
    pool.close()
    pool.join()
    
if __name__ == '__main__':
    startTime = time.time()
    main()
    print('%s总耗时：%f秒' % (titles, float(time.time()-startTime)))