from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestAddress():
    def test_address(self):
        #声明chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        #加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        #点击通讯录
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        #不可交互
        #1.元素被遮挡，元素前面还有其他不可见元素
        #2.元素有多个，需要人工挑选其中合适的元素
        def wait_name(driver):
            eles=driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn ww_btn_WithIcon js_invite']")
            if len(eles)>0:
                return True
            else:
                return False
        WebDriverWait(self.driver,10).until(wait_name)



        self.driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
        #输入姓名
        self.driver.find_element(By.XPATH,"//*[@id='username']").send_keys("今天是星期日123")
        #输入账号
        self.driver.find_element(By.XPATH,"//*[@id='memberAdd_acctid']").send_keys("happer012333")
        #输入手机号
        self.driver.find_element(By.XPATH,"//*[@id='memberAdd_phone']").send_keys("18810901980")
        #点击保存
        self.driver.find_element(By.XPATH,"//*[@class='qui_btn ww_btn js_btn_save']").click()


