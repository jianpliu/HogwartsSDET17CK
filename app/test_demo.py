import time

from appium import webdriver
class TestDemo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = True  # Don't reset app state before this session.
        # desired_caps['dontStopAppOnReset'] = True  # 系统在哪个页面就继续在哪个页面操作，不重新打开了，需要和driver.back结合使用
        # desired_caps['skipDeviceInitializaion'] = True  # 案例多的时候可以明显的缩小运行时间
        # desired_caps['unicodeKeyBoard'] = True
        # desired_caps['resetKeyBoard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    #
    def test_demo(self):

        el2 = self.driver.find_element_by_id("com.tencent.wework:id/igk")
        el2.click()
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/gy9")
        el3.send_keys("test")
        # el3.click()
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView[1]")
        el4.click()
        time.sleep(6)

