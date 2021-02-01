import pytest

@pytest.fixture()
def login():
    print("登录操作")


def test_search():
    print("搜索")

def test_cart(login):
    print("购物")

def test_order(login):
    print("下单")