import pytest

@pytest.fixture(params=[['harry','hemin'],["rry","tty"]],ids=["aaa","bbb"])

def login(request):
    print("login")
    return request.param


def test_search(login):
    print(login)
    print("搜索")


def check_search(login):
    print(login)
    print("下单")
