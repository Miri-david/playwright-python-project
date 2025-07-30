import pytest
from pages.Favourites_page import FavouritesPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_as_existing_user_page import LoginExistingUserPage
from pages.login_as_new_user_page import LoginASNewUserPage
from pages.search_toolbar_page import SearchToolbarPage
from utils.config_reader import ConfigReader

from playwright.sync_api import Page

# @pytest.fixture(scope="class")

def setup_page_class(request, browser, page=None):
    url = ConfigReader.read_config("global", "url")
    page.goto(url)
    request.cls.page = browser.new_page()

    request.cls.page.goto("https://www.next.co.il/en")

    request.cls.Home_page = HomePage(request.cls.page)

    request.cls.Search_toolbar_page = SearchToolbarPage(request.cls.page)

    request.cls.Login_as_gest_page = LoginExistingUser3Page(request.cls.page)

    request.cls.Login_as_new_user_page =Loginasnewuser4Page(request.cls.page)

    request.cls.Cart_page = Cart5Page(request.cls.page)

    request.cls.Favourites_page = Favourites6Page(request.cls.page)




    yield

    request.cls.page.close()

    browser.close()


import pytest





@pytest.fixture(scope="function")

def setup_page_function(request,page:Page):
    url=ConfigReader.read_config("global","url")
    page.goto(url)
    request.cls.page = page


    request.cls.home_page = HomePage(request.cls.page)

    request.cls.search_toolbar_page = SearchToolbarPage(request.cls.page)

    request.cls.Login_as_gest_page = LoginExistingUserPage(request.cls.page)

    request.cls.Login_as_new_user_page =LoginASNewUserPage(request.cls.page)

    request.cls.Cart_page = CartPage(request.cls.page)

    request.cls.Favourites_page = FavouritesPage(request.cls.page)




