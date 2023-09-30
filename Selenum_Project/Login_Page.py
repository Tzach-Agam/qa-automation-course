from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_Page:
    def __init__(self, browser: webdriver.chrome):
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

    # Targets the username element field in the login page
    def username(self):
        return self.browser.find_element(By.NAME, "username")

    # Inputs the username in the given parameter to the username field
    def username_input(self, username):
        """The username in the parameter has to be one that already exists in the site's system"""
        self.username().send_keys(username)

    # Targets the password element field in the login page
    def password(self):
        return self.browser.find_element(By.NAME, "password")

    # Inputs the password in the given parameter to the password field
    def password_input(self, password):
        """The password in the parameter has to be one that already exists in the site's system"""
        self.password().send_keys(password)

    # Targets the sign in button in the login page
    def sign_in_button(self):
        return self.browser.find_element(By.ID, "sign_in_btnundefined")

    # Clicks the sign in button in the login page
    def sign_in_click(self):
        while True:
            try:
                self.sign_in_button().click()
                break
            except:
                pass

    # Targets the sign out element in the user icon
    def log_out(self):
        return self.browser.find_element(By.CSS_SELECTOR,"label[translate='Sign_out'][ng-click='signOut($event)']")

    # Clicks the sign out element in the user icon
    def log_out_click(self):
        self.log_out().click()

    # This function will return the the text of the username that is located next to the user icon after the user logged in.
    # This we can know that the user logged in to the site
    def login_check_text(self):
        return self.browser.find_element(By.CSS_SELECTOR,"[class='hi-user containMiniTitle ng-binding']").text

    # This function will return the text of the SIGN IN button element in the log in page. If the user pressed on the
    # user icon and the SIGN IN button is there, then we can know that the user is logged out.
    def logout_check_text(self):
        return self.browser.find_element(By.ID, "sign_in_btnundefined").text
