from pages.BasePage import BasePage as BP
from locators.MainPageLocator import MainPageLocator
import requests
from bs4 import BeautifulSoup

MPL = MainPageLocator()


class MainPage(BP):
    def __init__(self):
        pass

    # header
    def check_header_text(self):
        header_text = BP.find_element(self, MPL.header_text_xpath)
        return header_text

    def check_logo_is_displayed(self):
        logo = BP.find_element(self, MPL.logo_xpath)
        return logo

    def check_login_button_is_displayed(self):
        login_button = BP.find_element(self, MPL.login_button)
        return login_button

    def check_catalog_button_is_displayed(self):
        catalog_button = BP.find_element(self, MPL.catalog_button)
        return catalog_button

    def check_cart_icon_is_displayed(self):
        cart_icon = BP.find_element(self, MPL.cart_icon_xpath)
        return cart_icon

    def check_cart_icon_text(self):
        cart_icon_text = BP.find_element(self, MPL.cart_Icon_text_xpath)
        return cart_icon_text

    def check_heart_icon_is_displayed(self):
        heart_icon = BP.find_element(self, MPL.heart_icon_xpath)
        return heart_icon

    def check_heart_icon_text(self):
        heart_icon_text = BP.find_element(self, MPL.heart_icon_text_xpath)
        return heart_icon_text

    # navigation
    def check_navigation_component(self):
        sale_button = BP.find_element(self, MPL.sale_button_xpath)
        toy_button = BP.find_element(self, MPL.toy_button_xpath)
        technic_button = BP.find_element(self, MPL.technic_button_xpath)
        home_button = BP.find_element(self, MPL.home_button_xpath)
        sport_button = BP.find_element(self, MPL.sport_button_xpath)
        beautiful_button = BP.find_element(self, MPL.beautiful_button_xpath)
        all_button = BP.find_element(self, MPL.all_button_xpath)
        return sale_button, toy_button, technic_button, home_button, sport_button, beautiful_button, all_button

    def check_bullets(self):
        bullet_1 = BP.find_element(self, MPL.bullet_1)
        bullet_2 = BP.find_element(self, MPL.bullet_2)
        bullet_3 = BP.find_element(self, MPL.bullet_3)
        bullet_4 = BP.find_element(self, MPL.bullet_4)
        bullet_5 = BP.find_element(self, MPL.bullet_5)
        bullet_6 = BP.find_element(self, MPL.bullet_6)
        return bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_6

    def check_banner_click(self):
        banner = BP.find_element(self, MPL.banner_xpath)
        return banner

    def scroll_to_day_offer(self):
        day_offer = BP.find_element(self, MPL.day_offer_xpath)
        return day_offer

    def add_to_cart(self):
        add = BP.find_element(self, MPL.add_to_cart_button)
        return add
