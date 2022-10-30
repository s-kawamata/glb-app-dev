from selenium import webdriver
#import chromedriver_binary
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import list
import sys
from selenium.webdriver import DesiredCapabilities
#sys.path.append("/Users/akatsukatakukai/Documents/working/kinmu_Bot")

#起動させた一ヶ月前の年月を取得

now = datetime.now()
last_month = now - relativedelta(months=1)
last_month_str = last_month.strftime('%Y年%m月')


CHROMEDRIVER = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# ドライバー指定でChromeブラウザを開く
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Remote(
#     command_executor="http://selenium:4444/wd/hub",
#     desired_capabilities=DesiredCapabilities.CHROME.copy(),
# )

# Googleアクセス
driver.get('https://login.salesforce.com/?locale=jp')

time.sleep(2)

driver.find_element_by_xpath('//*[@id="username"]').send_keys("s_kawamata@ap-com.co.jp")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("19921107Wanko")

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



    #前月のボタンをクリック
    select = Select(driver.find_element_by_xpath("//*[@class='ts-month-select']"))
    select.select_by_visible_text(f'{last_month_str}')

    time.sleep(5)


    #メンバ名を検索、クリック
    driver.find_element_by_link_text(i).click()


    #元のウインドウに戻る
    driver.switch_to.window(newhandles [0])

    time.sleep(3)



    #承認ステータスを確認し、未確定であればフラグを立てる
    
    status = driver.find_element_by_xpath('//*[@id="monthlyStatus"]').get_attribute("textContent")

    if status == '未確定':
        print(i + 'さんはまだ' + last_month_str + 'の勤怠を提出していません')
    else :
        print(i + 'さんはすでに' + last_month_str + 'の勤怠を提出しています')


    

#完了処理
driver.quit()




