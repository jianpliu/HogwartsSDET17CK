import pytest

@pytest.fixture()
def login():
    print("登录操作")

@pytest.fixture()
def get_username():
    name="郝敏"
    print(name)
    return name


def test_search():
    print("搜索")



#第二种使用fixture的方法
@pytest.mark.usefixtures("login")
def test_cart():
    print("购物")


#第一种使用fixture的方法
# def test_order(login):
#     print("下单")


#使用2个fixture的写法1：由下向上调用
# def test_order(login,get_username):
#     print("下单")


@pytest.mark.usefixtures("get_username")
@pytest.mark.usefixtures("login")
def test_order():
    print("下单")