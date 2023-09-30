from selenium import webdriver
from selenium.webdriver.common.by import By

class General_Functions:
    # This category will initialize the class and connect it with the driver
    def __init__(self, browser:webdriver.chrome):
        self.browser = browser

    # Targets to user icon on top of the page
    def user_icon(self):
        return self.browser.find_element(By.ID, "menuUser")

    # Clicks on the user icon on top of the page
    def user_icon_click(self):
        while True:
            try:
                self.user_icon().click()
                break
            except:
                pass

    # Targets the my orders option in the user icon. By clicking on it the user will be directed to my orders page
    def user_my_orders(self):
        return self.browser.find_element(By.CSS_SELECTOR, "label[translate='My_Orders'][class='option ng-scope'][role='link']")

    # Clicks on the my orders option in the user icon button and directs the user to it's orders page
    def user_my_orders_click(self):
        while True:
            try:
                self.user_my_orders().click()
                break
            except:
                pass

    # Targets the sign out element in the user icon
    def log_out(self):
        return self.browser.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][ng-click='signOut($event)']")

    # Clicks the sign out element in the user icon
    def log_out_click(self):
        self.log_out().click()

    # This function will target the return home element in the category page
    def return_home(self):
        return self.browser.find_element(By.CSS_SELECTOR, "[translate='HOME']")

    # This function will click on the home page element and will return the user back to the home page
    def return_home_click(self):
        self.return_home().click()

    # This function will get the total number of products in the cart through the cart window on top
    # of the page
    def total_items_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, "label.roboto-regular").text
    
    # This function will get a list of all the names in the cart window on top of the page.
    def product_name_list(self):
        """In order to get a specific name, the user has to combine an index. 0 is for first product name, 1 is for
        second and so on"""
        return self.browser.find_elements(By.CSS_SELECTOR, "a>h3")

    # This function will get a list of all the elements with the color in the parameter in the cart window on top of the page
    def product_color_check(self, color):
        """The functions will get all the elements with the given color. To get the specific color of the product,
        the user has to combine it with an index, according to the product's order in the cart window. The parameter has
        to be exactly like in the cart window"""
        return self.browser.find_elements(By.XPATH, "//*[contains(text(), '" + color + "')]")

    # This function will get a list of all the product's quantities in the cart window page
    def product_quantity_check(self, quantity):
        """The parameter will get all the elements with the given quantity. In order to get the specific order, the
        user has to combine an index of the product according to it's order in the cart window The parameter has
        to be exactly like in the cart window"""
        return self.browser.find_element(By.XPATH, "//*[contains(text(), '" + quantity + "')]").text

    # This function will get a list of all the product's prices in the cart window page
    def product_price_check(self, price):
        """The function will get all the elements with the given price. In order to get the specific order, the
        user has to combine an index of the product according to it's order in the cart window. The parameter has
        to be exactly like in the cart window"""
        return self.browser.find_elements(By.XPATH, "//*[contains(text(), '" + price + "')]")
    
    # This function will target the "X" button of the first product element in the cart window
    def remove_product(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.removeProduct")

    # This function will click on the "X" button of the first product in order in the cart window and will remove
    # it from the cart
    def remove_product_click(self):
        self.remove_product().click()

    # This function will target the cart icon on top of the site
    def move_to_cart(self):
        return self.browser.find_element(By.ID, "menuCart")

    # This function will click on the cart icon on top of the page, and will direct the user to the cart page
    def move_to_cart_click(self):
        self.move_to_cart().click()

    # This function will target the checkout button in the cart window
    def checkout(self):
        return self.browser.find_element(By.ID, "checkOutPopUp")

    # This function will click the checkout button in the cart window will will direct the user to the order payment page
    def checkout_click(self):
        self.checkout().click()






