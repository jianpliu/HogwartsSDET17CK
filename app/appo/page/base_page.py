import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

# 基类，初始化driver,find,finds,swipe_find,
from logs.logger import Logger


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    def find(self,locator,value):
        logging.info("find")
        logging.info(f"{locator},{value}")
        Logger("我的测试").getLogger().info("find")
        Logger("我的测试").getLogger().info(f"{locator},{value}")

        return self.driver.find_element(locator,value)

    def finds(self,locator,value):
        logging.info("finds")
        logging.info(f"{locator},{value}")
        Logger("我的测试").getLogger().info("%s这是一条提示信息" % ("finds"))
        Logger("我的测试").getLogger().info("%s这是一条提示信息" % (f"{locator},{value}"))

        return self.driver.find_elements(locator,value)

    def find_and_click(self,locator,value):
        logging.info("find and click")
        logging.info(f"{locator},{value}")
        Logger("我的测试").getLogger().info("%s这是一条提示信息" % ("find and click"))
        Logger("我的测试").getLogger().info("%s这是一条提示信息" % (f"{locator},{value}"))

        self.driver.find_element(locator,value).click()

    def swipe_find(self, text, num=5):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次，未找到")
            logging.info("set implicitly_wait:2")
            self.driver.implicitly_wait(2)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)




