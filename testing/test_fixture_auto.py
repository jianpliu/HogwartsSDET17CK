import pytest




@pytest.fixture(autouse = True )
def login():
    print("登录操作")

@pytest.fixture(autouse = True )
def get_username():
    name="郝敏"
    print(name)
    return name


def test_search():
    print("搜索")

def test_cart():
    print("购物")
