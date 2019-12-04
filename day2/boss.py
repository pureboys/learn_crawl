import requests
from lxml import etree

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

session = requests.Session()
session.get(url='https://www.zhipin.com', headers=headers)

url = 'https://www.zhipin.com/job_detail/?query=python%E5%AE%9E%E4%B9%A0&city=101010100&industry=&position='
response = session.get(url=url, headers=headers)
response.encoding = "utf-8"
page_text = response.text

print(page_text)

tree = etree.HTML(page_text)
li_lists = tree.xpath('//div[@class="job-list"]/ul/li')
for li in li_lists:
    title = li.xpath('.//div[@class="job-title"/text()]')[0]
    salary = li.xpath('.//span[@class="red"]/text()')[0]
    company = li.xpath('.//div[@class="company-text/h3/a/text()"]')[0]
