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
  elm = driver.find_element_by_xpath('//*[@id="phSearchContainer"]/div/div[1]')
  if elm :
    pass 
  else :
    raise ValueError("ログインに失敗しました")
except NoSuchElementException as e:
  print(e)

print("ログイン完了しました")
time.sleep(7)

print("処理開始します。")

#勤務表のタブをクリック
driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()
driver.implicitly_wait(5)

#繰り返し処理を開始
i=0
content = driver.find_elements_by_css_selector('.tele')
days = len(content)
print(days)

while i < days:
    print("処理スタート")
    print(i)

    #日付の欄まで縦スクロール、クリック
    elements = driver.find_elements_by_css_selector('.tele')[i]
    driver.execute_script("window.scrollTo(0, " + str(elements.location['y']) + ");")
    elements.click()
    time.sleep(5)

    print("日時が選択されました")

    #「勤務場所」入力欄まで移動
    kinmu_place = driver.find_element_by_xpath('//*[@id="workLocationId"]')
    print (kinmu_place)
    driver.execute_script("window.scrollTo(0, " + str(kinmu_place.location['y']) + ");")

    #「勤務場所」から「在宅勤務」を選択する
    select = Select(kinmu_place)
    select.select_by_value('a2B5F00000OkMUPUA3')#←文字の方がいい
    #select.select_by_value('')  #←空白

    #登録ボタンクリック
    driver.find_element_by_xpath('//*[@id="dlgInpTimeOk"]').click()
    i+=1
    print("登録ボタンが押されました")

    time.sleep(5)

else:
#処理対象が存在しない時の処理
#完了処理
    print("処理が正常に完了しました。")
    driver.quit()
