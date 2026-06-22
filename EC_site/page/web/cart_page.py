import csv
import os

class CartPage:
    def __init__(self, driver):
        self.web_driver = driver

    def screenshot(self):

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        self.web_driver.save_screenshot("screenshots/cart.png")
