from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.chrome.options import Options


# 设置无头
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 自动化标识禁止
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path='../chromedriver', options=chrome_options)
bro.get('http://125.35.6.84:81/xk/')

time.sleep(2)
page_text = bro.page_source

tree = etree.HTML(page_text)
name = tree.xpath('//*[@id="gzlist"]/li[1]/dl/a/text()')[0]
print(name)

time.sleep(3)
bro.quit()
