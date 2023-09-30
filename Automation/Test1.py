# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# service_chrome = Service(r"C:\Users\ME1\Desktop\Automation\chromedriver.exe")
# #service_firefox = Service(r"C:\Users\ME1\Desktop\Automation\geckodriver.exe")
#
# browser_c = webdriver.Chrome(service = service_chrome)
# #browser_f = webdriver.Firefox(service = service_firefox)
#
# browser_c.get("https://www.google.co.il/")
# browser_c.maximize_window()
# # In case an element s not found on the page, will try for 10 seconds before we get an error massage
# browser_c.implicitly_wait(10)
# gmail = browser_c.find_element(By.CSS_SELECTOR, "div.gb_e:nth-child(1) > a:nth-child(1)")
# if gmail.text == "Gmail":
#     print("passed")
# else:
#     print("failed")
#
# # Get the search line element object
# search_bar = browser_c.find_element(By.CSS_SELECTOR,".gLFyf")
# search_bar.send_keys("selenium")
# sleep(0.5)
# search_bar.clear()
# sleep(0.5)
# search_bar.send_keys("python")
# # Get the search bar element
# # search_button = browser_c.find_element(By.CSS_SELECTOR,".FPdoLc > center:nth-child(1) > input:nth-child(1)")
# # search_button.click()
# search_bar.send_keys(Keys.ENTER)

# def list_sum(lst):
#     total = lst[0]
#     count = 0
#     result = []
#     for i in range(1,len(lst)):
#         if total >= 0:
#             result.append(total)
#             count += 1
#         total += lst[i]
#     return result
#
# print(list_sum([2,0,5,100,20]))
# print(list_sum([1,4,1,13,9]))


def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print(Fizz)
        elif i % 5 == 0 and i % 3 != 0:
            print(Buzz)
        else:
            print(i)



