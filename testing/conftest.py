#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from typing import List

import pytest
# from pythoncode.Calculator import Calculator
#conftest.py 文件名字是固定的，不能改
@pytest.fixture(scope = "session")
def login():
    print("登录操作")
    token=datetime.datetime.now()
    yield token #yield相当于return
    print("登出操作")
    # return token

# @pytest.fixture(scope = "session")#session :工程级    module：模块级      class:类级    默认是方法级
# # def get_instance():
# #     print("开始计算")
# #     calc=Calculator()
# #     yield calc
# #     print("结束计算")


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)  #加标签add
    items.reverse()
