
# -*-coding:GBK -*-
from appium.webdriver.common.mobileby import MobileBy

from app.appo.page.base_page import BasePage





class DeleInfoPage(BasePage):
    def dele_Info(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='ɾ����Ա']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='ȷ��']").click()
        from app.appo.page.searchname_page import SearchPage
        return SearchPage(self.driver)


