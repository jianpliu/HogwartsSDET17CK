
import yaml

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from ui_framework.page.basepage import BasePage
from ui_framework.page.market import Market


class MainPage(BasePage):
    def goto_market(self):
        # self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(By.XPATH,"//*[@text='ÐÐÇé']")

        # with open ("../page/main_page.yaml","r") as f:
        #     function = yaml.safe_load(f)
        # print(function)
        # steps = function.get("goto_market")
        # for step in steps:
        #     if step.get("action") == "find_and_click":
        #         self.find_and_click(step.get('locator'),step.get('value'))
        self.parce("../page/main_page.yaml", "goto_market")




        return Market(self.driver)
