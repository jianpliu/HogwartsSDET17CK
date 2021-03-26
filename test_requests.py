# -*-coding:GBK -*-
import requests
class TestAddress:
    def setup(self):
        self.token = self.get_token()


    def get_token(self):
        proxies = {"https":"http://127.0.0.1:8888"}
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwd7ef645590f8ecb5&corpsecret=7YwkwdazbUe7Ap0h1coCBjVYkCWsU0_6NNCwTq53J3k"
        r= requests.get(url,proxies=proxies,verify = False)
        return r.json()['access_token']

    def test_get_information(self):
        user_id = "zhangsanfeng"
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}")
        print(r.json())

    def test_create_member(self):
        proxies = {"https": "http://127.0.0.1:8888"}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
                "userid": "zhangsanfeng",
                "name": "张三",
                "alias": "jackzhang",
                "mobile": "+86 13888888888",
                "department": [1],
        }
        r = requests.post(url,json= data,proxies=proxies,verify = False)
        print(r.json())

    def test_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "zhangsanfeng",
            "name": "张三san",
        }
        r = requests.post(url, json=data)
        print(r.json())

    def test_delete(self):
        userid="zhangsanfeng"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        r = requests.get(url)
        print(r.json())







