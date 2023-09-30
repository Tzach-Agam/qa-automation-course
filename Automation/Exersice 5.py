from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service_chrome = Service(r"C:\Users\ME1\Desktop\Automation\chromedriver.exe")
browser_c = webdriver.Chrome(service = service_chrome)
browser_c.get("https://juliemr.github.io/protractor-demo/")
browser_c.maximize_window()
browser_c.implicitly_wait(10)
num1_input = browser_c.find_element(By.CSS_SELECTOR,".input-small[ng-model=first]")
num1_input.send_keys("6")
num2_input = browser_c.find_element(By.CSS_SELECTOR,".input-small[ng-model=second]")
num2_input.send_keys("6")
browser_c.find_element(By.ID,"gobutton").click()
result = browser_c.find_element(By.CSS_SELECTOR,"h2.ng-binding")
sleep(5)
if result.text == "12":
    print("success")
else:
    print("fail",result.text)