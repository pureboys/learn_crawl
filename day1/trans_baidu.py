import requests

url = "https://fanyi.baidu.com/sug"
word = input('enter a english word:')
data = {
    'kw' : word
}

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.post(url, data, headers=headers)
json = response.json()

print(json)
