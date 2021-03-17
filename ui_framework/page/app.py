# from appium.webdriver import webdriver
import yaml

from appium import webdriver



from ui_framework.page.basepage import BasePage
from ui_framework.page.main_page import MainPage

with open("../datas/caps.yml",encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    desires = datas['desired_caps']
    ip = datas['server']['ip']
    port = datas['server']['port']

class App(BasePage):
    def start(self):
        if self.driver == None:
            #启动app
            #   desired_caps = {}
            #   desired_caps['platformName'] = 'android'
            #   desired_caps['platformVersion'] = '6.0'
            #   desired_caps['deviceName'] = '127.0.0.1:7555'
            #   desired_caps['appPackage'] = 'com.tencent.wework'
            #   desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            #   desired_caps['noReset'] = "true"  # Don't reset app state before this session.不清除缓存
            # desired_caps['settings[waitForIdleTimeout]'] = 1  # 动态页面的等待时间
            # 跳过安装uiautomator2server等服务
            #   desired_caps['skipServerInstallation'] = "true"
            # 跳过设备的初始化
            #   desired_caps['skipDeviceInitialization'] = "true"
            # 运行前不停止app
            # desired_caps['dontStopAppOnReset'] = True  # 系统在哪个页面就继续在哪个页面操作，不重新打开了，需要和driver.back结合使用
            # desired_caps['skipDeviceInitializaion'] = True  # 案例多的时候可以明显的缩小运行时间
            # desired_caps['unicodeKeyBoard'] = True
            # desired_caps['resetKeyBoard'] = True
            # 客户端与appium服务器建立连接的代码
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', desires)
            self.driver.implicitly_wait(20)
            print("test!!!!!!!!!!!!!!!!")
        else:
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
            self.driver.launch_app()#这两行效果一样，写法不一样
        return self

    def restart(self):
        #重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        #停止app
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)