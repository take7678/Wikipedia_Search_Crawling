from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

options = UiAutomator2Options()

options.set_capability("platformName", "Android")
options.set_capability("deviceName", "Android Emulator")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("appPackage", "com.android.settings")
options.set_capability("appActivity", "com.android.settings.Settings")

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options = options

)

serch_box = driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@resource-id='com.android.settings:id/search_action_bar']")
serch_box.click()

wait = WebDriverWait(driver, 10)

serch_input = wait.until(
    E.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
)

serch_input.send_keys("機内モード")

airswitch = wait.until(
    E.presence_of_element_located(
        (AppiumBy.ID, "android:id/switch_widget")
    )
)

if airswitch.get_attribute("checked") == "false":
    airswitch.click()
    print("off→Onに変更")
else:
    print("すでにOn")