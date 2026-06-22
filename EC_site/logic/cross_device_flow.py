from driver.selenium_driver import get_web_driver
from driver.appium_driver import get_mobile_driver

from page.web.login_page import LoginPage
from page.web.home_page import HomePage
from page.web.cart_page import CartPage

from page.mobile.chrome_page import MobileChromePage
from page.mobile.home_page import MobileHomePage
from page.mobile.login_page import MobileLoginPage
from page.mobile.cart_page import MobileCartPage


web_driver = get_web_driver()
web_driver.get("https://automationexercise.com/")

home_page = HomePage(web_driver)
home_page.move_login_page()

login_page = LoginPage(web_driver)
login_page.login("test@co.jp", "test123")

home_page = HomePage(web_driver)
home_page.add_product()
home_page.move_cart_page()

cart_page = CartPage(web_driver)
cart_page.screenshot()
cart_page.save_csv()


mobile_driver = get_mobile_driver()

chrome_page = MobileChromePage(mobile_driver)
chrome_page.open_site("https://automationexercise.com/")

mobile_home = MobileHomePage(mobile_driver)
mobile_home.switch_to_webview()

mobile_home.mobile_move_login_page()

mobile_login = MobileLoginPage(mobile_driver)
mobile_login.login("test@co.jp", "test123")

mobile_home.mobile_move_cart_page()

mobile_cart = MobileCartPage(mobile_driver)
mobile_cart.item()