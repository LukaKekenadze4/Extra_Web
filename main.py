import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://extra.ge/')
x = driver.find_element(By.XPATH, '/html/body/app-root/div[1]/ng-component/div[2]/app-home-page-products-carousel[2]/div/div/h3')
driver.execute_script("window.scrollTo(0,{})".format(x.rect['y']))
print(x.rect['y'])
time.sleep(2)
driver.close()