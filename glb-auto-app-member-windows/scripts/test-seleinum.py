from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = webdriver.Remote(
    command_executor="http://selenium:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME.copy(),
)

driver.get("https://maasaablog.com/")
print(driver.title)
driver.quit()