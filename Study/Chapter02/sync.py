# 2.1. 동기와 비동기의 차이 (동기)

import time


def time_wait(n):
    for i in range(3):
        time.sleep(1)
        print(f"{n} : {i+1}번째")
    print()


def process_time():
    start = time.time()
    time_wait(3)
    time_wait(1)
    end = time.time()
    print("경과시간 : ", end - start)


process_time()
