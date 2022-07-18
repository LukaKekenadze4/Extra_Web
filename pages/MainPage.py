from pages.BasePage import BasePage as BP
from locators.MainPageLocator import MainPageLocator

MPL = MainPageLocator()


class MainPage(BP):
    def __init__(self):
        pass

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

