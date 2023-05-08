from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_goods()
        self.should_be_text_basket_is_empty()

    def should_be_no_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), "Basket is not empty"

    def should_be_text_basket_is_empty(self):
        text_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert text_in_basket == "Your basket is empty. Continue shopping", f"Basket is not empty"
