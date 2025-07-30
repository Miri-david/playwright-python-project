
from pytest_playwright.pytest_playwright import page
from pages.Base_page import BasePage
from playwright.sync_api import Page

class SearchToolbarPage(BasePage):

    __TOOLBAR_SEARCH= "#header-big-screen-search-box"
    __SEARCH_BTN="#header-big-screen-search-box:nth-child(1)"


    def __init__(self,page:Page):
        self.page = page
        super().__init__(page)


    def open_home_page(self, url="https://www.next.co.il/"):
            self.page.goto(url)

    #test 5
    def toolbar_search(self, page):
        self.click(self.__TOOLBAR_SEARCH)
        self.fill(self.__TOOLBAR_SEARCH,"shirt")
        self.click(self.__SEARCH_BTN)
        page.title=page.title()

    #test 6
    def invalid_characters(self):
        self.click(self.__TOOLBAR_SEARCH)
        self.fill(self.__TOOLBAR_SEARCH,"$%^#%^")
        self.click(self.__SEARCH_BTN)

    #test 7
    def hover_on_toolbar(self):
        self.page.locator("#meganav-link-3").hover()

    #test 8
    def enter_connected_characters(self):
        self.click(self.__TOOLBAR_SEARCH)
        self.fill(self.__TOOLBAR_SEARCH,"PinkPrintedBucketHat")
        self.click(self.__SEARCH_BTN)

    #test 9
    def search_without_entering_text(self):
        self.click(self.__SEARCH_BTN)
        print(self.page.locator(".header-1f9vf8v").inner_text())

