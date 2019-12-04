# 多线程
import time
from multiprocessing.dummy import Pool
from time import sleep


def request(url):
    print("正在请求:", url)
    sleep(2)
    print("下载成功:", url)


start = time.time()

urls = ['www.baidu.com', 'www.sogou.com', 'www.goubanjia.com']
# for url in urls:
#     request(url)

pool = Pool(3)
pool.map(request, urls)

print(time.time() - start)
