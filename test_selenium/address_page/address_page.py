import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    def add_member(self):
        def wait_name(driver):
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'js_mod_party_name')))
            driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
            eles=driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles)>0

        WebDriverWait(self.driver,10).until(wait_name)




        #输入姓名
        self.driver.find_element(By.XPATH,"//*[@id='username']").send_keys("今天是星期日1238")
        #输入账号
        self.driver.find_element(By.XPATH,"//*[@id='memberAdd_acctid']").send_keys("happer0123338")
        #输入手机号
        self.driver.find_element(By.XPATH,"//*[@id='memberAdd_phone']").send_keys("18810901981")
        #点击保存
        self.driver.find_element(By.XPATH,"//*[@class='qui_btn ww_btn js_btn_save']").click()




