from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    
    CURRENT_BOOK_ALERT = (By.CSS_SELECTOR, ".alertinner  > strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    
    CURRENT_PRICE_ALERT = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasketPageLocators():
    GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, ".col-sm-6.h3")