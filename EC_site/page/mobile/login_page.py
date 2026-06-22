from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

class MobileLoginPage:

    def __init__(self, driver):
        self.mobile_driver = driver

    def login(self, email, password):

        wait = WebDriverWait(self.mobile_driver, 10)

        email_box = wait.until(
            E.presence_of_element_located(
                ("xpath", "//input[@data-qa='login-email']")
            )
        )
        email_box.send_keys(email)

        password_box = self.mobile_driver.find_element(
            "xpath", "//input[@data-qa='login-password']"
        )
        password_box.send_keys(password)

        login_btn = self.mobile_driver.find_element(
            "xpath", "//button[@data-qa='login-button']"
        )
        login_btn.click()