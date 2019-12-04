import requests
import re
from urllib import request
import os

if not os.path.exists('./bgm'):
    os.mkdir('./bgm')

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

url = 'https://bgm.tv/anime/browser?sort=rank&page=1'
page_text = requests.get(url=url, headers=headers).text

ex = '<span class="image">.*?<img src="(.*?)" .*?>.*?</span>'
img_url = re.findall(ex, page_text, re.S)

opener = request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')

for url in img_url:
    url = 'https:' + url
    image_name = url.split('/')[-1]
    image_path = './bgm/' + image_name
    opener.retrieve(url, image_path)
    print(image_name, 'download success!')
