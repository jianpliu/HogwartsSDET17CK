import time
import yaml

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TestDemo:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = True  # Don't reset app state before this session.不清除缓存
        desired_caps['settings[waitForIdleTimeout]'] = 1 #动态页面的等待时间
        # 跳过安装uiautomator2server等服务
        desired_caps['skipServerInstallation'] = "true"
        #跳过设备的初始化
        desired_caps['skipDeviceInitialization'] = "true"
        #运行前不停止app
        desired_caps['dontStopAppOnReset'] = True  # 系统在哪个页面就继续在哪个页面操作，不重新打开了，需要和driver.back结合使用
        # desired_caps['skipDeviceInitializaion'] = True  # 案例多的时候可以明显的缩小运行时间
        # desired_caps['unicodeKeyBoard'] = True
        # desired_caps['resetKeyBoard'] = True
        #客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(8)



    # def teardown(self):
    #     self.driver.quit()

    def swipe_find(self,text,num=3):
        for i in range(num):
            if i==num-1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次，未找到")
            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')

                start_x = width/2
                start_y = height*0.8

                end_x = start_x
                end_y = height*0.3

                self.driver.swipe(start_x,start_y,end_x,end_y,1000)









    def test_addcontact(self):
        name="hogwarts_4"
        phonenum="1300000000004"
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()

        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find("添加成员").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # name=self.driver.find_elements(By.XPATH,"//android.widget.ScrollView//android.widget.EditText")[0]
        # name = self.driver.find_element(By.XPATH, "//*[@text='姓名　']/../*[@text='必填']")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # tele=self.driver.find_elements(By.XPATH,"//android.widget.ScrollView//android.widget.EditText")[1]
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 验证添加成员 toast
        #assert '添加成员' in self.driver.page_source
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']")

    def test_delcontact(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/igk").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys("Hogwarts_11")
        elelist = self.driver.find_elements(MobileBy.XPATH, "//*[@text='Hogwarts_11']")
        #find_elements 方法返回的是一个列表[element1,element2,......]
        if len(elelist)>1:
            elelist[1].click()






