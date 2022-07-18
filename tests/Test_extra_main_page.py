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
@allure.story("I test main page tests")
class Test_Main_page:
    def test_check_header_text(self):
        header_text = MP.check_header_text()
        with assume:
            assert header_text.text == "უფასო მიწოდება 50 ლარიდან"
