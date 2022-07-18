from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    """
        this is the configuration of driver
    """
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window()
    # driver.set_window_size(1440, 768)
    driver.get("https://extra.ge/")
    driver.implicitly_wait(10)
    print("Driver initialized. {a}".format(a=driver.title))
