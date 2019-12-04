import requests
from lxml import etree
from urllib import request
import os

if not os.path.exists('./netbian'):
    os.mkdir('./netbian')

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

start_page = int(input('start page num:'))
end_page = int(input('end page num:'))
url = 'http://pic.netbian.com/4kdongman/index_%d.html'
for page in range(start_page, end_page + 1):
    if page == 1:
        new_url = 'http://pic.netbian.com/4kdongman/'
    else:
        new_url = format(url % page)

    response = requests.get(url=new_url, headers=headers)
    # 手动设置响应数据的编码
    # response.encoding = 'utf-8'

    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        img_name = li.xpath('./a/img/@alt')[0]
        img_name = img_name.encode("iso-8859-1").decode('gbk') + '.jpg'
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_path = './netbian/' + img_name
        request.urlretrieve(img_src, img_path)
        print(img_name, 'download success!')
