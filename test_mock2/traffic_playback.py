import json

from mitmproxy import ctx,http

class Counter:
    #
    def request(self,flow:http.HTTPFlow):
        url = flow.request.pretty_url
        method = flow.request.method
        with open(r"C:\home\Python\study\HogwartsSDE17CK\test_mock2\template.txt") as f:
            data = f.read()
            new_data = data.format(method=method, url=url)
            print(new_data)

        with open(r"C:\home\Python\study\HogwartsSDE17CK\test_mock2\template.py", "w", encoding="utf-8") as f:
            f.write(new_data)

    def response(self,flow: http.HTTPFlow):
        pass

addons=[
    Counter()
]