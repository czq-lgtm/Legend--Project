"""
进程属性展示
"""
from multiprocessing import Process
import time

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)
p = Process(target = fun,name = "Tedu")

# 父进程退出该子进程也退出
p.daemon = True

p.start()

print("Name:",p.name)
print("PID：",p.pid)
print("is_alive:",p.is_alive())