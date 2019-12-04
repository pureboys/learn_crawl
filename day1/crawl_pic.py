import requests

img_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574569932234&di=1a03f4fc5760a58f9a48e0136faf4e57&imgtype=0&src=http%3A%2F%2Fpic11.nipic.com%2F20101117%2F3320946_134752173000_2.jpg'

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

img_data = requests.get(url=img_url, headers=headers).content

with open('./picture.jpg', 'wb') as fp:
    fp.write(img_data)
