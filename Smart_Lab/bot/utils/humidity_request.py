import requests
import os

url = os.environ.get("URL")


def on_req():
    data = {"code": "C_M_006"}
    r = requests.post(url, data=data)
    print("가습기 제어 : ON, Status Code:", r)
    return r


def off_req():
    data = {"code": "C_M_007"}
    r = requests.post(url, data=data)
    print("가습기 제어 : OFF, Status Code:", r)
    return r


def humidity_req(arg):
    data = {"code": "C_M_008", "setTemp": arg}
    r = requests.post(url, data=data)
    print("가습기 제어 : 습도, Status Code:", r)
    return r
