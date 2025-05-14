from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

import time

import math

service = Service("C:/Users/desktop/Desktop/tools/chromedriver.exe")

link = "http://suninjuly.github.io/find_link_text"


try:

   # Инициализация Яндекс Браузера

   browser = webdriver.Chrome(service=service)

   browser.get(link)

   link_1 = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
   link_1.click()

   input1 = browser.find_element(By.TAG_NAME, "input")

   input1.send_keys("Ivan")

   input2 = browser.find_element(By.NAME, "last_name")

   input2.send_keys("Petrov")

   input3 = browser.find_element(By.CLASS_NAME, "form-control.city")

   input3.send_keys("Smolensk")

   input4 = browser.find_element(By.ID, "country")

   input4.send_keys("Russia")

   button = browser.find_element(By.CSS_SELECTOR, "button.btn")

   button.click()


finally:


   time.sleep(50)

   # закрываем браузер после всех манипуляций

   browser.quit()