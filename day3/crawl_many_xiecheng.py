import requests
import asyncio
import time
import aiohttp

urls = [
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/tom',
]


# 单线程 + 多任务异步协程

async def get_pageText(url):
    # print('正在下载:', url)
    # requests不支持异步操作的
    # page_text = requests.get(url).text
    # print('下载完毕:', url)
    # return page_text

    # 代理操作  async with await s.get(url, proxy="http://ip:port") as response:
    async with aiohttp.ClientSession() as s:
        async with await s.get(url) as response:
            page_text = await response.text()
            # print(page_text)
            # 借助与回调函数进行响应数据的解析操作
            return page_text


def parse(my_task):
    # 1. 获取响应数据
    page_text = my_task.result()
    print('page_text:', page_text)


start = time.time()
tasks = []
for url in urls:
    c = get_pageText(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start)
