# -*-coding:GBK -*-
import json

from mitmproxy import ctx,http

class Counter:

    def request(self,flow: http.HTTPFlow):
        """
        使用request事件实现map local
        :param flow:
        :return:
        """

        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            with open(r"C:\home\Python\study\HogwartsSDE17CK\test_mock2\11.json",encoding="utf=8") as f:
                flow.response = http.HTTPResponse.make(200,#(optional) status
                                                       f.read(),#(optional) content
                                                       {"Content-Type": "text/html"}
                                                       )

    def response(self,flow: http.HTTPFlow):
        pass


addons=[
    Counter()
]