from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
import user_info
import user_list
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException


# ドライバー指定でChromeブラウザを開く
# CHROMEDRIVER = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Remote(
     command_executor="http://selenium:4444/wd/hub",
     desired_capabilities=DesiredCapabilities.CHROME.copy(),
 )

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
  elm = driver.find_elements_by_xpath('//*[@id="phSearchContainer"]/div/div[1]')
  if elm :
    pass 
  else :
    raise ValueError("ログインに失敗しました")
except NoSuchElementException as e:
  print(e)

print("ログイン完了しました")
time.sleep(7)

#勤務表のタブをクリック
driver.find_element_by_xpath('//*[@id="01r5F000000g5DS_Tab"]/a').click()

for user in user_list.nameList:
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

    #お知らせウィンドウが開いていた場合は閉じる
    notification_window = driver.find_elements_by_xpath("//div[@data-dojo-attach-point='titleBar']/*[contains(text(), 'お知らせ')]")

    if notification_window:
        y_loca = driver.find_element_by_xpath("//tr[@id='dialogInfoBottom']//button[@class='std-button2 close_button']")
        driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
        y_loca.click()
    else:
        pass

    #時間外超過時間を摘出
    value = driver.find_element_by_xpath("//*[contains(text(), '当月度の超過時間＋法定休日労働時間')]/../../td[2]").text
    time.sleep(2)
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

#完了処理
print("処理が正常に完了しました。")
driver.quit()
