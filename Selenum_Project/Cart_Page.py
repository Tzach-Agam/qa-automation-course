from selenium import webdriver
from selenium.webdriver.common.by import By

class Cart_Page:
    # This function will initialize the class and connect it with the driver
    def __init__(self, browser: webdriver.chrome):
        self.browser = browser

    # This function gets the text in the top left corner of the page which display "SHOPPING CART". This way we can confirm
    # we're in the shopping cart page
    def cart_location_title(self):
        shopping_cart_text = self.browser.find_element(By.CSS_SELECTOR,".select")
        return shopping_cart_text.text

    # If the cart is empty and has no products in it, this function will get a text which says that the cart is empty.
    def empty_cart_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, "label.roboto-bold[translate='Your_shopping_cart_is_empty']").text

    # This function gets an element of the entire table which displays all of the products in the cart page
    def cart_products_list(self):
        products_table = self.browser.find_element(By.CSS_SELECTOR, "[class='fixedTableEdgeCompatibility']")
        tr_list = products_table.find_elements(By.CSS_SELECTOR, "tr.ng-scope")
        return tr_list

    # This function gets all the elements in the first row of the table in the cart page including the Name, Quantity and Price
    # of the first product
    def first_products_elements(self):
        first_row = self.cart_products_list()[0]
        td_list = first_row.find_elements(By.TAG_NAME, "td")
        return td_list

    def first_product_quantity(self):
        return self.first_products_elements()[-2].text

    # This function gets all the elements in the second row of the table in the cart page including the Name, Quantity and Price
    # of the second product
    def second_products_elements(self):
        second_row = self.cart_products_list()[1]
        td_list = second_row.find_elements(By.TAG_NAME, "td")
        return td_list

    def second_product_quantity(self):
        return self.second_products_elements()[-2].text

    # This function gets all the elements in the third row of the table in the cart page including the Name, Quantity and Price
    # of the third product
    def third_products_elements(self):
        third_row = self.cart_products_list()[2]
        td_list = third_row.find_elements(By.TAG_NAME, "td")
        return td_list

    def third_product_quantity(self):
        return self.third_products_elements()[-2].text

    # This function gets the total price of the entire order/products displayed in the cart page and return it as text
    def cart_total_price(self):
        return self.browser.find_element(By.CSS_SELECTOR,"table.fixedTableEdgeCompatibility>tfoot>tr>td[colspan='2']>span.roboto-medium").text

    # This function gets the total price in the cart page as string and turns it's type to float
    def price_to_float(self):
        total_price = self.cart_total_price()
        total_price_new = ""
        for i in total_price:
            if i.isnumeric() or i == ".":
                total_price_new += i
        total_price_new = float(total_price_new)
        return total_price_new

    # This function will target the edit element of the first product
    def first_edit(self):
        """For this function to work, the cart window has to disappear. A usage of 'wait' libary can solve this problem"""
        return self.first_products_elements()[-1].find_element(By.LINK_TEXT, "EDIT")

    # This function clicks on the edit element of the first product
    def first_edit_click(self):
        self.first_edit().click()

    # This function will target the edit element of the second product
    def second_edit(self):
        return self.second_products_elements()[-1].find_element(By.LINK_TEXT, "EDIT")

    # This function clicks on the edit element of the second product
    def second_edit_click(self):
        self.second_edit().click()







