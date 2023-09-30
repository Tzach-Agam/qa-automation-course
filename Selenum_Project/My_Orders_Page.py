from selenium import webdriver
from selenium.webdriver.common.by import By

class My_Orders_Page:
    # This function will initialize the class and connect it with the driver
    def __init__(self, browser: webdriver.chrome):
        self.browser = browser

    # This function will get the name of the order in my orders page
    def order_name(self):
        return self.browser.find_element(By.XPATH, "//tr/td/span[@class='ng-binding']")

    # This function will get the number of the order according to the row in the parameter
    def order_number(self, row):
        """The row parameter number determines the row in the table of orders in my orders page. 0 is for
        first tow. 1 is for second row and so on."""
        order = self.browser.find_elements(By.XPATH, "//tr/td[1]/label")
        return order[row].text

    # This function will remove an order from my orders page
    def remove_order(self, order):
        """The order parameter determines the order the user wants to delete. 0 is for first order, 1 for second ans
         so on"""
        removes = self.browser.find_elements(By.CSS_SELECTOR, "[translate='REMOVE']")
        return removes[order]

    # This function will click on the remove button in the page and will delete the order
    def remove_order_click(self, order):
        self.remove_order(order).click()
