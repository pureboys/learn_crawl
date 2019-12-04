import requests

city = input('enter a city:')

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
data = {
    'cname': '',
    'pid': '',
    'keyword': city,
    'pageIndex': '1',
    'pageSize': '10'
}

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.post(url, data, headers=headers)
json_text = response.text

print(json_text)
