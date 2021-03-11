# -*-coding:GBK -*-


from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.appo.page.base_page import BasePage
from app.appo.page.personnalInfo_page import PersonnalInfoPage


class SearchPage(BasePage):
    def counter(self,name):
        elelist = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        return elelist

    def input_search(self,name):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((MobileBy.XPATH, "//*[@text='联系人']")))
        # elelist = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        num_nodele = len(self.counter(name))
        if num_nodele > 1:
            self.counter(name)[1].click()

        else:
            print("用户不存在")
        return  (PersonnalInfoPage(self.driver),num_nodele)
    #

    def dele_ok(self,name):
        after_dele = len(self.counter(name))
        return after_dele




