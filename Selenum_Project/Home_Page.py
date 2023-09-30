from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class Home_Page:
    # This function will initialize the class and connect it with the driver
    def __init__(self, browser:webdriver.chrome):
        self.browser = browser

    # This function gets a list of all the available categories elements, and will return a random category
    def random_category(self):
        self.category_list = \
        [self.browser.find_element(By.CSS_SELECTOR, "[aria-label='SpeakersCategory']"),
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='TabletsCategory']"),
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='HeadphonesCategory']"),
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='LaptopsCategory']"),
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='MiceCategory']")]
        return random.choice(self.category_list)

    # This function will click on a random category given to it
    def category_click(self):
        while True:
            try:
                self.random_category().click()
                break
            except:
                pass

    # This function will choose the speakers category and will click it
    def speakers_category(self):
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='SpeakersCategory']").click()

    # This function will choose the tablets category and will click it
    def tablets_category(self):
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='TabletsCategory']").click()

    # This function will choose the headphones category and will click it
    def headphones_category(self):
        self.browser.find_element(By.CSS_SELECTOR, "[aria-label='HeadphonesCategory']").click()

    # This function will get the the text of the title "OUR PRODUCTS" in the home page
    def our_products_title(self):
        return self.browser.find_element(By.LINK_TEXT, "OUR PRODUCTS").text


