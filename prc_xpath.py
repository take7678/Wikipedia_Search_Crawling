from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome()
driver.get("https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8")

#
user_input = input("調べたいキーワードを教えてください(A　Bのように複数でも良いよ)")
keyword = [n.strip() for n in user_input.split("　")]

for n in keyword:

    musi_icon = driver.find_element(By. CLASS_NAME, "search-toggle")
    musi_icon.click()

    time.sleep(2)

    serch_box = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
    serch_box.send_keys(f"{n}")

    time.sleep(2)

    serch_box.send_keys(Keys.ENTER)

    time.sleep(2)

    try:
        ps = driver.find_elements(By.XPATH,"//section[@data-mw-section-id='1']//p")
        if not ps:
            raise Exception()
    except:
        ps = driver.find_elements(By.XPATH, "//p")


    for m in ps: 
        with open("prc_xpath.txt", "a", encoding="utf-8-sig") as f:
            f.write(m.text + "\n" + "\n")

    