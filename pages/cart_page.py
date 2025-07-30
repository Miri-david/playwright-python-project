
from playwright.sync_api import Page
from pages.Base_page import BasePage
from pytest_playwright.pytest_playwright import page

class CartPage(BasePage):

    __CLICK_TOOLBAR="#pdp-description-form > div.pdp-css-5e8q5w > div:nth-child(2) > div.pdp-css-13b6bqt > div > div"
    __SELECT_OPTION=".pdp-css-ti795y"
    __ADD_TO_BAG=".pdp-css-vuq5s4"
    __BAG=".shoppingbag.header-1nxssqr"
    __REMOVE_ITEMS_BTN=".sbm-idDeleteButton"
    __VIEW_BAG=".header-53gc78"
    __CHECKOUT= ".header-5lt4ux > a"
    __ADD_PRODUCT_BY_ONE=".qty-plus"




    def __init__(self ,page:Page):
        self.page=page
        super().__init__(page)


    #test 24
    def purchase_purchase_an_item_cart(self):
        self.page.goto("https://www.next.co.il/en/style/su184329/k80433#k80433")
        self.click(self.__ADD_TO_BAG)
        self.click(self.__BAG)


    #test 25
    def amount_of_items_cart_visibility(self):
        self.page.goto("https://www.next.co.il/en/style/su184329/k80433#k80433")

        self.click(self.__ADD_TO_BAG)
        self.click(self.__BAG)
        print(self.page.locator(".header-12fmmev").inner_text())


    #test 26
    def remove_items_in_cart(self):
        self.page.goto("https://www.next.co.il/en/style/su184329/k80433#k80433")
        self.click(self.__ADD_TO_BAG)
        self.click(self.__BAG)
        self.click(self.__VIEW_BAG)
        self.click(self.__REMOVE_ITEMS_BTN)
        print(self.page.locator(".sfl-item-count").inner_text())


    # test 27
    def saved_items_after_exit(self):
        self.page.goto("https://www.next.co.il/en/style/su184329/k80433#k80433")
        self.click(self.__ADD_TO_BAG)
        self.click(self.__BAG)
        self.click(self.__VIEW_BAG)
        self.page.goto("https://www.next.co.il/en/")
        self.click(self.__BAG)
        print(self.page.locator(".header-13pbzqv").inner_text())


    #test 28
    def adding_a_product_to_the_shopping_cart(self):
        self.page.goto("https://www.next.co.il/en/style/su184329/k80433#k80433")
        self.click(self.__ADD_TO_BAG)
        self.click(self.__BAG)
        self.click(self.__VIEW_BAG)
        self.click(self.__ADD_PRODUCT_BY_ONE)












