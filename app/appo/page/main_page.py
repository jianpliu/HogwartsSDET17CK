from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.appo.page.addresslist_page import AddressListPage
from app.appo.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self,driver:WebDriver):#: 来指定类型的
    #     self.driver = driver
    addressList_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_addressList(self):
        #点击通讯录
        self.find(*self.addressList_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
