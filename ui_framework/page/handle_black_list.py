import allure
from selenium.webdriver.common.by import By

from ui_framework.page.logger import log


def handle_black(fun):
    def run(*args,**kwargs):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        #Ïàµ±ÓÚself
        instance = args[0]
        try:
            log.debug("find" + args[2])
            return fun(*args, **kwargs)
        except Exception:
            allure.attach(instance.screenshot(),attachment_type=allure.attachment_type.PNG)
            for ele_xpath in black_list:
                eles=instance.finds(By.XPATH,ele_xpath)
                if len(eles)>0:
                    eles[0].click()
                    return fun(*args,**kwargs)
    return run
