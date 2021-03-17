
import yaml

from selenium.webdriver.common.by import By

from ui_framework.page.basepage import BasePage
from ui_framework.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']")
        # with open ("../page/market.yaml","r") as f:
        #     function = yaml.load(f)
        # print(function)
        # steps = function.get("goto_search")
        # for step in steps:
        #     if step.get("action") == "find_and_click":
        #         self.find_and_click(step.get('locator'),step.get('value'))
        self.parce("../page/market.yaml", "goto_search")

        return Search(self.driver)