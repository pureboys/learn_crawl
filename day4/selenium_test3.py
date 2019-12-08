from selenium import webdriver
from selenium.webdriver import ActionChains
import time

bro = webdriver.Chrome(executable_path='../chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

bro.switch_to.frame('iframeResult')
div_tag = bro.find_element_by_id('draggable')

action = ActionChains(bro)
action.click_and_hold(div_tag)

for i in range(5):
    action.move_by_offset(17, 0).perform()  # perform()立即执行动作链
    time.sleep(0.5)

bro.quit()
