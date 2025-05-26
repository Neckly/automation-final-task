from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

# pytest -v --tb=line --language=en -m need_review
# в test_user_can_add_product_to_basket и test_guest_can_add_product_to_basket есть тесты с промо ссылками. Для правильной работы с ними
# нужно откомментировать @pytest.parametrize, ссылку с offer, alert, и добавить offer в параметры теста (self, browser, offer). Закомментить другую ссылку

@pytest.mark.user   
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "password"
        page.register_new_user(email, password)
        page.should_be_authorized_user() # сетап авторизации гостя
    
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(browser, link)
     page.open()
    
     page.add_to_bucket()
     page.should_not_be_success_message() # проверка, что юзер не видит уведомление об успешном добавлении товара в корзину
     
    @pytest.mark.need_review
    #@pytest.mark.parametrize('offer', ['?promo=offer0', '?promo=offer1', '?promo=offer2', '?promo=offer3', '?promo=offer4', '?promo=offer5', '?promo=offer6', pytest.param('?promo=offer7', marks=pytest.mark.xfail), '?promo=offer8', '?promo=offer9'])
    def test_user_can_add_product_to_basket(self, browser):
     #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}" # offer добавить в параметр (после r_browser)
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(browser, link)
     page.open()
     page.add_to_bucket()
     #page.alert_solve_quiz_and_get_code()
     time.sleep(3)
     page.should_be_right_book()
     page.should_be_right_price() # проверка добавления юзером товара в корзину и проверка корректного названия книги и цены
     # иногда может не запуститься с первого раза(из-за ожидания)! Если было провалено - запустить тест снова.
     
@pytest.mark.need_review
#@pytest.mark.parametrize('offer', ['?promo=offer0', '?promo=offer1', '?promo=offer2', '?promo=offer3', '?promo=offer4', '?promo=offer5', '?promo=offer6', pytest.param('?promo=offer7', marks=pytest.mark.xfail), '?promo=offer8', '?promo=offer9'])
def test_guest_can_add_product_to_basket(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}" # offer добавить в параметр (после r_browser)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_bucket()
    #page.alert_solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_right_book()
    page.should_be_right_price() # проверка добавления товара в корзину для гостя и проверка корректного названия книги и цены
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    
    page.add_to_bucket()
    page.should_not_be_success_message() # проверка, что гость не видит уведомление об успешности добавления товара в корзину
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    
    page.add_to_bucket()
    page.should_be_success_message_is_disappeared() # проверка исчезновения сообщения о добавлении товара в корзину для гостя
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() # проверка видимости ссылки на логин
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page() # проверка перехода на страницу логина с главной страницы для гостя
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    browser.implicitly_wait(5)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message() # проверка, что есть сообщение о пустой корзине для гостя
    
def test_guest_can_see_empty_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket() # проверка, что в корзине нету товара для гостя. Негатив-тест верхней проверки(он не отрицательный!)
    