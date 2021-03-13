# -*-coding:GBK -*-

def b(fun):
    def run(*args,**kwargs):
        print("你好")
        fun(*args,**kwargs)
        print("再见")
    return run



@b
def a():
    print("我是a")


def test():
    a()