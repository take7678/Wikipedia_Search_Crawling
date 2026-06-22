class MobileChromePage:

    def __init__(self, driver):
        self.mobile_driver = driver

    def open_site(self, url):
        self.mobile_driver.get(url)