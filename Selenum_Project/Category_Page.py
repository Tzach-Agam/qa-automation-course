from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class Category_Page:
    # This category will initialize the class and connect it with the driver
    def __init__(self, browser: webdriver.chrome):
        self.browser = browser

    # This function will target the header of the category page
    def category_title(self):
        return self.browser.find_element(By.CSS_SELECTOR, "h3.categoryTitle")

    # This function will return the text of the heading of the category page
    def category_title_text(self):
        return self.category_title().text

    # This function will get a random product in the category page using the header text to compare and will
    # return the random product
    def random_product(self):
        if self.category_title().text == "SPEAKERS":
            id_number = ["19", "20", "21", "22", "23", "24", "25"]
            return self.browser.find_element(By.ID, random.choice(id_number))
        elif self.category_title().text == "TABLETS":
            id_number = ["16", "17", "18"]
            return self.browser.find_element(By.ID, random.choice(id_number))
        elif self.category_title().text == "HEADPHONES":
            id_number = ["12", "14", "15"]
            return self.browser.find_element(By.ID, random.choice(id_number))
        elif self.category_title().text == "LAPTOPS":
            id_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
            return self.browser.find_element(By.ID, random.choice(id_number))
        elif self.category_title().text == "MICE":
            id_number = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34"]
            return self.browser.find_element(By.ID, random.choice(id_number))

    # This function will click on the random product and will enter its page
    def random_product_click(self):
        self.random_product().click()

    # This function will choose a specific speaker from the speakers category page
    def speaker_product(self):
        """Gets the first speaker in the category"""
        self.browser.find_element(By.ID, "20").click()

    # This function will choose a specific tablet from the tablets category page
    def tablets_product(self):
        """Gets the first tablet in the category"""
        self.browser.find_element(By.ID, "16").click()

    # This function will choose a specific headphones from the speakers headphones page
    def headphones_product(self):
        """Gets the first headphones in the category"""
        self.browser.find_element(By.ID, "15").click()

    # This function will target the return home element in the category page
    def return_home(self):
        return self.browser.find_element(By.CSS_SELECTOR, "[translate='HOME']")

    # This function will click on the home page element and will return the user back to the home page
    def return_home_click(self):
        self.return_home().click()
