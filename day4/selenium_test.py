from selenium import webdriver
from lxml import etree
import time

bro = webdriver.Chrome(executable_path='../chromedriver')
bro.get('http://125.35.6.84:81/xk/')

time.sleep(2)
page_text = bro.page_source

tree = etree.HTML(page_text)
name = tree.xpath('//*[@id="gzlist"]/li[1]/dl/a/text()')[0]
print(name)

time.sleep(3)
bro.quit()
