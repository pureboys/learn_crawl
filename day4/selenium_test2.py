from selenium import webdriver
from lxml import etree
import time

bro = webdriver.Chrome(executable_path='../chromedriver')
bro.get('https://www.taobao.com/')

time.sleep(2)
input_text = bro.find_element_by_id('q')
input_text.send_keys('mac pro')

time.sleep(2)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)


btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

time.sleep(3)
bro.quit()
