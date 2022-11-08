from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import user_info
import user_list


# ドライバー指定でChromeブラウザを開く
CHROMEDRIVER = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(ChromeDriverManager().install())
 
# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')

driver.find_element_by_xpath('//*[@id="username"]').send_keys(user_info.salesforce_id)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(user_info.salesforce_passwd)

#ログインボタンをクリック
driver.find_element_by_xpath('//*[@id="Login"]').click()


for user in user_list.nameList:
    #勤務表のタブをクリック
    driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="empListButton"]').click()

    #別ウインドウをアクティブに
    newhandles = driver.window_handles
    driver.switch_to.window(newhandles[1])

    time.sleep(5)

    #メンバ名を検索、クリック
    driver.find_element_by_link_text(user).click()

    driver.switch_to.window(newhandles[0])

    time.sleep(5)

    #時間外超過時間を摘出
    value = driver.find_element_by_xpath("//*[contains(text(), '当月度の超過時間＋法定休日労働時間')]/../../td[2]").text
    #:より前を切り出す
    target = ':'
    idx = value.find(target)
    exceed_time = int(value[:idx]) 


    if exceed_time < 25:
        print(user + "さんの現在の超過時間:" + str(exceed_time) )
        print("問題なし")

    elif exceed_time >= 25:
        print(user + "さんの現在の超過時間:" + str(exceed_time) )
        print("要注意")

    elif exceed_time >= 35:
        print(user + "さんの現在の超過時間:" + str(exceed_time) )
        print("時間外労働時間が45時間を超えそうです。申請の準備をお願いします")

    elif exceed_time >= 45:
        print(user + "さんの現在の超過時間:" + str(exceed_time) )
        print("45時間を超えています!")

