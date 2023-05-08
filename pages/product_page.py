import math

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product(self):
        self.should_add_to_cart()
        self.solve_quiz_and_get_code()

    def should_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Button add to cart is not presented"
        self.browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]').click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_correct_price_of_good_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_OF_GOOD_IN_ALERT).text \
               == self.browser.find_element(*ProductPageLocators.PRICE_OF_GOOD).text, \
            "The price of the product in the basket does not match the real price of the product!"

    def should_be_correct_name_of_good_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_GOOD_IN_ALERT).text \
               == self.browser.find_element(*ProductPageLocators.NAME_OF_GOOD).text, \
            "The name of the product in the alert does not match the real name of the product!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_OF_GOOD_IN_ALERT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_OF_GOOD_IN_ALERT), \
            "Success message should disappear, but it has not disappeared!"
