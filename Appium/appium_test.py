from appium import webdriver
from appium.options.android import UiAutomator2Options


options = UiAutomator2Options()

options.set_capability("platformName", "Android")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("deviceName", "Android Emulator")

options.set_capability("appPackage", "com.android.settings")
options.set_capability("appActivity", ".Settings")

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
