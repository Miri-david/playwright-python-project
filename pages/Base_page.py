from playwright.sync_api import Page


class BasePage:
    def __init__(self, page:Page):
        self.page=page

    def select_option(self,selector:str,text:str):
        self.page.locator(selector).select_option(text)

    def fill(self,selector:str,text:str)->None:
        self.page.locator(selector).fill(text)

    def click(self,selector:str):
        self.page.locator(selector).click()