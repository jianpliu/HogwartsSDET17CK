# -*-coding:GBK -*-

from appium.webdriver.common.mobileby import MobileBy

from app.appo.page.base_page import BasePage
from app.appo.page.deleinfo_page import DeleInfoPage


class EditInfoPage(BasePage):
    def edit_Info(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return DeleInfoPage(self.driver)

