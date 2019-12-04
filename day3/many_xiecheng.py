# 协程
import asyncio


async def request(url):
    print("正在请求:", url)
    print("下载成功:", url)


c = request('www.baidu.com')

# 实例化一个事件循环对象
loop = asyncio.get_event_loop()
# 创建一个任务对象 将协程对象封装到了任务对象中
# task = loop.create_task(c)

# 另一种形式实例化任务对象的方法
task = asyncio.ensure_future(c)

# 将协程对象注册到事件循环对象中，并且我们需要启动事件循环对象
loop.run_until_complete(task)
