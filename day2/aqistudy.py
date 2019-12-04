import requests
from lxml import etree
from urllib import request

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)

# hot_city = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')[0]
# all_city = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')
# print(all_city)

all_city = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text() | //div[@class="bottom"]/ul/li/a/text()')
