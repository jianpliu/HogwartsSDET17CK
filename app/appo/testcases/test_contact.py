# -*-coding:GBK -*-
import time

from appium.webdriver.common.mobileby import MobileBy

from app.appo.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App().start()


    def setup(self):
        self.main =self.app.goto_main()
        pass
    #
    # def teardown_class(self):
    #     self.app.stop()

    def test_addcontact(self):
        name = 'Hogwarts_1152'
        phonenum = "12345671152"
        editpage = self.main.goto_addressList().click_addcontact().addcontact_menual()
        editpage.edit_contact(name,phonenum)
        editpage.verify_ok()

    def test_delecontact(self):
        name = 'aaa2'
        search_info = self.main.goto_addressList().click_search().input_search(name)
        if search_info[1]>1:

            dele_result = search_info[0].click_dot().edit_Info().dele_Info()
            time.sleep(5)
            now_count = dele_result.dele_ok(name)
            assert now_count == search_info[1] - 1
        else:
            print("用户不存在")



