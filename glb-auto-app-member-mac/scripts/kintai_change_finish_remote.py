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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


TOKEN = user_info.slack_token
CHANNEL = 'akatsuka_test'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
  'channel': CHANNEL,
  'text': 'リモワ完了します'
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

#ログイン開始
try:
  #ログイン画面にてクレデンシャルを入力
  driver.find_element_by_xpath('//*[@id="username"]').send_keys(user_info.salesforce_id)
  driver.find_element_by_xpath('//*[@id="password"]').send_keys(user_info.salesforce_passwd)
  #ログインボタンをクリック
  driver.find_element_by_xpath('//*[@id="Login"]').click()
  time.sleep(5)

  #2段階認証を求められた場合は2分の認証時間を設ける
  auth_check = driver.find_elements_by_xpath("//*[contains(text(), 'モバイルデバイスを確認')]")
  if auth_check:
    wait = WebDriverWait(driver, 120)
    wait.until(expected_conditions.invisibility_of_element_located((By.ID, "header")))
  else:
    pass
  
  #お知らせウィンドウが開いていた場合は閉じる
  notification_window = driver.find_elements_by_xpath("//div[@data-dojo-attach-point='titleBar']/*[contains(text(), 'お知らせ')]")
  
  if notification_window:
    y_loca = driver.find_element_by_xpath("//tr[@id='dialogInfoBottom']//button[@class='std-button2 close_button']")
    driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
    y_loca.click()
  else:
    pass
    
  time.sleep(5)
  elm = driver.find_element_by_xpath('//*[@id="phSearchContainer"]/div/div[1]')
  if elm :
    pass 
  else :
    raise ValueError("ログインに失敗しました")
except NoSuchElementException as e:
  print(e)

print("ログイン完了しました")
time.sleep(7)

#iframeを切り替える
iframe=driver.find_element_by_xpath("//*[@id='0665F00000117vk']")
driver.switch_to.frame(iframe)
driver.implicitly_wait(15)

#htmlを表示2
#print("ここからiframe切り替えてます。" + driver.page_source)

#退勤ボタンをクリック
y_loca = driver.find_element_by_xpath("//*[@id='btnEtInput']")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)

driver.switch_to.default_content()

#完了処理
print("処理が正常に完了しました。")
driver.quit()
