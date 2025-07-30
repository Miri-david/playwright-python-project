
from pages.Favourites_page import FavouritesPage

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_as_existing_user_page import LoginExistingUserPage
from pages.login_as_new_user_page import LoginASNewUserPage
from pages.search_toolbar_page import SearchToolbarPage



class BaseTest:
    def __init__(self, page):
        self.page=page
        self.home_page=HomePage(page)
        self.search_toolbar_page=SearchToolbarPage(page)
        self.login_as_existing_user_page=LoginExistingUserPage(page)
        self.login_as_new_user_page=LoginASNewUserPage(page)
        self.cart_page=CartPage(page)
        self.favourites_page=FavouritesPage(page)












