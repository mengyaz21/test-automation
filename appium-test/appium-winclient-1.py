# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

#结合自己的client当前的Appium-Python-Client的版本
#https://github.com/appium/python-client

options = AppiumOptions()
options.load_capabilities({
    "platformName": "windows",
    "appium:automationName": "Windows",
    "appium:app": "Root",
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://10.103.209.250:4723", options=options)

driver.quit()
