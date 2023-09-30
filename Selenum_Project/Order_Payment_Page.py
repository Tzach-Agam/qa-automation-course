from selenium import webdriver
from selenium.webdriver.common.by import By

class Order_Payment_page:
    # This function will initialize the class and connect it with the driver
    def __init__(self, browser:webdriver.chrome):
        self.browser = browser

    # In the order payment page, this function will target the register element and will click it for unregistered users
    def order_payment_register(self):
        self.browser.find_element(By.ID, "registration_btnundefined").click()

    # Click on the "NEXT"button in the page and moves to the payment method oprions
    def next_payment_method(self):
        self.browser.find_element(By.ID, "next_btn").click()

    # Clicks on the safepay option as payment method
    def safepay_choose(self):
        self.browser.find_element(By.NAME, "safepay").click()

    # Inputs a username for the safepay payment method option
    def safepay_username(self, username):
        """The username in the parameter can be the username the user used to login with"""
        self.browser.find_element(By.NAME, "safepay_username").send_keys(username)

    # Inputs a password for the safepay payment method option
    def safepay_passward(self, password):
        """The password in the parameter can be the password the user used to login with"""
        self.browser.find_element(By.NAME, "safepay_password").send_keys(password)

    # Clicks on pay now while the user pays with the safepay option
    def pay_now_safepay(self):
        """There is a difference in the elements of "Pay Now" between pay now with safepay and pay now with credit card"""
        return self.browser.find_element(By.ID, "pay_now_btn_SAFEPAY").click()

    # Inputs the username in the parameter in the username field for registered user
    def login_username(self, username):
        """The username in the parameter has to contain minimum 5 letters and maximum 15 letters for the user to register"""
        self.browser.find_element(By.NAME, "usernameInOrderPayment").send_keys(username)

    # Inputs the password in the parameter in the username field for registered user
    def login_passward(self, passward):
        """The passward in the parameter as to contain at least 1 uppercase and lowercase letter, and numbers.minimum
        8 characters"""
        self.browser.find_element(By.NAME, "passwordInOrderPayment").send_keys(passward)

    # Clicks the login button in the page and moves the registered user to the next option
    def order_payment_login(self):
        self.browser.find_element(By.ID, "login_btnundefined").click()

    # Clicks and chooses the credit card option as payment method
    def credit_card_choose(self):
        self.browser.find_element(By.NAME, "masterCredit").click()

    # Inputs the card number in the parameter to the card number field
    def credit_card_number(self, number):
        """The number in the parameter has to contain exactly 16 numbers"""
        self.browser.find_element(By.ID, "creditCard").send_keys(number)

    # Inputs the cvv number in the parameter to the card cvv field
    def credit_card_cvv(self, cvv_number):
        """The number in the parameter has to contain exactly 3 characters"""
        self.browser.find_element(By.NAME, "cvv_number").send_keys(cvv_number)

    # Inputs the card's holder name that in the parameter to the cardholder field
    def credit_card_cardholder(self, name):
        """The name in the parameter has to contain first and last name"""
        self.browser.find_element(By.NAME, "cardholder_name").send_keys(name)

    # Clicks on the pay now option if the user pays with credit card
    def pay_now_credit(self):
        """There is a difference in the elements of "Pay Now" between pay now with safepay and pay now with credit card"""
        self.browser.find_element(By.ID, "pay_now_btn_ManualPayment").click()

    # Gets a text of a successful order in the page the user is directed to after clicking on pay now option.
    def successful_payment_check(self):
        return self.browser.find_element(By.CSS_SELECTOR, "[translate='Thank_you_for_buying_with_Advantage']").text




