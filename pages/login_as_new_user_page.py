
from pages.Base_page import BasePage
from playwright.sync_api import Page


class LoginASNewUserPage(BasePage):

    __USER_BTN = ".header-1g16tvz:nth-child(1)"
    __REGISTRATION_BTN= "#registrationBtn"
    __TITLE_NAME="#Title"
    __GENDER="#Title > option:nth-child(4)"
    __FIRST_NAME="#FirstName"
    __LAST_NAME="#LastName"
    __EMAIL="#Email"
    __PASSWORD="#Password"
    __PHONE_NUMBER="#PhoneNumber"
    __ADDRESS_NAME="#AddressLine2"
    __CITY="#AddressLine4"
    __ZIP_CODE="#AddressLine6"
    __FINISH_REGISTRATION= "#SignupButton"



    def __init__(self, page: Page):
         self.page = page
         super().__init__(page)



    #test 10
    def registration_new_user(self):
     self.click(self.__USER_BTN)
     self.click(self.__REGISTRATION_BTN)
     self.select_option(self.__TITLE_NAME,"Miss")
     self.fill(self.__FIRST_NAME,"miri")
     self.fill(self.__LAST_NAME,"david")
     self.fill(self.__EMAIL,"miridavid25@gmail.com")
     self.fill(self.__PASSWORD,"Md123456")
     self.fill(self.__PHONE_NUMBER,"0522297572")
     self.fill(self.__ADDRESS_NAME,"12345")
     self.fill(self.__CITY,"ashdod")
     self.fill(self.__ZIP_CODE,"128752")
     self.click(self.__FINISH_REGISTRATION)


    #test 11
    def registration_with_invalid_email(self):
        self.click(self.__USER_BTN)
        self.click(self.__REGISTRATION_BTN)
        self.select_option(self.__TITLE_NAME, "Miss")
        self.fill(self.__FIRST_NAME, "miri")
        self.fill(self.__LAST_NAME, "david")
        self.fill(self.__EMAIL, "1123.com")
        self.fill(self.__PASSWORD, "Md123456")
        self.fill(self.__PHONE_NUMBER, "0522297572")
        self.fill(self.__ADDRESS_NAME, "12345")
        self.fill(self.__CITY, "ashdod")
        self.fill(self.__ZIP_CODE, "128752")
        self.click(self.__FINISH_REGISTRATION)
        print(self.page.locator("#Email-error").inner_text())

    #test 12
    def registration_with_2_character_password(self):
        self.click(self.__USER_BTN)
        self.click(self.__REGISTRATION_BTN)
        self.fill(self.__FIRST_NAME, "miri")
        self.fill(self.__LAST_NAME, "david")
        self.fill(self.__EMAIL, "m1223@gmail.com")
        self.fill(self.__PASSWORD, "12")
        self.fill(self.__PHONE_NUMBER, "0522297572")
        self.fill(self.__ADDRESS_NAME, "12345")
        self.fill(self.__CITY, "ashdod")
        self.fill(self.__ZIP_CODE, "128752")
        self.click(self.__FINISH_REGISTRATION)
        print(self.page.locator("#Password-error").inner_text())


    #test 13
    def registration_numbers_in_name(self):
        self.click(self.__USER_BTN)
        self.click(self.__REGISTRATION_BTN)
        self.fill(self.__FIRST_NAME, "17985")
        self.fill(self.__LAST_NAME, "david")
        self.fill(self.__EMAIL, "miri1128@gmail.com")
        self.fill(self.__PASSWORD, "Md123456")
        self.fill(self.__PHONE_NUMBER, "0522297572")
        self.fill(self.__ADDRESS_NAME, "12345")
        self.fill(self.__CITY, "ashdod")
        self.fill(self.__ZIP_CODE, "128752")
        self.click(self.__FINISH_REGISTRATION)
        print(self.page.locator("#FirstName-error").inner_text())


    #test 14
    def change_language_button_in_registration(self):
        self.click(self.__USER_BTN)
        self.click(self.__REGISTRATION_BTN)
        self.page.locator(".countrylangselector.header-2d1dy4").is_enabled()
