import datetime
import time

#import chromedriver_binary
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome import service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait

import user_info

# TOKEN = user_info.slack_token
# CHANNEL = 'akatsuka_test'

# url = "https://slack.com/api/chat.postMessage"
# headers = {"Authorization": "Bearer "+TOKEN}
# data  = {
#   'channel': CHANNEL,
#   'text': ''+ user_info.destination_station +'退館します'
# }

# r = requests.post(url, headers=headers, data=data)

# if "\'ok\': True" in str(r.json()):
#   print("SlackへのPOST成功")
# else:
#   print("SlackへのPOST失敗")

# #ドライバー指定でChromeブラウザを開く
# CHROMEDRIVER = "C:\chromedriver.exe"
# driver = webdriver.Chrome(CHROMEDRIVER)

driver = webdriver.Remote(
     command_executor="http://selenium:4444/wd/hub",
     desired_capabilities=DesiredCapabilities.CHROME.copy(),
 )

#ウインドウサイズを変更
driver.set_window_size(1920,1080)

# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')

#ログイン開始
try:
  #ログイン画面にてクレデンシャルを入力
  driver.find_element_by_xpath('//*[@id="username"]').send_keys(user_info.salesforce_id)
  driver.find_element_by_xpath('//*[@id="password"]').send_keys(user_info.salesforce_passwd)
  #ログインボタンをクリック
  driver.find_element_by_xpath('//*[@id="Login"]').click()
  time.sleep(5)

  #指定したdriverに対して最大で10秒間待つように設定する
  wait = WebDriverWait(driver, 120)
  wait.until(expected_conditions.invisibility_of_element_located((By.ID, "//*[contains(text(), 'モバイルデバイスを確認')]")))
  time.sleep(5)
  #指定された要素が非表示になるまで待機する(要素は約5秒後に非表示になる)
  elm = driver.find_element_by_xpath('//*[@id="phSearchContainer"]/div/div[1]')
  if elm :
    pass 
  else :
    raise ValueError("ログインに失敗しました")
except NoSuchElementException as e:
  print(e)

print("ログイン完了しました")
time.sleep(10)

print("処理開始します。")
#iframeを切り替える
iframe=driver.find_element_by_xpath("//*[@id='0665F00000117vk']")
driver.switch_to.frame(iframe)
driver.implicitly_wait(15)

#退勤ボタンをクリック
y_loca = driver.find_element_by_xpath("//*[@id='btnEtInput']")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)

driver.switch_to.default_content()

#完了処理
print("処理が正常に完了しました。")
driver.quit()
