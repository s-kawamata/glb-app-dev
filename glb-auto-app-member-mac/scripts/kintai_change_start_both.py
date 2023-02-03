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


TOKEN = user_info.slack_token
CHANNEL = 'akatsuka_test'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
  'channel': CHANNEL,
  'text': 'リモワ開始します\n本日は'  + user_info.destination_station +'出社です'
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
  elm = driver.find_element_by_xpath('//*[@id="phSearchContainer"]/div/div[1]')
  if elm :
    pass 
  else :
    raise ValueError("ログインに失敗しました")
except NoSuchElementException as e:
  print(e)

print("ログイン完了しました")
time.sleep(7)

#htmlを表示
#print(driver.page_source)

#iframeを切り替える
iframe=driver.find_element_by_xpath("//*[@id='0665F00000117vk']")
driver.switch_to.frame(iframe)
driver.implicitly_wait(15)

#htmlを表示2
#print("ここからiframe切り替えてます。" + driver.page_source)

#在宅勤務4h未満ボタンを選択
y_loca = driver.find_element_by_xpath("//*[@id='workLocationButtons']/label[3]/div")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)


#出勤ボタンをクリック
y_loca = driver.find_element_by_xpath("//*[@id='btnStInput']")
driver.execute_script("window.scrollTo(0, " + str(y_loca.location['y']) + ");")
y_loca.click()
time.sleep(2)

driver.switch_to.default_content()


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

#完了処理
print("処理が正常に完了しました。")
driver.quit()
