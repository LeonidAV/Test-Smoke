import time

from selenium import webdriver
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_buy_product_1():
    driver = webdriver.Firefox(executable_path='D:\Хом драйвер и геко\geckodriver-v0.33.0-win64')

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    print("Finish test 1")
    time.sleep(5)
    driver.quit()
