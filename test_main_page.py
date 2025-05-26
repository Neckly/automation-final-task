import pytest
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    # инициализируем страницу как объект класса
    page = MainPage(browser, link)

    page.open()
    page.go_to_login_page()