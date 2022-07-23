# Basic Imports
import allure
from pytest import assume
from driver import Driver
import time
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Pages Imports
from pages.MainPage import MainPage

# clear reports files(images/allure)

MP = MainPage()

import os

mypath = "reports/images"
mypath1 = "reports/allure"
for root, dirs, files in os.walk(mypath):
    for file in files:
        os.remove(os.path.join(root, file))

for root, dirs, files in os.walk(mypath1):
    for file in files:
        os.remove(os.path.join(root, file))


@allure.feature("MainPageTests")
@allure.story("I test main page")
class Test_Main_page:
    @allure.title("check header's components")
    @allure.description("we should check all texts and elements in the header")
    def test_check_header_text(self):
        header_text = MP.check_header_text()
        logo = MP.check_logo_is_displayed().is_displayed()
        login_button = MP.check_login_button_is_displayed()
        catalog_button = MP.check_catalog_button_is_displayed().is_displayed()
        cart_icon = MP.check_cart_icon_is_displayed()
        cart_icon_text = MP.check_cart_icon_text()
        heart_icon = MP.check_heart_icon_is_displayed()
        heart_icon_text = MP.check_heart_icon_text()

        with assume: assert header_text.text == "უფასო მიწოდება 50 ლარიდან"
        with assume: assert Driver.driver.title == "🎁 Extra.ge - რაც გაგიხარდება"
        with assume: assert logo == True
        with assume: assert login_button.is_displayed() == True
        with assume: assert login_button.text == "შესვლა"
        with assume: assert catalog_button == True
        with assume: assert cart_icon.is_displayed() == True
        with assume: assert cart_icon_text.text == "კალათა"
        with assume: assert heart_icon.is_displayed() == True
        with assume: assert heart_icon_text.text == 'შენახული'

    @allure.title("check navigations's components")
    @allure.description("we should check all texts in navigation component")
    def test_navigation_components(self):
        nav_comp = []
        all_items = MP.check_navigation_component()
        for i in range(len(all_items)):
            nav_comp.append(all_items[i].text)
        texts = ['ფასდაკლებები', 'სათამაშოები', 'ტექნიკა', 'სახლი და ეზო', 'სპორტი და მოგზაურობა',
                 'სილამაზე და ჯანმრთელობა', 'ყველას ნახვა']
        for j in range(len(nav_comp)):
            with assume: assert texts[j] == nav_comp[j]

    def test_check_bullets(self):
        all_bullets = MP.check_bullets()
        for i in range(len(all_bullets)):
            bull = all_bullets[i]
            bull.click()

    def test_check_banner_click(self):
        MP.check_banner_click().click()
        time.sleep(2)
        with assume: assert 'Soskin | Extra' in Driver.driver.title
        Driver.driver.back()

    def test_click_cart_icon(self):
        add_to_cart_button = MP.click_cart_icon()
        # y = add_to_cart_button.rect()['y']
        # Driver.driver.execute_script("window.scrollTo(0, {})".format(y))
        add_to_cart_button.click()
        # with assume: assert add_to_cart_button[1].text == 'კალათაში დამატება'
