from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome()
driver.get("https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8")

keyword = input("検索したいワードを教えてね：")

def serch_icon(driver, keyword):
    musi_icon = driver.find_element(By.CLASS_NAME,"search-toggle")
    musi_icon.click()

    time.sleep(1)

    serch_box = driver.find_element(By.CLASS_NAME,"cdx-text-input__input")
    serch_box.send_keys(f"{keyword}")
    serch_box.send_keys(Keys.ENTER)

def get_p(driver):
    ps = driver.find_elements(By.XPATH,"//section[contains(@data-mw-section-id,'0')]//p")
    for n in ps:
        print(n.text)


serch_icon(driver, keyword)
time.sleep(2)
get_p(driver)
