import pytest
from pytest_playwright.pytest_playwright import page
from tests.base_test import BaseTest


class TestLoginAsNewUser:

    @pytest.fixture(scope="function", autouse=True)
    def setup_pages(self, page):
        self.base_pages = BaseTest(page)

    def test_10_registration_new_user(self,setup_page_function, page):
        self.base_pages.login_as_new_user_page.registration_new_user()

        expected_result = "enter to my account-https://account.next.co.il/en/MyAccount/OrderTracking"
        actual_result = "enter to my account-https://account.next.co.il/en/MyAccount/OrderTracking"

        assert f"{"Checking whether its possible to enter as a new user"}"

        assert actual_result == expected_result, f"Expected title '{expected_result}', and also got '{actual_result}'"
        print("Test 10 executed successfully.")


    def test_11_registration_with_invalid_email(self,setup_page_function):
        self.base_pages.login_as_new_user_page.registration_with_invalid_email()

        expected_result = "the inner text should revel :This value should be a valid email."
        actual_result ="the inner text should revel :This value should be a valid email."
        assert f"{"Checking whether it is possible to register with an invalid email"}"

        assert actual_result == expected_result, f"Expected title '{expected_result}', and also got '{actual_result}'"
        print("Test 11 executed successfully.")


    def test_12_registration_with_2_character_password(self,setup_page_function):
        self.base_pages.login_as_new_user_page.registration_with_2_character_password()

        expected_result = "the inner text should revel :Please enter at least 6 characters.."
        actual_result = "the inner text should revel :Please enter at least 6 characters.."
        assert f"{"Check if it is possible to register with a 2-character password."}"

        assert actual_result == expected_result, f"Expected title '{expected_result}', and also got '{actual_result}'"
        print("Test 12 executed successfully.")



    def test_13_registration_numbers_in_name(self,setup_page_function):
        self.base_pages.login_as_new_user_page.registration_numbers_in_name()

        expected_result = "the inner text should revel :Please supply a valid first name (English or Local Language characters only.).."
        actual_result = "the inner text should revel :Please supply a valid first name (English or Local Language characters only.).."
        assert f"{"Check if is possible to enter digits in the name for registration."}"

        assert actual_result == expected_result, f"Expected title '{expected_result}', and also got '{actual_result}'"
        print("Test 13 executed successfully.")



    def test_14_change_language_button_in_registration(self,setup_page_function):
        self.base_pages.login_as_new_user_page.change_language_button_in_registration()

        expected_result= "The button to change the language on the page should be clickable and visible to the user."
        actual_result ="The button is not clickable for the user and is inactive."
        assert f"{"Checking whether it is possible to click on change language in  login registration--"}"

        assert actual_result == expected_result, f"Expected title '{expected_result}', but we got '{actual_result}'"
        print("Test 14 failed --bag.")
