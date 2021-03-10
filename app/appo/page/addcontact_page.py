from appium.webdriver.common.mobileby import MobileBy

from app.appo.page.base_page import BasePage
from app.appo.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def addcontact_menual(self):
        #手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditContactPage(self.driver)
