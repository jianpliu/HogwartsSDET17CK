# print(round(1.99999999999,2))  #2.0
import yaml,os,sys
# def get_datas():
#     with open("./testing/datas/calc.yml") as f:
#         all_datas=yaml.safe_load(f)
#     return all_datas
#     # datas=all_datas[name][type]['datas']
#     # ids=all_datas[name][type]['ids']
#     # return (datas,ids)
#
# print(get_datas())
# print(type(get_datas()))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.getcwd())
print(os.path.dirname(os.getcwd()))

print(sys.path)
sys.path.append('..')

print(sys.path)