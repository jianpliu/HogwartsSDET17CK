import requests
def request_demo():
    res = requests.request(method="POST",url="https://ceshiren.com/message-bus/e628d681137244f49af4da5f93195993/poll?dlp=t")


if __name__=='__main__':
    request_demo()
