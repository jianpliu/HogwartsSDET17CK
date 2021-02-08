## 项目介绍
霍格沃兹测试学院 测开17期实战演示

## 霍格沃兹
- [测试人论坛](https://ceshiren.com/)

## 参考链接
pytest: https://docs.pytest.org/en/stable/getting-started.html
## 作业地址


###pytest常用执行参数
pytest --collect-only 只收集用例
pytest -k "add" 匹配所有名称中包含add的用例（'add or div'、 'TestClass''）
pytest -m mark 标签名 标记
pytest --junitxml=./result.xml 生成执行结果文件
pytest --setup-show  回溯fixture的执行过程
####执行上一次失败的用例：在案例所在文件的cache/lastfailed :{XXX}:
pytest test_demo.py::test_answer







