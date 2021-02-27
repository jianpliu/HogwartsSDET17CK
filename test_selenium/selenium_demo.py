import json
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmp():
    def setup_method(self,method):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_arg)
        # self.vars={}
        self.driver=webdriver.Chrome()


    # def teardown_method(self,method):
    #     self.driver.quit()

    def test_tmp(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH,"//*[@class='index_top_operation_loginBtn']").click()
        self.driver.find_element(By.XPATH,"//*[@class='login_registerBar_link']").click()
        sleep(4)
        self.driver.find_element(By.XPATH,"//*[@id='corp_name']").send_keys("xxx")

    def test_tmp2(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("qq邮箱")
        self.driver.find_element_by_id("su").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//*[@id='8']/h3/a").click()


    def test_login_tmp(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()



    def test_get_cookie(self):
        cookies=self.driver.get_cookies()
        print(cookies)
        with open("tmp.txt","w",encoding="utf-8") as f:
            # f.write(json.dumps(cookies))
            json.dump(cookies,f) #和f.write(json.dumps(cookies))效果一样

    def test_with_cookie(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#createMessage")
        # cookies=[{'domain': '.qq.com', 'expiry': 1614404184, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850129139677'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '8gHYp-C8goAj-WlTmMklKWKK24umMTLrWmcvbjVhKRzIRBXXJtEbTb74fW2hWvaWyNPB0ogHBiVsSxnRgzrkAUt48xmUCrHvdXW8VFtackpg52DADAIQ4fUBlyeiwH1ao4-S0Ms6d107QnuHD386JclICXchVPbUuiqb6QwPGK2zo2Wuu_ypzGB3PAxoaE7kOTPjKa85uCQ64QNBv4d-xTNcf2Wt91Fzhnest6GyDnZe1QdMXz7UBfyjt7joq163MNswhQ7_3vS3ygAJKxNmNA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850129139677'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325096430599'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7117535'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '1tP8QzAaZXAlCoH4zrBS4Qfmz9egfT-IAUkSOr6AkGFjaVZCHIHl6BIYsw-Omnyi'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645940040, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614403179,1614403536,1614404041'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614404041'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '20829575352040623'}, {'domain': '.qq.com', 'expiry': 1614490524, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1730015563.1614403180'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614434713, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '24v328r'}, {'domain': '.qq.com', 'expiry': 1677476124, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.746754464.1614403180'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645939177, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1616996127, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        with open("tmp.txt","r",encoding='utf-8') as f:
            # raw_cookies = f.read()
            # #序列化
            # cookies=json.loads(raw_cookies)
            cookies=json.load(f)  #和raw_cookies = f.read()   cookies=json.loads(raw_cookies)效果一样
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        # self.driver.find_element(By.XPATH,"//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
