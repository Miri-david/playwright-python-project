from playwright.sync_api import Page
from pages.Base_page import BasePage
from pytest_playwright.pytest_playwright import page



class FavouritesPage(BasePage):

    __ADD_TO_FAVOURITES="#product-summary-favourites-icon-AT4656"
    __FAVOURITES_BUTTON=".header-4rkvz6"
    __REMOVE_ITEM=".remove-item-link"
    __ADD_TO_FAVOURITES_BUTTON1="#product-summary-favourites-icon-D41274"
    __TOOLBAR_SEARCH= "#header-big-screen-search-box"
    __SEARCH_BTN=".header-1298jtw"



    def __init__(self ,page:Page):
        self.page=page
        super().__init__(page)


    # test 29
    def add_favorite_items(self):
        self.page.goto("https://www.next.co.il/en/shop/gender-women-category-dresses-0")
        self.click(self.__ADD_TO_FAVOURITES)
        print(self.page.locator(".produc-1ccjn3s").inner_text())



     #test 30
    def remove_favorite_items(self):
        self.page.goto("https://www.next.co.il/en/shop/gender-women-category-dresses-0")
        self.click(self.__ADD_TO_FAVOURITES)
        self.click(self.__FAVOURITES_BUTTON)
        self.click(self.__REMOVE_ITEM)


    #test 31
    def moving_a_product_from_favorites_to_cart(self):
        self.page.goto("https://www.next.co.il/en/shop/gender-women-category-dresses-0")
        self.click(self.__ADD_TO_FAVOURITES)
        self.click(self.__FAVOURITES_BUTTON)
        self.page.locator(".primary.enabled").click()


    # test 32
    def number_of_products_in_favorites(self):
        self.page.goto("https://www.next.co.il/en?gad_source=1&gad_campaignid=244843994&gbraid=0AAAAADn-_y8LK3jM7o9PHtMubSkF0xvBl&gclid=Cj0KCQjwhO3DBhDkARIsANxrhTqQQeF2r54c3WCV-63RCh-rMKcdau_VicfhBzWe20itswr46-Dmi00aApryEALw_wcB&gclsrc=aw.ds")
        self.fill(self.__TOOLBAR_SEARCH,"Natural Country Ceramic Lydford Medium Textured Flower Vase")
        self.click(self.__SEARCH_BTN)
        self.click(self.__ADD_TO_FAVOURITES_BUTTON1)
        self.page.locator("#product-summary-favourites-icon-K75184").click()
        self.click(self.__FAVOURITES_BUTTON)
        print(self.page.locator("#favouriteItemsCountTarget").inner_text())













