from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '[id = "login_link"]')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REG_FORM = (By.CSS_SELECTOR, '[id="register_form"]')
    FIELD_EMAIL_FOR_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-email")
    FIELD_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-password1")
    FIELD_REPEAT_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    NAME_OF_GOOD = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_OF_GOOD_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    PRICE_OF_GOOD = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_OF_GOOD_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '[id = "login_link"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '[id = "login_link_inc"')
    USER_ICON = (By.CSS_SELECTOR, '[class = "icon-user"]')


class BasketPageLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    GOODS_IN_BASKET = (By.CSS_SELECTOR, '[class = "col-sm-6"]')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
