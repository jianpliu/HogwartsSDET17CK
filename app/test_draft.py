import logging


class T:
    a=1
    def ss(self):
        self.name=self.a
        return self

    def dd(self):
        print(self.name)
T().ss().dd()

logging.basicConfig(level=logging.INFO)
# log = logging.getLogger(__name__)
class TestA:
    root_log = logging.getLogger()
    logging.basicConfig(level=logging.INFO)
    def test_a(self):


        # root_log = logging.getLogger()

        logging.info("aaaaa")

