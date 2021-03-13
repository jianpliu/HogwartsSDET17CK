# -*-coding:GBK -*-
# import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

# 基类，初始化driver,find,finds,swipe_find,
# from logs.logger import Logger
from selenium.webdriver.common.by import By


class BasePage:
    # logging.basicConfig(level=logging.INFO)

    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    # def find(self,locator,value):
    #     black_list=['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
    #     try:
    #         return self.driver.find_element(locator,value)
    #     except Exception:
    #         for ele_xpath in black_list:
    #             eles=self.finds(By.XPATH,ele_xpath)
    #             if len(eles)>0:
    #                 eles[0].click()
    #                 return self.find(locator,value)

    def find1(fun):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        def run(*args,**kwargs):
            self = args[0]
            try:
                return fun(*args, **kwargs)
            except Exception:
                for ele_xpath in black_list:
                    eles=self.finds(By.XPATH,ele_xpath)
                    if len(eles)>0:
                        eles[0].click()
                        return fun(*args,**kwargs)
        return run


    @find1
    def find(self, locator, value):
        return self.driver.find_element(locator, value)










    def finds(self,locator,value):
        return self.driver.find_elements(locator,value)

    def find_and_click(self,locator,value):
        # self.driver.find_element(locator,value).click()
        self.find(locator,value).click()

    def find_and_send(self,locator,value,content):
        self.find(locator,value).send_keys(content)

    def swipe_find(self, text, num=5):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次，未找到")

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

