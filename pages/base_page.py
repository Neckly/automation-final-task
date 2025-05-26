from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasePage():
    
    def __init__(self, r_browser, url):
        self.r_browser = r_browser
        self.url = url
    
    def open(self):
        self.r_browser.get(self.url) # метод для открытия ссылки
        
    def __init__(self, r_browser, url, timeout=3):
      self.r_browser = r_browser
      self.url = url
      self.r_browser.implicitly_wait(timeout)
      
    def go_to_login_page(self): # метод для автоматического открытия страницы логина (с главной страницы?)
        link = self.r_browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self): # метод для проверки ссылки на страницу логина
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        
    def go_to_basket_page(self): # метод для перехода в корзину
        link = self.r_browser.find_element(*BasketPageLocators.GO_TO_BASKET)
        link.click()
        
    def should_be_authorized_user(self): # метод проверки логина пользователя
     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
      
    def is_element_present(self, how, what): # метод поиска элемента через селектор
     try:
        self.r_browser.find_element(how, what)
     except NoSuchElementException:
        return False
     return True
  
    def is_not_element_present(self, how, what, timeout=4): # метод проверяет, что элемент НЕ появляется на странице в течение заданного времени
     try:
        WebDriverWait(self.r_browser, timeout).until(EC.presence_of_element_located((how, what)))
     except TimeoutException:
        return True

     return False
  
    def is_disappeared(self, how, what, timeout=4): # метод для проверки исчезновения элемента в течение определеного времени
     try:
        WebDriverWait(self.r_browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
     except TimeoutException:
         return False

     return True
 
    def solve_quiz_and_get_code(self):
        alert = self.r_browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
           alert = self.r_browser.switch_to.alert
           alert_text = alert.text
           print(f"Your code: {alert_text}")
           alert.accept()
        except NoAlertPresentException:
           print("No second alert presented")