from selenium.webdriver.common.by import By


class MainPageLocator():
    # header components Locators
    header_text_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[1]/p')
    logo_xpath = (By.XPATH,'/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[1]/a/img')
    login_button = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/button')
    catalog_button = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[1]/button[2]')
    cart_icon_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a[2]/i')
    cart_Icon_text_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a['
                                      '1]/span')
    heart_icon_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a[1]/i')
    heart_icon_text_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a['
                                       '2]/span')

