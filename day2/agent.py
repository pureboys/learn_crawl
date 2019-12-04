import requests
import random

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

http = [
    {'http': '59.57.148.28:9999'},
    {'http': '59.57.148.28:9999'},
]

https = [
    {'https': '59.57.148.28:9999'},
    {'https': '59.57.148.28:9999'},
]

url = 'https://www.baidu.com/s?wd=ip'

if url.split(':')[0] == 'https':
    page_text = requests.get(url=url, headers=headers, proxies=random.choice(https)).text
else:
    page_text = requests.get(url=url, headers=headers, proxies=random.choice(http)).text

with open('./ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
