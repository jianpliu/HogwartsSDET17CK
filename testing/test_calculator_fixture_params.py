#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure
import pytest
import sys,yaml,os
sys.path.append('..')

print(sys.path)

from pythoncode.Calculator import Calculator

def get_datas(name,type='int'):
    with open("./datas/calc.yml") as f:
        all_datas=yaml.safe_load(f)
    datas=all_datas[name][type]['datas']
    ids=all_datas[name][type]['ids']


    return (datas,ids)



#———————————————也可以把这个写在conftest里边————————————————
@pytest.fixture()#session :工程级    module：模块级      class:类级    function 默认是方法级
def get_instance():
    print("开始计算")
    calc=Calculator()
    yield calc
    print("结束计算")

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




#测试类
class TestCalc():
    # add_int_data = get_datas('add','int')
    # add_decimal_data = get_datas('add','decimal')
    # div_int_data = get_datas('div','int_normal')
    # div_zero_data= get_datas('div','int_error')
    # div_combination = get_datas('div','int_normal_and_error')




    # #前置条件
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc=Calculator()
    #
    # # 后置条件
    # def teardown_class(self):
    #     print("结束计算")


    @pytest.mark.login #和pytest.ini结合使用
    # @pytest.mark.parametrize("a,b,result",add_int_data[0],ids=add_int_data[1])
    def test_add(self,get_instance,get_date_with_fixture):
        f=get_date_with_fixture
        print(f"a={f[0]},b={f[1]},result={f[2]}")
        assert f[2] == get_instance.add(f[0],f[1])

    @pytest.mark.search
    # @pytest.mark.parametrize("a,b,result",add_decimal_data[0],ids=add_decimal_data[1])
    def test_add_decimal(self,get_instance,get_date_with_fixture_for_add_decimal):
        f=get_date_with_fixture_for_add_decimal
        print(f"a={f[0]},b={f[1]},result={f[2]}")
        assert round(f[2],2)==round(get_instance.add(f[0],f[1]),2)


    # @pytest.mark.parametrize("a,b,result", div_int_data[0], ids=div_int_data[1])
    def test_div(self,get_instance, get_date_with_fixture_for_div_int):
        f=get_date_with_fixture_for_div_int
        print(f"a={f[0]},b={f[1]},result={f[2]}")
        assert f[2] == get_instance.div(f[0], f[1])


    # @pytest.mark.parametrize("a,b,result", div_zero_data[0], ids=div_zero_data[1])
    def test_div_zero(self,get_instance, get_date_with_fixture_for_div_zero):
        f = get_date_with_fixture_for_div_zero
        with pytest.raises(ZeroDivisionError):
            f[2] = get_instance.div(f[0],f[1])


#遇到分母为0时的2种处理方法，最好让用例尽量简单，不要混合写在一起
    # @pytest.mark.parametrize("a,b,result", div_combination[0], ids=div_combination[1])
    def test_div_normal_and_zero(self,get_instance,get_date_with_fixture_for_div_combination):
        f=get_date_with_fixture_for_div_combination
        if f[1]==0:
            with pytest.raises(ZeroDivisionError) as excinfo:
                get_instance.div(f[0],f[1])
            #断言异常类型type
            assert  excinfo.type==ZeroDivisionError
            #断言异常类型value值
            assert "division by zero" in str(excinfo.value)
        else:
            assert f[2]==get_instance.div(f[0],f[1])




if __name__=="__main__":
    # pytest.main("test_calculator.py::test_div_zero","vs")
    pytest.main("test_calculator.py","vs")





