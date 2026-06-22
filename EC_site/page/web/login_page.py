from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.web_driver = driver

    def move_login_page(self):
        login_page = self.web_driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
        login_page.click()
    
    def login(self, email, password):

        email_box = WebDriverWait(self.web_driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']"))
        )
        email_box.send_keys(email)

        password_box = WebDriverWait(self.web_driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-password']"))
        )
        password_box.send_keys(password)

        login_btn = self.web_driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
        login_btn.click()

    