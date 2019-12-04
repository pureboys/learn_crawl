import requests

wd = input("enter a word:")
url = "http://www.sogou.com/web"

param = {
    "query": wd
}

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.get(url, param, headers=headers)
response.encoding = "utf-8"

page_text = response.text
file_name = wd + ".html"

with open(file_name, "w", encoding="utf-8") as fp:
    fp.write(page_text)

print(file_name, "爬取成功！！")
