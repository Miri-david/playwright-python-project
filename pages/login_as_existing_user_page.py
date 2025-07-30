from pytest_playwright.pytest_playwright import page
from pages.Base_page import BasePage
from playwright.sync_api import Page


class LoginExistingUserPage(BasePage):

    __USER_BTN = ".header-1g16tvz:nth-child(1)"
    __EMAIL_ADDRESS="#username"
    __USER_PASSWORD="#password"
    __SIGN_IN=".c8fc15737"
    __SHOW_PASSWORD="#showPasswordButton"
    __FORGETTING_PASSWORD=".c99384160"
    __RESET_PASSWORD=".c02192423"
    __REMEMBER_EMAIL="#rememberEmail"


    #test 15
    def login_to_user(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ADDRESS,"miri4@gmail.com")
        self.fill(self.__USER_PASSWORD,"Miri123")
        self.click(self.__SIGN_IN)


    #test 16
    def error_alert_incorrect_password(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ADDRESS,"miri4@gmail.com")
        self.fill(self.__USER_PASSWORD,"123456789")
        self.click(self.__SIGN_IN)
        print(self.page.locator(".msgContent").inner_text())

    #test 17
    def error_alert_incorrect_email(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ADDRESS,"miri44@gmail.com")
        self.fill(self.__USER_PASSWORD,"Miri123")
        self.click(self.__SIGN_IN)
        print(self.page.locator(".msgContent").inner_text())

    #test 18
    def error_alert_incorrect_email_and_password(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ADDRESS,"miri@gamil.com")
        self.fill(self.__USER_PASSWORD,"Mypassword789")
        self.click(self.__SIGN_IN)
        self.click(self.page.locator(".msgContent").inner_text())

    #test 19
    def change_language_button_in_login(self):
        self.click(self.__USER_BTN)
        self.page.locator(".header-country-flag").click()


    #test 20
    def show_button(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ADDRESS,"miri4@gmail.com")
        self.fill(self.__USER_PASSWORD,"Miri123")
        self.click(self.__SHOW_PASSWORD)


    #test 21
    def forget_Your_Password_button(self):
        self.click(self.__USER_BTN)
        self.click(self.__FORGETTING_PASSWORD)

    #test 22
    def reset_password_options(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ADDRESS, "miri4@gmail.com")
        self.click(self.__FORGETTING_PASSWORD)
        self.click(self.__RESET_PASSWORD)


    #test 23
    def remember_email(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ADDRESS,"miri4@gmail.com")
        self.page.dblclick(self.__REMEMBER_EMAIL)
        self.page.goto("https://www.next.co.il/en")
        self.click(self.__USER_BTN)




    def __init__(self, page: Page):
         self.page = page
         super().__init__(page)

