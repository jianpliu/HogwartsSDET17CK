import json

def handle_data(data):
    if isinstance(data,dict):
        for key,value in data.items():
            data[key] = handle_data(value)
    elif isinstance(data,list):
        data = [handle_data(item) for item in data]
    elif isinstance(data,str):
        data = data + "a"
    elif isinstance(data,bool):
        data = data
    elif isinstance(data,(int,float)):
        data = data*2
    else:
        data =data
    return data

if __name__ =='__main__':
    data=handle_data(json.load(open("11.json",encoding="utf-8")))
    print(data)
    with open("22.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)