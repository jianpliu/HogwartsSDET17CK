import logging
import os
import time
class Logger():
    def __init__(self,logger_name):
        self.logger=logging.getLogger(logger_name)
        self.logger.setLevel("DEBUG")
        self.fmt=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        #*********记住写法**************
        # log_path=os.path.dirname(os.path.abspath('.'))+'/RC-配置文件/logs/'
        # log_path = os.path.abspath('..') + '/logs/'
        log_path=r"C:/home/Python/study/HogwartsSDE17CK/logs/"
        # now=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # now=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        now = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        self.log_name=log_name=log_path+now+'.txt'

    def getLogger(self):
        if not self.logger.handlers:
            fh=logging.StreamHandler()
            ch=logging.FileHandler(self.log_name,encoding='utf-8')

            fh.setLevel("INFO")
            ch.setLevel("INFO")

            fh.setFormatter(self.fmt)
            ch.setFormatter(self.fmt)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

        return self.logger


if __name__=='__main__':
    list1=[1,2,4,5]
    for i in range(len(list1)):
        Logger("我的测试").getLogger().info("%s这是一条提示信息"%(list1[i]))


    # Logger("我的测试").getLogger().error("这是一条提示信息")



