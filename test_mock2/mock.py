
import json
from mitmproxy import ctx,http
class Counter:


    def request(self,flow):
        # self.num = self.num + 1
        # ctx.log.info("We've seen %d flows"%self.num)
        pass

    def response(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # print(json.loads(flow.response.text))
            data = self.handle_data(json.loads(flow.response.text))
            print(data)
            flow.response.text = json.dumps(data)

    def handle_data(self,data):
        if isinstance(data, dict):
            for key, value in data.items():
                data[key] = self.handle_data(value)
        elif isinstance(data, list):
            data = [self.handle_data(item) for item in data]
        elif isinstance(data, str):
            data = data
        elif isinstance(data, bool):
            data = data
        elif isinstance(data, (int, float)):
            data = data*2
        else:
            data = data
        return data


addons=[
    Counter()
]

