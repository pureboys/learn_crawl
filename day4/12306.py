from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

bro = webdriver.Chrome(executable_path=r'../chromedriver')
bro.get('https://kyfw.12306.cn/otn/login/init')

time.sleep(2)
code_img_ele = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
time.sleep(2)

location = code_img_ele.location
print('this location is:', location)

size = code_img_ele.size
print('this size is:', size)

rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height'])
)

bro.save_screenshot('aa.png')
i = Image.open('./aa.png')

code_img_name = 'code.png'
frame = i.crop(rangle)
frame.save(code_img_name)

# use 超级鹰

all_list = []  # [[x,y], [x1,y1], [x2,y2]]

for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()

bro.find_element_by_id('username').send_keys('xxxxxx')
time.sleep(2)
bro.find_element_by_id('password').send_keys('xxxxxxx')
time.sleep(2)
bro.find_element_by_id('loginSub').click()
time.sleep(4)

