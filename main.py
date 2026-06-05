from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

word = input("キーワードを入力してください:")

driver = webdriver.Chrome()

driver.get("https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8")

time.sleep(2)

musimegane = driver.find_element(By.CLASS_NAME, "search-toggle")
musimegane.click()

time.sleep(2)

serch = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")

serch.send_keys(word)
serch.send_keys(Keys.ENTER)

time.sleep(2)

title = driver.find_element(By.CLASS_NAME, "mw-page-title-main")
print(title.text)

naiyou = driver.find_element(By.ID, "mw-content-text")

ps = naiyou.find_elements(By.TAG_NAME, "p")

results = []

for n in ps:
    if len(n.text) > 20:
        results.append([title.text, n.text])


with open("result.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["タイトル", "内容"])
    writer.writerows(results)
