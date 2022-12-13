import user_info
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
import datetime
from config import *


TOKEN = user_info.slack_token
CHANNEL = 'fujihira_test'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
  'channel': CHANNEL,
  'text': 'リモワ完了します'
}
r = requests.post(url, headers=headers, data=data)
print("return ", r.json())

CHROMEDRIVER = "C:\chromedriver.exe"
# ドライバー指定でChromeブラウザを開く
driver = webdriver.Chrome(CHROMEDRIVER)

#ウインドウサイズを変更
driver.set_window_size(1920,1080)
 
# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')
 
#ログイン画面にてクレデンシャルを入力
driver.find_element_by_xpath('//*[@id="username"]').send_keys(user_info.salesforce_id)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(user_info.salesforce_passwd)

#ログインボタンをクリック
driver.find_element_by_xpath('//*[@id="Login"]').click()
print ("ログイン完了")
time.sleep(7)

#退勤ボタンを押下
elements = driver.find_element_by_xpath('//*[@id="0665F00000117vk"]')
loc = elements.location
x, y = loc['x'], loc['y']
actions = ActionChains(driver)
actions.move_by_offset(x+715,y+50)
actions.click()
actions.click()
actions.perform()
time.sleep(5)

driver.quit()