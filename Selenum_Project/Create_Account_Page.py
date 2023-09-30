from selenium import webdriver
from selenium.webdriver.common.by import By

class Create_Account_Page:
    # This function will initialize the class and connect it with the driver
    def __init__(self, browser:webdriver.chrome):
        self.browser = browser

    # Inputs the username in the parameter to the username field in the page
    def create_account_username(self, username):
        """The username in the parameter has to contain minimum 5 letters and maximum 15 letters for the user to register"""
        self.browser.find_element(By.NAME, "usernameRegisterPage").send_keys(username)

    # Inputs the email address in the parameter to the email field in the page
    def create_account_email(self, email):
        """The email in the parameter has to contain at least one letter before and after the @ sign, a @ sign and the letter com"""
        self.browser.find_element(By.NAME, "emailRegisterPage").send_keys(email)

    # Inputs both the passward and the passward confirmation to their fields in the page
    def create_account_passward(self, passward):
        """The passward in the parameter as to contain at least 1 uppercase and lowercase letter, and numbers.
        minimum 8 characters"""
        self.browser.find_element(By.NAME, "passwordRegisterPage").send_keys(passward)
        self.browser.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(passward)

    # Clicks on the agree to condition option in the page
    def create_account_agree(self):
        """THis function is mandatory if the user wishes to register"""
        while True:
            try:
                self.browser.find_element(By.NAME, "i_agree").click()
                break
            except:
                pass

    # Clicks on the register button in the page
    def create_account_register(self):
        while True:
            try:
                self.browser.find_element(By.ID, "register_btnundefined").click()
                break
            except:
                pass
