# -*-coding:GBK -*-

def b(fun):
    def run(*args,**kwargs):
        print("���")
        fun(*args,**kwargs)
        print("�ټ�")
    return run



@b
def a():
    print("����a")


def test():
    a()