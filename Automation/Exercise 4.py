from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_chrome = Service(r"C:\Users\ME1\Desktop\Automation\chromedriver.exe")
browser_c = webdriver.Chrome(service = service_chrome)
browser_c.get("https://demo.guru99.com/test/newtours/")
browser_c.maximize_window()
browser_c.implicitly_wait(10)
username = browser_c.find_element(By.NAME,"userName")
username.send_keys("tutorial")
password = browser_c.find_element(By.NAME,"password")
password.send_keys("tutorial")
submit = browser_c.find_element(By.NAME,"submit")
submit.click()
browser_c.find_element(By.LINK_TEXT,"Flights").click()
browser_c.find_element(By.CSS_SELECTOR,"[name='tripType'][value='oneway']").click()
browser_c.find_element(By.CSS_SELECTOR,"[name='servClass'][value='First']").click()
browser_c.find_element(By.NAME,"findFlights").click()






