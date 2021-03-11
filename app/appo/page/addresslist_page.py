from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from app.appo.page.addcontact_page import AddContactPage
from app.appo.page.base_page import BasePage
from app.appo.page.searchname_page  import SearchPage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    # def swipe_find(self,text,num=3):
    #     for i in range(num):
    #         if i==num-1:
    #             self.driver.implicitly_wait(5)
    #             raise NoSuchElementException(f"找到{num}次，未找到")
    #         self.driver.implicitly_wait(2)
    #         try:
    #             element = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{text}']")
    #             self.driver.implicitly_wait(5)
    #             return element
    #         except:
    #             print("未找到")
    #             size = self.driver.get_window_size()
    #             width = size.get('width')
    #             height = size.get('height')
    #
    #             start_x = width/2
    #             start_y = height*0.8
    #
    #             end_x = start_x
    #             end_y = height*0.3
    #
    #             self.driver.swipe(start_x,start_y,end_x,end_y,1000)

    def click_addcontact(self):
        element = self.swipe_find("添加成员").click()
        return AddContactPage(self.driver)

    def click_search(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/igk").click()
        return SearchPage(self.driver)