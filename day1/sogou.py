import requests

url = "http://www.sogou.com"
response = requests.get(url)
page_text = response.text

with open("./sogou.html", "w", encoding="utf-8") as fp:
    fp.write(page_text)

print("over!")
