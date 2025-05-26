from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def should_be_basket_button(self):
     assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Basket button not found"
    
    def add_to_bucket(self):
        button_basket1 = self.r_browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_basket1.click()
        
    def alert_solve_quiz_and_get_code(self):
        self.solve_quiz_and_get_code()
        
    def should_be_right_book(self):
        expected_result = self.r_browser.find_element(*ProductPageLocators.BOOK_NAME)
        expected = expected_result.text
        actual_result = self.r_browser.find_element(*ProductPageLocators.CURRENT_BOOK_ALERT)
        actual = actual_result.text
        
        assert expected == actual, f"ожидаемое название книги ({expected}) не соответствует актуальному ({actual})"
        
    def should_be_right_price(self):
        expected_result1 = self.r_browser.find_element(*ProductPageLocators.BOOK_PRICE)
        expected1 = expected_result1.text 
        actual_result1 = self.r_browser.find_element(*ProductPageLocators.CURRENT_PRICE_ALERT)
        actual1 = actual_result1.text
        
        assert expected1 == actual1, f"ожидаемая цена книги {expected1} не соответствует актуальной {actual1}"
        
    def should_not_be_success_message(self):
     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
       
    def should_be_success_message_is_disappeared(self):
     assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message isn't disappeared"