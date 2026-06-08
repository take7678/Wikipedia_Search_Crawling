from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Chrome()
driver.get("https://ja.wikipedia.org/wiki/%E9%83%BD%E9%81%93%E5%BA%9C%E7%9C%8C")

with open("ジャパン.txt", "r", encoding= "utf-8") as f:
        japan = [line.strip() for line in f]

for n in japan:
    link = driver.find_element(By.XPATH, f"//a[text() = '{n}']")
    link.click()
    
    time.sleep(2)

    p = driver.find_element(By.XPATH, "//table[contains(@class,'infobox')]/following-sibling::p[1]")
    print(p.text)
    driver.back()
    time.sleep(2)

