import user_info
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
import datetime
import requests
from config import *


TOKEN = user_info.slack_token
CHANNEL = 'fujihira_test'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
  'channel': CHANNEL,
  'text': 'リモワ開始します\n本日は'  + user_info.destination_station +'出社です'
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


#「在宅勤務4h未満」に勤務形態を登録
print(elements)
loc = elements.location
x, y = loc['x'], loc['y']
actions = ActionChains(driver)
actions.move_by_offset(x+305,y+65)
actions.click()
actions.click()
actions.perform()
time.sleep(5)
actions.reset_actions()

#出勤ボタンを押下
elements = driver.find_element_by_xpath('//*[@id="0665F00000117vk"]')
loc = elements.location
x, y = loc['x'], loc['y']
actions = ActionChains(driver)
actions.move_by_offset(x+650,y+50)
actions.click()
actions.click()
actions.perform()
time.sleep(5)

#経費申請画面に遷移
elements = driver.find_element_by_xpath('//*[@id="01r5F000000g5DF_Tab"]/a')
loc = elements.location
x, y = loc['x'], loc['y']
actions = ActionChains(driver)
actions.move_by_offset(x,y)
actions.click()
actions.perform()
time.sleep(5)

#+ボタンを押下
driver.find_element_by_xpath('//*[@id="expApplyForm0"]/div[6]/table/tfoot/tr[4]/td/table/tr/td[1]/div/button').click()
time.sleep(10)

#利用日を入力
today = datetime.date.today()
year = today.year
month = today.month
day = today.day
driver.find_element_by_xpath('//*[@id="DlgDetailDate"]').clear()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="DlgDetailDate"]').send_keys(year, "/", month, "/", day)
time.sleep(5)

#費目を選択
element = driver.find_element_by_xpath('//*[@id="DlgDetailExpItem"]')
time.sleep(5)
#タブを選択する為の処理
select = Select(element)
driver.implicitly_wait(5)
select.select_by_value('a1M5F00000S8BBiUAN')#交通費を選択
time.sleep(5)

driver.find_element_by_xpath('//*[@id="DlgExpDetailStFrom"]').send_keys("user_info.departure_station")#出発駅を入力
driver.find_element_by_xpath('//*[@id="DlgExpDetailStTo"]').send_keys("user_info.destination_station")#到着駅を入力
time.sleep(5)

#虫眼鏡をクリック
driver.find_element_by_xpath('//*[@id="dijit_Dialog_1"]/div[2]/div/div[2]/div[3]/div[2]/div/input[2]').click()
driver.find_element_by_xpath('//*[@id="expSearchOk"]').click()
driver.find_element_by_xpath('//*[@id="expSearchOk"]/div').click()
time.sleep(5)

#往復ボタンを押下
driver.find_element_by_xpath('//*[@id="dijit_Dialog_1"]/div[2]/div/div[2]/div[3]/div[2]/div/input[1]').click()
time.sleep(5)

#OKを押下
driver.find_element_by_xpath('//*[@id="dijit_Dialog_1"]/div[2]/div/div[3]/div[2]/button[1]/div').click()
time.sleep(5)

#保存を押下
driver.find_element_by_xpath('//*[@id="tsfArea"]/div[4]/div[2]/table/tbody/tr/td[8]/button').click()
time.sleep(5)

driver.quit()