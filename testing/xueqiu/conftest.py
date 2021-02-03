import pytest
import datetime

@pytest.fixture(scope="session")
def login():
    print("登录操作>>>>>>>>")
    name="哈利波特"
    yield name
    print("登出操作")