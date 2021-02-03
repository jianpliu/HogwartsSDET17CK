import pytest
import datetime



# @pytest.fixture()
# def login():
#     print("登录操作")
#     token=datetime.datetime.now()
#     # yield #相当于return yield后边的东西等test_执行完了之后才会执行
#     # yield token
#     #     # print("登出操作")
#     return token

# @pytest.fixture()
# def get_username(login):
#     name="郝敏"
#     print(name)
#     return name


def test_search(login):
    print(login)
    print("搜索")

def test_cart(login):
    print(login)
    print("购物")

# @pytest.mark.usefixtures('login')
# def test_order():
#     print(login) #如果使用装饰器，无法获取fixture返回的值
#     print("下单")


def test_order(login):
    print(login) #如果使用装饰器，无法获取fixture返回的值
    print("下单")