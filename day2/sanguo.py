import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

url = 'http://shicimingju.com/book/sanguoyanyi.html'

page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')
fp = open('./sanguo.txt', 'w', encoding='utf-8')

li_lists = soup.select('.book-mulu > ul > li')
for li in li_lists:
    title = li.a.string
    detail_url = 'http://shicimingju.com' + li.a['href']
    # print(title, detail_url)
    detail_page_text = requests.get(url=detail_url, headers=headers).text
    soup = BeautifulSoup(detail_page_text, 'lxml')
    content = soup.find('div', class_='chapter_content').text

    fp.write(title + '\n' + content + '\n')
    print(title, 'download success')

fp.close()
