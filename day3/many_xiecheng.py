# 多任务异步协程
import asyncio
import time
from time import sleep

urls = ['www.baidu.com', 'www.sogou.com', 'www.goubanjia.com']


async def request(url):
    print("正在请求:", url)
    # 在多任务异步协程实现中，不可以出现不支持异步的相关代码
    # sleep(2)
    await asyncio.sleep(2)
    print("下载成功:", url)


start = time.time()
# 任务列表: 放置多个任务对象
tasks = []
loop = asyncio.get_event_loop()
for url in urls:
    c = request(urls)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
print(time.time() - start)
