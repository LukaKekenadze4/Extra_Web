from pages.BasePage import BasePage as BP
from locators.MainPageLocator import MainPageLocator

MPL = MainPageLocator()


class MainPage(BP):
    def __init__(self):
        pass

    def check_header_text(self):
        header_text = BP.find_element(self, MPL.header_text_xpath)
        return header_text
