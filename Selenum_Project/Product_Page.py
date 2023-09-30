from selenium import webdriver
from selenium.webdriver.common.by import By
from Home_Page import Home_Page
from Category_Page import Category_Page

class Product_Page:
    # This category will initialize the class and connect it with the driver
    def __init__(self, browser: webdriver.chrome):
        self.browser = browser
        self.home_page = Home_Page(self.browser)
        self.category_page = Category_Page(self.browser)

    # The function gets the name of the product in the product page
    def product_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div[id='Description']>h1").text

    # The function gets the price of the product in the product page
    def product_price(self):
        return self.browser.find_element(By.CSS_SELECTOR,"div[id='Description']>h2").text

    # The function gets the quantity of the product in the product page
    def product_quantity(self):
         return self.browser.find_element(By.NAME, "quantity").get_attribute("value")

    # This function targets the add product element in the product page. If the product is sold out, then it will
    # choose another random product until the chosen product will be available
    def add_product(self):
        while self.browser.find_element(By.CSS_SELECTOR, "[translate='SOUL_OUT']").text == "SOLD OUT":
            self.return_home_click()
            self.home_page.category_click()
            self.category_page.random_product_click()
        else:
            return self.browser.find_element(By.CSS_SELECTOR, "[translate='ADD_TO_CART']")

    # This function will click on the add product element and will add the product to the cart
    def add_product_click(self):
        self.add_product().click()

    # This function will add a product with the plus sign in the product page
    def plus_product(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".plus").click()

    # This function will remove a product with the minus sign in the product page
    def minus_product(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".minus").click()

    # This function gets the price of the product and turns it's type from string to float
    def price_to_float(self):
        product_price = self.product_price()
        product_price_new = ""
        for i in product_price:
            if i.isnumeric() or i == ".":
                product_price_new += i
        product_price_new = float(product_price_new)
        return product_price_new

    # This function will target the return home element in the product page
    def return_home(self):
        return self.browser.find_element(By.CSS_SELECTOR, "[translate='HOME']")

    # This function will click on the home page element and will return the user back to the home page
    def return_home_click(self):
        self.return_home().click()

    # This function will target the return to the category page from products page
    def return_category(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div>nav>a.ng-binding")

    # This function will click on the category page element and will return the user back to the category page
    def return_category_click(self):
        self.return_category().click()








