import json

from mitmproxy import ctx,http

class Counter:
    #
    # def request(self,flow):
    #     self.num = self.num+1
    #     ctx.log.info("We've seen %d flows"%self.num)

    def response(self,flow: http.HTTPFlow):
        #判断请求的url是否包含指定的url信息
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            print(flow.response.text)
            # data = json.loads(flow.response.text)
            # data["data"]["items"][0]["quote"]["name"] = "hogwartyyyyyyyyyyyyyyyyyy"
            # flow.response.text = json.dumps(data)

addons=[
    Counter()
]