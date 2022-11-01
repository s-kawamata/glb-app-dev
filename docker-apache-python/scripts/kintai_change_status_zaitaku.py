from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select

# ドライバー指定でChromeブラウザを開く
driver = webdriver.Chrome(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome') 
#driver = webdriver.Firefox()
 
# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')

#driver.maximize_window()
driver.set_window_size(1200,3000)

driver.find_element_by_xpath('//*[@id="username"]').send_keys("k_fujihira@ap-com.co.jp")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("613457Frontier")

#ログインボタンをクリック
driver.find_element_by_xpath('//*[@id="Login"]').click()

#勤務表のタブをクリック
driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()
time.sleep(5)
#driver.find_element_by_xpath('//*[@id="nextMonthButton"]').click()
#time.sleep(5)
#driver.find_element_by_xpath('//*[@id="nextMonthButton"]').click()
#time.sleep(5)

#繰り返し処理を開始
i=0

content = driver.find_elements_by_css_selector('.tele')
days = len(content)
print(days)

while i < days:
    print("処理スタート")
    print(i)
    elements = driver.find_elements_by_css_selector('.tele')[i]
    loc = elements.location
    x, y = loc['x'], loc['y']
    actions = ActionChains(driver)
    actions.move_by_offset(x,y)
    actions.click()
    actions.perform()

    #処理を待つ
    time.sleep(4)

    print("日時が選択されました") 

    #勤務場所のタブを選択する
    element = driver.find_element_by_xpath('//*[@id="workLocationId"]')
    driver.implicitly_wait(5)

    #タブを選択する為の処理
    select = Select(element)
    driver.implicitly_wait(5)

    #value属性から「在宅勤務」を選択する 
    select.select_by_value('a2B5F00000OkMUPUA3')  #←文字の方がいい
    #select.select_by_value('')  #←空白
    driver.implicitly_wait(5)

    #登録ボタンクリック
    driver.find_element_by_xpath('//*[@id="dlgInpTimeOk"]').click()
    driver.implicitly_wait(5)
    i+=1
    print("登録ボタンが押されました")

    #アクションをリセット
    actions.reset_actions()
    #処理待ち
    time.sleep(6)
else:
# 処理対象が存在しない時の処理
    driver.quit()
