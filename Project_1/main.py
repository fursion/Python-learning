import time
import datetime
#from Project_2 import ceshi

from datetime import datetime as f_datetime
# 查看时间
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(now)
class Testclass(object):
    def __init__(self) -> None:
        self.age = 30
    def fun01():
        print("Testclass_Fun01")
def fun1():
    print(time.time())
    print(f_datetime.today())
    # 获取UTC时间
    da = datetime.datetime.utcnow()
    print(time.time())
    print(type(da))
    test = Testclass()
    # test.fun01()
    print(f"age :{test.age}")
    #ceshi.im() 
fun1()
