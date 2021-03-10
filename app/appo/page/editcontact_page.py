from appium.webdriver.common.mobileby import MobileBy

from app.appo.page.base_page import BasePage


class EditContactPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def edit_contact(self,name,phonenum):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # tele=self.driver.find_elements(By.XPATH,"//android.widget.ScrollView//android.widget.EditText")[1]
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

    def verify_ok(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")