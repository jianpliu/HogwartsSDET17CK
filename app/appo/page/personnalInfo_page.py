
#!/usr/bin/env python
# -*- coding:utf-8 -*-


from appium.webdriver.common.mobileby import MobileBy

from app.appo.page.base_page import BasePage
from app.appo.page.editinfo_page import EditInfoPage


class PersonnalInfoPage(BasePage):
    def click_dot(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/iga").click()
        return EditInfoPage(self.driver)
