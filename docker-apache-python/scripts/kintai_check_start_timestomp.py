from selenium import webdriver
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import list
import sys
sys.path.append("/Users/akatsukatakukai/Documents/working/kinmu_Bot")

#今日の日付を取得し、要素検索用に加工

today = date.today()
print(today)
startTimeElement = "ttvTimeSt" + str(today)
print(startTimeElement)


CHROMEDRIVER = "C:\chromedriver.exe"
# ドライバー指定でChromeブラウザを開く
driver = webdriver.Chrome(ChromeDriverManager().install())

# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')

time.sleep(2)

driver.find_element_by_xpath('//*[@id="username"]').send_keys("xxxxx")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("xxxxx")

time.sleep(2)

#ログインボタンをクリック
driver.find_element_by_xpath('//*[@id="Login"]').click()

time.sleep(2)

#勤務表のタブをクリック
driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()

driver.implicitly_wait(10)


#メンバリスト分繰り返し処理を開始
for i in list.nameList:

    #社員名横のプルダウンをクリック
    driver.find_element_by_xpath('//*[@id="empListButton"]').click()

    time.sleep(3)



    #別ウインドウをアクティブに
    newhandles = driver.window_handles
    driver.switch_to.window(newhandles [1])

    time.sleep(3)


    #メンバ名を検索、クリック
    driver.find_element_by_link_text(i).click()


    #元のウインドウに戻る
    driver.switch_to.window(newhandles [0])

    time.sleep(3)



    #勤務開始の要素を確認し、未入力であればフラグを立てる
    
    status = driver.find_element_by_id(startTimeElement).get_attribute("textContent")

    if status == '':
        print(i + 'さんはまだ本日の勤怠開始を打刻していません')
    else :
        print(i + 'さんはすでに本日の勤怠開始を打刻しています')
    

#完了処理
driver.quit()




