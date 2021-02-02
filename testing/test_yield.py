import pytest
import datetime



@pytest.fixture()
def login():
    print("登录操作")
    token=datetime.datetime.now()
    # yield #相当于return yield后边的东西等test_执行完了之后才会执行
    yield token
    print("登出操作")

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