
import yaml

from selenium.webdriver.common.by import By

from ui_framework.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        # self.find_and_send(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']","alibaba")

        # with open ("../page/search.yaml","r") as f:
        #     function = yaml.load(f)
        # print(function)
        # steps = function.get("search")
        # for step in steps:
        #     if step.get("action") == "find_and_click":
        #         self.find_and_click(step.get('locator'),step.get('value'))
        #     elif step.get("action") == "find_and_send":
        #         self.find_and_send(step.get('locator'), step.get('value'),step.get('content'))
        self.parce("../page/search.yaml", "search")

