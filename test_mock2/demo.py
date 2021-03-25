def demo():
    with open("template.txt") as f:
        data = f.read()
        new_data=data.format(method = "get" , url = "www.baidu.com")
        print(new_data)
        with open("template.py","w",encoding="utf-8") as f:
            f.write(new_data)

if __name__=='__main__':
    demo()


