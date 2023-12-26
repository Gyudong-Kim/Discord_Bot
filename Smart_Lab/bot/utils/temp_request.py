import requests
import os

url = os.environ.get("URL")


def on_req():
    data = {"code": "C_M_001"}
    r = requests.post(url, data=data)
    print("냉난방기 제어 : ON, Status Code:", r)
    return r


def off_req():
    data = {"code": "C_M_002"}
    r = requests.post(url, data=data)
    print("냉난방기 제어 : OFF, Status Code:", r)
    return r


def temp_req(arg):
    data = {"code": "C_M_003", "setTemp": arg}
    r = requests.post(url, data=data)
    print("냉난방기 제어 : 온도, Status Code:", r)
    return r


def flow_req(arg):
    data = {"code": "C_M_004", "setFlow": arg}
    r = requests.post(url, data=data)
    print("냉난방기 제어 : 바람세기, Status Code:", r)
    return r


def mode_req(arg):
    data = {"code": "C_M_005"}
    r = requests.post(url, data=data)
    print("냉난방기 모드 제어 : 바람세기, Status Code:", r)
    return r
