class MobileCartPage:

    def __init__(self, driver):
        self.mobile_driver = driver

    def item(self):

        self.mobile_driver.save_screenshot("mobile_cart.png")

        cart_item = self.mobile_driver.find_element(
            "xpath", "//tr"
        )
