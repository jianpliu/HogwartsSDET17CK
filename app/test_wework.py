import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = True  # Don't reset app state before this session.
        desired_caps['settings[waitForIdleTimeout]'] = 1
        # desired_caps['dontStopAppOnReset'] = True  # 系统在哪个页面就继续在哪个页面操作，不重新打开了，需要和driver.back结合使用
        # desired_caps['skipDeviceInitializaion'] = True  # 案例多的时候可以明显的缩小运行时间
        # desired_caps['unicodeKeyBoard'] = True
        # desired_caps['resetKeyBoard'] = True
        #客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    #
    def test_demo(self):
        self.driver.find_element(By.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        self.driver.find_element(By.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(By.XPATH, "//*[contains(@text,'次外出')]").click()
        # time.sleep(4)
        # assert "外出打卡成功" in self.driver.page_source
        #激活隐式等待
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡成功']")






