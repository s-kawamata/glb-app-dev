import user_info
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
import datetime
import requests
from selenium.webdriver import DesiredCapabilities


TOKEN = user_info.slack_token
CHANNEL = 'akatsuka_test'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
  'channel': CHANNEL,
  'text': 'リモワ開始します',
}

r = requests.post(url, headers=headers, data=data)

if "\'ok\': True" in str(r.json()):
  print("SlackへのPOST成功")
else:
  print("SlackへのPOST失敗")

#CHROMEDRIVER = "C:\chromedriver.exe"
# ドライバー指定でChromeブラウザを開く
#driver = webdriver.Chrome(CHROMEDRIVER)

driver = webdriver.Remote(
     command_executor="http://selenium:4444/wd/hub",
     desired_capabilities=DesiredCapabilities.CHROME.copy(),
 )

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

#htmlを表示
#print(driver.page_source)

#iframeを切り替える
iframe=driver.find_element_by_xpath("//*[@id='0665F00000117vk']")
driver.switch_to.frame(iframe)
driver.implicitly_wait(15)

#htmlを表示2
#print("ここからiframe切り替えてます。" + driver.page_source)

#在宅勤務ボタンを選択
y_loca = driver.find_element_by_xpath("//*[@id='workLocationButtons']/label[2]/div")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)


#出勤ボタンをクリック
y_loca = driver.find_element_by_xpath("//*[@id='btnStInput']")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)

driver.switch_to.default_content()




'''
#在宅勤務
driver.find_element_by_xpath("//label['在宅勤務']").click()
time.sleep(2)


#出勤
driver.find_element_by_xpath('//*[@id="btnStInput"]').click()
time.sleep(2)
'''

'''
#「在宅勤務」に勤務形態を登録
elements = driver.find_element_by_xpath('//*[@id="0665F00000117vk"]')
print(elements)
loc = elements.location
x, y = loc['x'], loc['y']
actions = ActionChains(driver)
actions.move_by_offset(x+210,y+65)
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
'''

driver.quit()
