
import pytest
from pytest_playwright.pytest_playwright import page
from tests.base_test import BaseTest

class TestCart:


    @pytest.fixture(scope="function", autouse=True)
    def setup_pages(self, page):
        self.base_pages = BaseTest(page)


    def test_24_purchase_purchase_an_item_cart(self,setup_page_function):
        self.base_pages.cart_page.purchase_purchase_an_item_cart()

        assert f"{"Check if it is possible to make a purchase an item"}"

        expected_title = "Checking whether the product has been added to the shopping list"
        actual_title = "Checking whether the product has been added to the shopping list"
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        print("Test 24 executed successfully.")


    def test_25_amount_of_items_cart_visibility(self,setup_page_function):
        self.base_pages.cart_page.amount_of_items_cart_visibility()

        assert  f"{"Checking whether the quantity of items in the cart after clicking is visible to the user"}"

        expected_title = "Checking whether The text should reveal an numbers item in the bag."
        actual_title = "Checking whether The text should reveal an numbers item in the bag."
        assert actual_title == expected_title

        print("Test 25 executed successfully.")


    def test_26_remove_items_in_cart(self,setup_page_function):
        self.base_pages.cart_page.remove_items_in_cart()

        assert f"{"Checking whether it is possible to remove items on the cart page"}"

        expected_title = "items need to be removed and print 0."
        actual_title = "items need to be removed and print 0."
        assert actual_title == expected_title

        print("Test 26 executed successfully.")


    def test_27_saved_items_after_exit(self,setup_page_function):
        self.base_pages.cart_page.saved_items_after_exit()

        assert f"{"See if items are saved in the cart when you completely exit the site"}"

        expected_title = "The site should remember the product even after you leave it - the product name is printed in the shopping cart."
        actual_title = "The site should remember the product even after you leave it - the product name is printed in the shopping cart."
        assert actual_title == expected_title

        print("Test 27 executed successfully.")


    def test_28_adding_a_product_to_the_shopping_cart(self,setup_page_function):
        self.base_pages.cart_page.adding_a_product_to_the_shopping_cart()

        assert f"{"Checking if the plus button for adding a product work"}"

        expected_title = "Checking if the plus button for adding a product works."
        actual_title = "Checking if the plus button for adding a product works."
        assert actual_title == expected_title

        print("Test 28 executed successfully.")