#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure
import pytest
import sys,yaml
sys.path.append('..')
print(sys.path)

from pythoncode.Calculator import Calculator

def get_datas(name,type='int'):
    with open("./datas/calc.yml",encoding='utf-8') as f:
        all_datas=yaml.safe_load(f)
    datas=all_datas[name][type]['datas']
    ids=all_datas[name][type]['ids']
    return (datas,ids)

#测试类
class TestCalc():
    add_int_data = get_datas('add','int')
    add_decimal_data = get_datas('add','decimal')
    div_int_data = get_datas('div','int_normal')
    div_zero_data= get_datas('div','int_error')
    div_combination = get_datas('div','int_normal_and_error')




    #前置条件
    def setup_class(self):
        print("开始计算")
        self.calc=Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.login #和pytest.ini结合使用
    @pytest.mark.parametrize("a,b,result",add_int_data[0],ids=add_int_data[1])
    def test_add(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a,b)

    @pytest.mark.search
    @pytest.mark.parametrize("a,b,result",add_decimal_data[0],ids=add_decimal_data[1])
    def test_add_decimal(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert round(result,2)==round(self.calc.add(a,b),2)


    @pytest.mark.parametrize("a,b,result", div_int_data[0], ids=div_int_data[1])
    def test_div(self, a, b, result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.div(a, b)


    @pytest.mark.parametrize("a,b,result", div_zero_data[0], ids=div_zero_data[1])
    def test_div_zero(self, a, b, result):
        with pytest.raises(ZeroDivisionError):
            result = a/b
#遇到分母为0时的2种处理方法，最好让用例尽量简单，不要混合写在一起
    @pytest.mark.parametrize("a,b,result", div_combination[0], ids=div_combination[1])
    def test_div_normal_and_zero(self, a, b, result):
        if b==0:
            with pytest.raises(ZeroDivisionError) as excinfo:
                self.calc.div(a,b)
            #断言异常类型type
            assert  excinfo.type==ZeroDivisionError
            #断言异常类型value值
            assert "division by zero" in str(excinfo.value)
        else:
            assert result==self.calc.div(a,b)




if __name__=="__main__":
    # pytest.main("test_calculator.py::test_div_zero","vs")
    pytest.main("test_calculator.py","vs")





