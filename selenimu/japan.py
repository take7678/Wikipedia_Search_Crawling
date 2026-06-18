from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome()
driver.get("https://ja.wikipedia.org/wiki/都道府県")



with open("ジャパン.txt", "r", encoding="utf-8") as f:
    japan = []
    for line in f:
        japan.append(line.strip())


with open("japan.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["都道府県", "説明"])


for n in japan:
    try:
        link = driver.find_element(By.XPATH, f"//a[text()='{n}']")

        driver.execute_script("arguments[0].scrollIntoView();", link)
        driver.execute_script("arguments[0].click();", link)

        time.sleep(2)

        p = driver.find_element(
            By.XPATH,"//table[contains(@class,'infobox')]/following-sibling::p[1]"
        )

        text = p.text

        with open("japan.csv", "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([n, text])

        driver.back()
        time.sleep(2)

    except Exception as e:
        print(f"{n} でエラー発生: {e}")

driver.quit()
