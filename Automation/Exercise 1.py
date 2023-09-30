from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_chrome = Service(r"C:\Users\ME1\Desktop\Automation\chromedriver.exe")
browser_c = webdriver.Chrome(service = service_chrome)
browser_c.get("https://phptravels.net/api/admin")
browser_c.maximize_window()
email_bar = browser_c.find_element(By.CSS_SELECTOR,"[name = 'email'][type = 'text']")
email_bar.send_keys("admin@phptravels.com")
passward_bar = browser_c.find_element(By.CSS_SELECTOR,"[type = 'password'][name = 'password']")
passward_bar.send_keys("demoadmin")
login_bar = browser_c.find_element(By.CSS_SELECTOR, "[class='btn btn-primary btn-block ladda-button fadeIn animated mdc-ripple-upgraded']")
login_bar.click()
dashboard_bar = browser_c.find_element(By.CSS_SELECTOR, "div[class='text-uppercase font-monospace']")
if dashboard_bar.text == "DASHBOARD":
    print("success")
else:
    print("fail")
personal_icon = browser_c.find_element(By.ID, "dropdownMenuProfile")
personal_icon.click()
log_out = browser_c.find_element(By.CSS_SELECTOR, "a[class = 'dropdown-item loadeffect mdc-ripple-upgraded'][href='https://phptravels.net/api/admin/logout']")
lst_logout = browser_c.find_elements(By.CSS_SELECTOR, "[class ='me-3']")
lst_logout[3].click()
#log_out.click()
browser_c.close()