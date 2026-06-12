from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

options = UiAutomator2Options()

options.set_capability("platformName", "Android")
options.set_capability("deviceName", "Android Emulator")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("appPackage", "com.google.android.apps.maps")
options.set_capability("appActivity", "com.google.android.maps.MapsActivity")

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

wait = WebDriverWait(driver, 10)

#GoogleMap開くと出てくるログイン画面
try:
    skip = wait.until(
        E.presence_of_element_located(
            (AppiumBy.XPATH, '//*[@text="スキップ"]')
        )
    )
    skip.click()
except:
    pass

#検索BOX
serch_box = wait.until(
    E.presence_of_element_located(
        (AppiumBy.XPATH, '//*[@text="ここで検索"]')
    )
)
serch_box.click()

#検索テキストBOX
keyword_box = wait.until(
    E.presence_of_element_located(
        (AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_edit_text")
    )
)

#検索キーワード
keyword_box.send_keys("横浜駅")

#キーワード候補選択
keyword_content = wait.until(
    E.presence_of_element_located(
        (AppiumBy.ID, "com.google.android.apps.maps:id/compass_container")
    )
)
keyword_content.click()

#経路選択
route = wait.until(
    E.presence_of_element_located(
    (AppiumBy.XPATH, "//android.view.View[@content-desc='経路']")
    )
)
route.click()

#初回検索の場合位置情報選択設定
try:
    first_tab = wait.until(
        E.presence_of_element_located(
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        )
    )
    first_tab.click()
except:
    pass

#現在地BOX確認
current_location_box = wait.until(
    E.presence_of_element_located(
        (AppiumBy.ID ,"com.google.android.apps.maps:id/custom_header_container")
    )
)
current_location_box.click()

#現在地キーワード
current_location = wait.until(
    E.presence_of_element_located(
        (AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_edit_text")
    )
)
current_location.send_keys("東京駅")

#検索候補選択
current_location_content = wait.until(
    E.presence_of_element_located(
        (AppiumBy.ID, "com.google.android.apps.maps:id/compass_container")
    )
)
current_location_content.click()

#ガイドスタートボタン
guide = wait.until(
    E.presence_of_element_located(
        (AppiumBy.XPATH, "//android.view.View[@content-desc='ガイド']")
    )
)
guide.click()