from selenium import webdriver

def get_web_driver():    
    web_driver = webdriver.Chrome()
    return web_driver