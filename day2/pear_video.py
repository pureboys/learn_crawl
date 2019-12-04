import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool
import random

# 开启线程池
pool = Pool(4)
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
url = 'https://www.pearvideo.com/category_1'


def get_video_data(video_url):
    return requests.get(url=video_url, headers=headers).content


def save_video(data):
    name = str(random.randint(0, 9999)) + '.mp4'
    with open(name, 'wb') as fp:
        fp.write(data)
    print(name, 'download success!')


page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
video_urls = []  # 所有视频的url
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    detail_text = requests.get(url=detail_url, headers=headers).text
    ex = 'srcUrl="(.*?)",vdoUrl='
    video_src = re.findall(ex, detail_text, re.S)[0]
    video_urls.append(video_src)

# 使用异步线程池进行数据的下载
all_video_data_list = pool.map(get_video_data, video_urls)

pool.map(save_video, all_video_data_list)
