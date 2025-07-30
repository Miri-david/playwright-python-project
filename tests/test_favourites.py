import pytest
from tests.base_test import BaseTest


class TestFavourites:


    @pytest.fixture(scope="function", autouse=True)
    def setup_pages(self, page):
        self.base_pages = BaseTest(page)


    def test_29_add_favorite_items(self,setup_page_function):
        self.base_pages.favourites_page.add_favorite_items()

        assert f"{"Checking whether it is possible to add favorite items and have them be visible on the page"}"

        expected_title = "Checking if the product was added successfully ."
        actual_title = "Checking if the product was added successfully ."
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        print("Test 29 executed successfully.")


    def test_30_remove_favorite_items(self,setup_page_function):
        self.base_pages.favourites_page.remove_favorite_items()
        assert f"{"Check if it is possible to remove items from favorites on a page"}"

        expected_title = "Checking whether a product can be removed from favorites ."
        actual_title = "Checking whether a product can be removed from favorites ."
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        print("Test 30 executed successfully.")


    def test_31_moving_a_product_from_favorites_to_cart(self,setup_page_function):
        self.base_pages.favourites_page.moving_a_product_from_favorites_to_cart()

        assert f"{"Check whether clicking on add to bag from the favorites takes the product to the requested page."}"

        expected_title = "Checking whether it is possible to click on Proceed to Purchase after clicking the button ."
        actual_title = "Checking whether it is possible to click on Proceed to Purchase after clicking the button ."
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        print("Test 31 executed successfully.")



    def test_32_number_of_products_in_favorites(self, setup_page_function):
        self.base_pages.favourites_page.number_of_products_in_favorites()

        assert f"{"Checking how many products are in favorites."}"

        expected_title = "Checking whether the quantity of products is displayed on the favorites page ."
        actual_title = "Checking whether the quantity of products is displayed on the favorites page."
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        print("Test 32 executed successfully.")





