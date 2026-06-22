import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

class MobileHomePage:

    def __init__(self, driver):
        self.mobile_driver = driver

    def switch_to_webview(self):
        for i in range(10):
            contexts = self.mobile_driver.contexts

            for context in contexts:
                if "CHROMIUM" in context:
                    self.mobile_driver.switch_to.context(context)
                    return

            time.sleep(1)

        raise Exception("WEBVIEWが見つからない")

    def mobile_move_login_page(self):

        self.mobile_driver.execute_script("window.scrollBy(0, 300);")

        wait = WebDriverWait(self.mobile_driver, 10)

        login_btn = wait.until(
            E.presence_of_element_located(
                ("xpath", "//a[contains(text(),'Signup / Login')]")
            )
        )
        self.mobile_driver.execute_script("arguments[0].click();", login_btn)

    def mobile_move_cart_page(self):

        wait = WebDriverWait(self.mobile_driver, 10)

        cart_btn = wait.until(
            E.presence_of_element_located(
                ("xpath", "//a[contains(text(),'Cart')]")
            )
        )
        cart_btn.click()