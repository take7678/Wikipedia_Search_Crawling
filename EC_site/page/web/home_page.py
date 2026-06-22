from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.web_driver = driver

    def move_login_page(self):
        login_page = self.web_driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
        login_page.click()
    

    def move_cart_page(self):
        cart_page = self.web_driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
        cart_page.click()


    def add_product(self):
        product1 = self.web_driver.find_element(By.CSS_SELECTOR, "a[data-product-id='1']")
        self.web_driver.execute_script("arguments[0].click();", product1)


        WebDriverWait(self.web_driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cartModal"))
            )
    
        continue_btn = WebDriverWait(self.web_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.close-modal"))
        )
        continue_btn.click()

        product2 = self.web_driver.find_element(By.CSS_SELECTOR, "a[data-product-id='2']")
        self.web_driver.execute_script("arguments[0].click();", product2)


        WebDriverWait(self.web_driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cartModal"))
        )

        view_cart = WebDriverWait(self.web_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/view_cart']"))
        )
        self.web_driver.execute_script("arguments[0].click();", view_cart)
