# conftest.py 用法
# 数据共享的文件，名字是固定的，不能修改
# 可以存放fixture , hook 函数
# 就近生效（如果不在同一个文件夹下，离测试文件最近的conftest.py 生效）
# 当前目录一定要有__init__.py 文件，也就是要创建一个包
import datetime
from typing import List
import pytest,sys,yaml
from pytest_encode import logger

sys.path.append('..')
from pythoncode.Calculator import Calculator
# conftest.py 文件名字是固定的，不能改

@pytest.fixture(scope = "session")
def login():
    print("登录操作")
    token=datetime.datetime.now()
    yield token #yield相当于return
    print("登出操作")
    return token

@pytest.fixture(scope = "session")#session :工程级    module：模块级      class:类级    默认是方法级
def get_instance():
    print("开始计算")
    calc=Calculator()
    yield calc
    print("结束计算")


def get_datas(name, type='int'):
    with open("./datas/calc.yml", encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']

    return (datas, ids)


@pytest.fixture(params=get_datas("add","int")[0],ids=get_datas("add","int")[1])
def get_date_with_fixture(request):
    return request.param

@pytest.fixture(params=get_datas("add","decimal")[0],ids=get_datas("add","decimal")[1])
def get_date_with_fixture_for_add_decimal(request):
    return request.param

@pytest.fixture(params=get_datas("div","int_normal")[0],ids=get_datas("div","int_normal")[1])
def get_date_with_fixture_for_div_int(request):
    return request.param

@pytest.fixture(params=get_datas("div","int_error")[0],ids=get_datas("div","int_error")[1])
def get_date_with_fixture_for_div_zero(request):
    return request.param

@pytest.fixture(params=get_datas("div", "int_normal_and_error")[0],ids=get_datas("div", "int_normal_and_error")[1])
def get_date_with_fixture_for_div_combination(request):
    return request.param


# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     print(items)
#     for item in items:
#         item.name=item.name.encode('utf-8').decode('unicode_escape')
#         item._nodeid=item.nodeid.encode('utf-8').decode('unicode_escape')
#         logger.info(f"item.name:{item.name}")
#         logger.info(f"item._nodeid:{item._nodeid}")
#         if 'add' in item._nodeid:
#             item.add_marker(pytest.mark.add)  #加标签add
#     items.reverse()


# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     print(items)
# # #     for item in items:
# # #         item.name=item.name.encode('utf-8').decode('unicode_escape')
# # #         item._nodeid=item.nodeid.encode('utf-8').decode('unicode_escape')
# # #         logger.info(f"item.name:{item.name}")
# # #         logger.info(f"item._nodeid:{item._nodeid}")
