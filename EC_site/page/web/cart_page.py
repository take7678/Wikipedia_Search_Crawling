import csv
import os

class CartPage:
    def __init__(self, driver):
        self.web_driver = driver

    def screenshot(self):

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        self.web_driver.save_screenshot("screenshots/cart.png")

    def save_csv(self):

        file_exists = os.path.isfile("result.csv")

        with open("result.csv", "a", newline="") as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(["Test Name", "Result", "Screenshot"])

                writer.writerow(["Add Cart Test", "PASS", "screenshots/cart.png"])
