
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



