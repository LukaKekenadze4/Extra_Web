from selenium.webdriver.common.by import By


class MainPageLocator:
    # header components Locators
    header_text_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[1]/p')
    logo_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[1]/a/img')
    login_button = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/button')
    catalog_button = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[1]/button[2]')
    cart_icon_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a[2]/i')
    cart_Icon_text_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a['
                                      '2]/span')
    heart_icon_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a[1]/i')
    heart_icon_text_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[1]/div/div[1]/div[3]/a['
                                       '1]/span')

    # navigation components
    sale_button_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[2]/div/div/div/a[1]/span')
    toy_button_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[2]/div/div/div/a[2]')
    technic_button_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[2]/div/div/div/a[3]')
    home_button_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[2]/div/div/div/a[4]')
    sport_button_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[2]/div/div/div/a[5]')
    beautiful_button_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[2]/div/div/div/a[6]')
    all_button_xpath = (By.XPATH, '/html/body/app-root/app-header/header/div/div[2]/div[2]/div/div/div/a[7]')

    # bullets
    bullet_1 = (By.XPATH, '//*[@id="router-holder"]/ng-component/div[1]/app-hero-slider/div[2]/div/div[1]/div/i')
    bullet_2 = (By.XPATH, '//*[@id="router-holder"]/ng-component/div[1]/app-hero-slider/div[2]/div/div[2]/div/i')
    bullet_3 = (By.XPATH, '//*[@id="router-holder"]/ng-component/div[1]/app-hero-slider/div[2]/div/div[3]/div/i')
    bullet_4 = (By.XPATH, '//*[@id="router-holder"]/ng-component/div[1]/app-hero-slider/div[2]/div/div[4]/div/i')
    bullet_5 = (By.XPATH, '//*[@id="router-holder"]/ng-component/div[1]/app-hero-slider/div[2]/div/div[5]/div/i')
    bullet_6 = (By.XPATH, '//*[@id="router-holder"]/ng-component/div[1]/app-hero-slider/div[2]/div/div[6]/div/i')

    banner_xpath = (By.XPATH,
                    '/html/body/app-root/div[1]/ng-component/div[1]/app-hero-slider/div[1]/div[2]/div/swiper/div/div[12]/a/div/picture/img')

    add_to_cart_button = (By.XPATH, '//*[@id="swiper-wrapper-ec106a7eba1e804ed"]/div[2]/app-product-card/div/button')
