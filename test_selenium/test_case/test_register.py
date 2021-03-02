from time import sleep

from test_selenium.login_page.main_page import MainPage


class TestAddress:
    def test_register(self):
        main=MainPage()
        main.goto_register().register()
        sleep(6)

    def test_login_register(self):
        main=MainPage()
        main.goto_login().goto_register().register()
        sleep(6)