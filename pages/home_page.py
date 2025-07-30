
from playwright.sync_api import Page
from pages.Base_page import BasePage

class HomePage(BasePage):

    __LANGUAGE_BTN=".header-sor9qu:nth-child(1)"
    __CHANGE_LANG_BTN= ".header-uirxd5"

    __USER_BTN=".header-1g16tvz:nth-child(1)"
    __EMAIL_ACCOUNT="#username"
    __PASSWORD_ACCOUNT="#password"
    __SIGN_IN_BTN=".c5d45fb63"

    __NEXT_ICON= ".header-bcqwvy:nth-child(1)"


    def __init__(self ,page:Page):
        self.page=page
        super().__init__(page)

    #test1
    def open_home_page(self,url="https://www.next.co.il/"):
        self.page.goto(url)


    #test2
    def change_lang(self):
        self.click(self.__LANGUAGE_BTN)
        self.click(self.__CHANGE_LANG_BTN)


    #test3
    def user_connaction(self):
        self.click(self.__USER_BTN)
        self.fill(self.__EMAIL_ACCOUNT,"miridavid22@gmail.com")
        self.fill(self.__PASSWORD_ACCOUNT,"Miri12124")
        self.click(self.__SIGN_IN_BTN)
        self.open_home_page()
        self.click(self.__USER_BTN)
        self.page.get_by_test_id('a[data-testid="header-my-account-container-tooltip-title"]')


    #test4
    def next_icon(self):
        self.page.locator("#meganav-link-0").click()
        self.click(self.__NEXT_ICON)



