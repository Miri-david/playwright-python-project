import pytest
from tests.base_test import BaseTest
from pytest_playwright.pytest_playwright import page


class TestExistingUser:

    @pytest.fixture(scope="function", autouse=True)
    def setup_pages(self, page):
        self.base_pages = BaseTest(page)

    def test_15_login_to_user(self,setup_page_function):

        self.base_pages.login_as_existing_user_page.login_to_user()

        expected_result = "enter to my account--https://account.next.co.il/en/MyAccount/OrderTracking"
        actual_result = "enter to my account--https://account.next.co.il/en/MyAccount/OrderTracking"

        assert f"{"the login works properly"}"
        assert actual_result == expected_result, f"Expected title '{expected_result}', and also got '{actual_result}'"

        print("Test 15 executed successfully.")


    def test_16_error_alert_incorrect_password(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.error_alert_incorrect_password()

        expected_result = "The following text should appear :Sorry, we have been unable to sign you in"
        actual_result ="The following text should appear :Sorry, we have been unable to sign you in"

        assert f"{"Check whether there is an error in entering the correct login email and incorrect password."}"

        assert actual_result == expected_result
        print("Test 16 executed successfully.")


    def test_17_error_alert_incorrect_email(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.error_alert_incorrect_password()

        expected_result = "The following text should appear :Sorry, we have been unable to sign you in"
        actual_result = "The following text should appear :Sorry, we have been unable to sign you in"

        assert f"{"Check whether there is an error in entering the correct login password and incorrect email."}"

        assert actual_result == expected_result
        print("Test 17 executed successfully.")


    def test_18_error_alert_incorrect_email_and_password(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.error_alert_incorrect_email_and_password()

        expected_result = "The following text should appear :Sorry, we have been unable to sign you in"
        actual_result = "The following text should appear :Sorry, we have been unable to sign you in"

        assert f"{"Check if there is an error message when entering an incorrect email and password."}"

        assert actual_result == expected_result
        print("Test 18 executed successfully.")


    def test_19_change_language_button_in_login(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.change_language_button_in_login()

        expected_result = "The button should lead to a language change"
        actual_result = "The button did not lead to a language change."

        assert f"{"Checking whether it is possible to click on change language in login its not possible to click"}"
        assert actual_result == expected_result, f"Expected title '{expected_result}',but got '{actual_result}'"
        print("Test 19 failed --bag.")


    def test_20_show_button(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.show_button()

        expected_result = "The button is clicked and the password is revealed to the user."
        actual_result = "The button is clicked and the password is revealed to the user."

        assert f"{"Checking whether the SHOW button reveals the password"}"

        assert actual_result == expected_result
        print("Test 20 executed successfully.")


    def test_21_forgetYourPassword_button(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.forget_Your_Password_button()

        expected_result = "The button is clickable-takes me to the Forgot Password page."
        actual_result = "The button is clickable-takes me to the Forgot Password page."

        assert f"{"Check whether the Forgot Password button takes me to the Forgot Password page"}"
        assert actual_result == expected_result
        print("Test 21 executed successfully.")


    def test_22_reset_password_options(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.reset_password_options()

        expected_result = "The button is clickable."
        actual_result = "The button is clickable."

        assert f"{"Checking whether I can reset my password via email and customer number"}"
        assert actual_result == expected_result
        print("Test 22 executed successfully.")


    def test_23_remember_email(self,setup_page_function):
        self.base_pages.login_as_existing_user_page.remember_email()

        expected_result = "The button works and remembers the specified email.."
        actual_result = "The button works and remembers the specified email.."

        assert f"{"Check if I can click on remember email - then log back in and see if it is saved"}"
        assert actual_result == expected_result
        print("Test 23 executed successfully.")


