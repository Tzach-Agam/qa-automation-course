from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login_Page import Login_Page
from Home_Page import Home_Page
from Category_Page import Category_Page
from Product_Page import Product_Page
from Cart_Page import Cart_Page
from Order_Payment_Page import Order_Payment_page
from My_Orders_Page import My_Orders_Page
from Create_Account_Page import Create_Account_Page
from General_Functions import General_Functions
from time import sleep

class Test_Selenium_Project(TestCase):
    # The setup will stat with every test execution, determine the website address and initialize the objects of the classes
    # for the execution of the tests. The are for each page in the site
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(100)
        self.wait = WebDriverWait(self.driver, 10)
        self.login = Login_Page(self.driver)
        self.home_page = Home_Page(self.driver)
        self.category_page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.cart_page = Cart_Page(self.driver)
        self.order_payment = Order_Payment_page(self.driver)
        self.my_orders = My_Orders_Page(self.driver)
        self.create_account = Create_Account_Page(self.driver)
        self.general_functions = General_Functions(self.driver)

    # This test will choose 3 products from different categories and will check if the total number of products in
    # the cart window is correct
    def test_one(self):
        # Adding 2 products from one category to cart
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        self.product_page.add_product_click()
        # Add 1 product from different category to cart
        self.product_page.return_home_click()
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        # Check if the total number of items is correct in the cart window
        self.assertEqual(self.general_functions.total_items_text(), "(3 Items)")

    # This test will add 3 different products in different quantities and will check if  the name, color, quantity and
    # price of each product is correct
    def test_two(self):
        # Adding 3 products from one category
        self.home_page.headphones_category()
        self.category_page.headphones_product()
        for i in range(3):
            self.product_page.add_product_click()
        # Adding 2 products from different category
        self.product_page.return_home_click()
        self.home_page.tablets_category()
        self.category_page.tablets_product()
        for i in range(2):
            self.product_page.add_product_click()
        # Adding 1 products from different category
        self.product_page.return_home_click()
        self.home_page.speakers_category()
        self.category_page.speaker_product()
        self.product_page.add_product_click()
        # 3 tests to check if the names of the products in the cart window are correct. Each test checks that the text of the
        # given element is the correct name of the product according to it's order in the cart window
        self.assertEqual(self.general_functions.product_name_list()[0].text, "BOSE SOUNDLINK BLUETOOTH SP...")
        self.assertEqual(self.general_functions.product_name_list()[1].text, "HP ELITEPAD 1000 G2 TABLET")
        self.assertEqual(self.general_functions.product_name_list()[2].text, "BEATS STUDIO 2 OVER-EAR MAT...")
        # 3 tests to check if the colors of the products in the cart window are correct. Each test checks that the text of the
        # given element is the correct color of the product according to it's order in the cart window
        self.assertEqual(self.general_functions.product_color_check("BLACK")[0].text,"BLACK")
        self.assertEqual(self.general_functions.product_color_check("BLUE")[1].text, "BLUE")
        self.assertEqual(self.general_functions.product_color_check("BLACK")[1].text, "BLACK")
        # 3 tests to check if the quantities of the products in the cart window are correct. Each test checks that the text of the
        # given element is the correct quantity of the product according to it's order in the cart window.
        self.assertEqual(self.general_functions.product_quantity_check("QTY: 1"), "QTY: 1")
        self.assertEqual(self.general_functions.product_quantity_check("QTY: 2"), "QTY: 2")
        self.assertEqual(self.general_functions.product_quantity_check("QTY: 3"), "QTY: 3")
        # 3 tests to check if the prices of the products in the cart window are correct. Each test checks that the text of the
        # given element is the correct price of the product according to it's order in the cart window
        self.assertEqual(self.general_functions.product_price_check("$269.99")[0].text, "$269.99")
        self.assertEqual(self.general_functions.product_price_check("$2,018.00")[0].text, "$2,018.00")
        self.assertEqual(self.general_functions.product_price_check("$539.97")[0].text, "$539.97")

    # This test will add two different products and then will remove one of them. Then the test will check if the number of
    # items displayed in the cart window is correct.
    def test_three(self):
        # Add 1 item of one product
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        self.product_page.return_home_click()
        # Add 1 item from second product
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        # Removes the item from the cart
        self.general_functions.remove_product_click()
        # Checks if the number of items displayd the cart window is correct
        self.assertEqual(self.general_functions.total_items_text(), "(1 Item)")

    # This test will add one product, will move to the cart page and will check if the user's location is indeed the cart
    # page by the location text in the top left corner of the page
    def test_four(self):
        # Add 1 product
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        # Moves to cart page
        self.general_functions.move_to_cart_click()
        # Wait until the "SHOPPING CART" text is displayd in the top left corner of the page
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".select"), "SHOPPING CART"))
        # Prints the text of the location and checks if the user is in the cart page. The "SHOPPING CART" text will be
        # shown only if the user will be in the cart page.
        print(self.cart_page.cart_location_title())
        self.assertEqual(self.cart_page.cart_location_title(), "SHOPPING CART")

    # This test will add 3 different products in different quantities to the cart, will keep their name, price and chosen
    # quantities, will add the multiplication of each product price with it's quantity, and will check if the total
    # quantity displayd in the cart page is correct.
    def test_five(self):
        # Add 3 items of first product and keep it's name, price and quantity
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.plus_product()
        self.product_page.plus_product()
        self.product_page.add_product_click()
        p_name1 = self.product_page.product_name()
        p_price1 = self.product_page.price_to_float()
        p_quantity1 = int(self.product_page.product_quantity())
        # Add 2 items of second product and keep it's name, price and quantity
        self.product_page.return_home_click()
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.plus_product()
        self.product_page.add_product_click()
        p_name2 = self.product_page.product_name()
        p_price2 = self.product_page.price_to_float()
        p_quantity2 = int(self.product_page.product_quantity())
        # Add 1 items of third product and keep it's name, price and quantity
        self.product_page.return_home_click()
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        p_name3 = self.product_page.product_name()
        p_price3 = self.product_page.price_to_float()
        p_quantity3 = int(self.product_page.product_quantity())
        # Move to cart page
        self.general_functions.move_to_cart_click()
        # Multiply the price of each product with it's quantity, add it all and keep it in a variable
        total_price = p_price1 * p_quantity1 + p_price2 * p_quantity2 + p_price3 * p_quantity3
        cart_total_price = self.cart_page.price_to_float()
        # Check if the price of the product in cart page is correct
        self.assertEqual(total_price, cart_total_price)
        # Display of all the products information (name, price and quantity)
        print(f"First product information: Name: {p_name1}, Quantity: {p_quantity1}, Price: {p_price1}")
        print(f"Second product information: Name: {p_name2}, Quantity: {p_quantity2}, Price: {p_price2}")
        print(f"Third product information: Name: {p_name3}, Quantity: {p_quantity3}, Price: {p_price3}")

    # This test will add two products, increase their quantity by 1 and will check if the new
    # quantity is being displayed in the cart page
    def test_six(self):
        # Add 1 item of first product
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        # Add 1 item of second product
        self.product_page.return_home_click()
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        # Move to cart page
        self.general_functions.move_to_cart_click()
        # The cart window is blocking the first edit button of the first product. wait for it to disappear and click on the
        # edit button of the first product.
        self.wait.until(EC.invisibility_of_element_located((By.ID, "checkOutPopUp")))
        self.cart_page.first_edit_click()
        # Add another product to the cart
        self.product_page.plus_product()
        self.product_page.add_product_click()
        # Click on the second edit button and add another product to the cart
        self.cart_page.second_edit_click()
        self.product_page.plus_product()
        self.product_page.add_product_click()
        # Check if the quantity of each of the product changed and that it's now 2
        self.assertEqual(self.cart_page.first_product_quantity(), "2")
        self.assertEqual(self.cart_page.second_product_quantity(), "2")
        # The test failed continuously, it appears the is a bug in the site that doesn't allow the user to add more
        # than 1 product of an item.

    # This test will choose a product from tablets category, will go back to tablet category, check the location, will go
    # back to home page, and will check the location too
    def test_seven(self):
        # Add 1 tablet to cart
        self.home_page.tablets_category()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        self.product_page.return_category_click()
        # Check if we returned back to the category page
        self.assertEqual(self.category_page.category_title_text(), "TABLETS")
        self.category_page.return_home_click()
        # # Check if we returned to home page
        self.assertEqual(self.home_page.our_products_title(), "OUR PRODUCTS")

    # This test will add products of some kind to cart, will create a user to pay for them, pay with safepay as payment
    # method, will check if the order was made successfully, will check if the cart is empty and will go to my orders page to
    # see if the order is there
    def test_eight(self):
        # Add 2 items of a product to cart
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        self.product_page.add_product_click()
        # Go to checkout through cart window
        self.general_functions.checkout_click()
        # Create a new user
        self.order_payment.order_payment_register()
        self.create_account.create_account_username("bcd123")
        self.create_account.create_account_email("bcd123@abc.com")
        self.create_account.create_account_passward("Bcd12345")
        self.create_account.create_account_agree()
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))
        self.create_account.create_account_register()
        # Choose safepay as payment method and press on pay
        self.order_payment.next_payment_method()
        self.order_payment.safepay_username("bcd123")
        self.order_payment.safepay_passward("Bcd12345")
        self.order_payment.pay_now_safepay()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']"), "Thank you for buying with Advantage"))
        # Test if the order was made successfully
        self.assertEqual(self.order_payment.successful_payment_check(), "Thank you for buying with Advantage")
        self.general_functions.move_to_cart_click()
        # Test if the cart is empty now
        self.assertEqual(self.cart_page.empty_cart_text(), "Your shopping cart is empty")
        self.general_functions.user_icon_click()
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))
        self.general_functions.user_my_orders_click()
        self.wait.until(EC.element_to_be_clickable((self.my_orders.remove_order(0))))
        # Test if the order is in my orders page
        print(len(self.my_orders.order_number(0)))
        self.assertEqual(len(self.my_orders.order_number(0)), 10)

    # This test will add products of some kind to cart, will enter the site with an existing user and pay with credit card
    # will check if the order was made successfully, will check if the cart is empty and will go to my orders page to
    # see if the order is there
    def test_nine(self):
        # Add 2 items of a product to cart
        self.home_page.category_click()
        self.category_page.random_product_click()
        self.product_page.add_product_click()
        self.product_page.add_product_click()
        # Go to checkout through cart window
        self.general_functions.checkout_click()
        # Login to site with existing user
        self.order_payment.login_username("bcd123")
        self.order_payment.login_passward("Bcd12345")
        self.order_payment.order_payment_login()
        # Choose credit card as payment method, enter credit card information and pay
        self.order_payment.next_payment_method()
        self.order_payment.credit_card_choose()
        self.order_payment.credit_card_number("123456789012")
        self.order_payment.credit_card_cvv("1234")
        self.order_payment.credit_card_cardholder("Tzach Agam")
        self.order_payment.pay_now_credit()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']"), "Thank you for buying with Advantage"))
        # Test if the order was made successfully
        self.assertEqual(self.order_payment.successful_payment_check(), "Thank you for buying with Advantage")
        self.general_functions.move_to_cart_click()
        # Test if the cart is empty now
        self.assertEqual(self.cart_page.empty_cart_text(), "Your shopping cart is empty")
        self.general_functions.user_icon_click()
        self.wait.until(EC.invisibility_of_element((By.XPATH, "//div[@class='loader']")))
        self.general_functions.user_my_orders_click()
        self.wait.until(EC.element_to_be_clickable((self.my_orders.remove_order(0))))
        # Test if the order is in my orders page
        print(len(self.my_orders.order_number(0)))
        self.assertEqual(len(self.my_orders.order_number(0)), 10)

    # This test will check the login logout processes in the site. Will check if an existing user can login and logout
    # successfully
    def test_ten(self):
        # Entering username and password and logging in to the site
        self.login.user_icon_click()
        self.login.username()
        self.login.username_input("bcd123")
        self.login.password()
        self.login.password_input("Bcd12345")
        self.login.sign_in_click()
        # Check if the user is in the site
        self.assertEqual(self.login.login_check_text(), "bcd123")
        self.login.user_icon_click()
        self.login.log_out_click()
        # check if the user signed out
        self.login.user_icon_click()
        self.wait.until(EC.text_to_be_present_in_element((By.ID, "sign_in_btnundefined"), "SIGN IN"))
        print(self.login.logout_check_text())
        self.assertEqual(self.login.logout_check_text(), "SIGN IN")

    # A general execution to use the site
    def test_Login(self):
        self.login.user_icon_click()
        self.login.username()
        self.login.username_input("bcd123")
        self.login.password()
        self.login.password_input("Bcd12345")
        self.login.sign_in_click()
        sleep(1000)













































