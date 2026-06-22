from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_mobile_driver():
    options = UiAutomator2Options()

    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "Android Emulator")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("browserName", "Chrome")
    options.set_capability("chromedriver_autodownload", True)
    options.set_capability("chromedriverExecutableDir","C:\\chromedriver")
    mobile_driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    return mobile_driver