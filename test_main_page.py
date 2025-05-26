from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser): 
     link = "http://selenium1py.pythonanywhere.com/"
     page = MainPage(browser, link)
     page.open() 
     page.go_to_login_page() # проверка, что гость может перейти на страницу логина
     
    def test_guest_should_see_login_link(self, browser):
     link = "http://selenium1py.pythonanywhere.com/"
     page = MainPage(browser, link)
     page.open()
     page.should_be_login_link() # проверка отображения ссылки на логин для гостя
    
def test_existense_of_bucket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
  
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() # проверка, что гость может перейти на страницу логина с главной страницы
   
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message() # проверка, что гость не видит товар в корзине, открытой с главной страницы
    
def test_guest_can_see_empty_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket() # проверка, что гость видит пустую корзину, переходя с главной страницы