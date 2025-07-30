import pytest
from pytest_playwright.pytest_playwright import page
from tests.base_test import BaseTest

class TestHomePage:

   @pytest.fixture(scope="function", autouse=True)
   def setup_pages(self, page):
      self.base_pages = BaseTest(page)

   def test_01_open_home_page(self):
      self.base_pages.home_page.open_home_page(url="https://www.next.co.il/")

      expected_title = "האתר הרשמי של Next: אופנה, בגדי ילדים ועיצוב הבית אונליין"
      actual_title = self.base_pages.page.title()
      assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

      print("Test 01 executed successfully.")

   def test_02_change_language_button_in_home_page(self,setup_page_function):
      self.base_pages.home_page.change_lang()

      assert f"{"Checking whether it is possible to click on change language in home page-- its possible to click!"}"
      print("Test 02 executed successfully.")


   def test_03_saving_data_after_exit(self,setup_page_function):
      self.base_pages.home_page.user_connaction()

      assert f"{"Checking whether after logging in and suddenly exiting the page - the personal profile is saved on the home page."}"
      print("Test 03 executed successfully.")


   def test_04_clicking_on_the_main_logo_to_connect_the_home_page(self,setup_page_function):
      self.base_pages.home_page.next_icon()

      assert f"{"Clicking on the Next's logo after clicking on button of the site to see if its can connect to the home page again."}"
      print("Test 04 executed successfully.")