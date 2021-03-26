import requests
def request_demo():
    res = requests.request(method="POST",url="http://211.103.164.29:8081/oa/rest/workDetail/gscx")


if __name__=='__main__':
    request_demo()
