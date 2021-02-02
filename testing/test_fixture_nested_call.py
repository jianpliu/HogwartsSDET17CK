import pytest




@pytest.fixture()
def login():
    print("登录操作")

@pytest.fixture()
def get_username(login):
    name="郝敏"
    print(name)
    return name


def test_search(get_username):
    print("搜索")

def test_cart():
    print("购物")