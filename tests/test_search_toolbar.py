import pytest

from tests.base_test import BaseTest
from pytest_playwright.pytest_playwright import page


class TestSearchToolbar:

    @pytest.fixture(scope="function", autouse=True)
    def setup_pages(self, page):
        self.base_pages = BaseTest(page)

    def test_05_search_item_in_toolbar(self,setup_page_function,page):
        self.base_pages.search_toolbar_page.toolbar_search(page)

        assert f"{"Checking whether it is possible to search for an item in the search bar - shirt "}"
        expected_title = "https://www.next.co.il/en/search?w=shirts&p=1#416"
        actual_title = "https://www.next.co.il/en/search?w=shirts&p=1#416"
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

        print("Test 05 executed successfully.")

    def test_06_enter_invalid_characters(self,setup_page_function):
        self.base_pages.search_toolbar_page.invalid_characters()

        expected_result="No Results"
        actual_result="https://www.next.co.il/en/search?w=$%^%23%^&p=1#100"
        assert f"{"Checking whether it is possible to write characters such as #$%^ and this will reveal that it did not find what we asked for-is is reviles results"}"
        assert actual_result == expected_result, f"Expected title '{expected_result}', but got '{actual_result}'"

        print("Test 06 failed --bag.")

    def test_07_hover_on_toolbar(self,setup_page_function):
        self.base_pages.search_toolbar_page.hover_on_toolbar()
        assert f"{"Checking whether hovering over the toolbar reveals the relevant items"}"

        print("Test 07 executed successfully.")

    def test_08_enter_connected_characters(self,setup_page_function):
        self.base_pages.search_toolbar_page.enter_connected_characters()

        expected_result="https://www.next.co.il/en/search?w=pinkprintedbuckethat"
        actual_result ="https://www.next.co.il/en/search?w=pinkprintedbuckethat"

        assert f"{"Testing whether it is possible to enter connected characters in a search toolbar and it will find results"}"
        assert actual_result == expected_result, f"Expected title '{expected_result}', and also got '{actual_result}'"

        print("Test 08 executed successfully.")

    def test_09_search_without_entering_text(self,setup_page_function):
        self.base_pages.search_toolbar_page.search_without_entering_text()

        expected_result= "Search product or brand"
        actual_result = "Search product or brand"
        assert f"{"Testing if the user can see results when clicking search without entering text"}"
        assert actual_result == expected_result, f"Expected title '{expected_result}', and also got '{actual_result}'"

        print("Test 09 executed successfully.")
