import logging

import yaml
import logging

from logs.logger import Logger

root_log = logging.getLogger()
logging.basicConfig(level=logging.INFO)
# logging.info("aaaa")
def test_yaml():

    with open("./appo/datas/caps.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        desires = datas['desired_caps']
        ip = datas['server']['ip']
        port = datas['server']['port']
        # print(datas)


    pythonobj = {'desired_caps': {'platformName': 'android', 'platformVersion': '6.0', 'deviceName': '127.0.0.1:7555', 'appPackage': 'com.tencent.wework', 'appActivity': '.launch.LaunchSplashActivity', 'noReset': 'True', 'skipServerInstallation': 'true', 'skipDeviceInitialization': 'true'}, 'server': {'ip': '127.0.0.1', 'port': 4723}}
    # print(yaml.safe_dump(pythonobj))
    # logging.info(yaml.safe_dump(pythonobj))
    Logger("我的测试").getLogger().info("%s这是一条提示信息" % (yaml.safe_dump(pythonobj)))


