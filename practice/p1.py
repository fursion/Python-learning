# 进程间通讯IPC
# 文件
# 读写冲突
#  两个进程同时进行写，或者一个读一个写，就导致了冲突
# 解决读写冲突
#  互斥锁
import datetime
from threading import Thread
from multiprocessing import Process, Lock


def save_to_file(index, lock_log):
    with lock_log:
        with open("test1.log", "a", encoding="utf-8") as f:
            f.write(str(index) + "\n")


if __name__ == "__main__":
    process_array = []
    lock = Lock()
    for i in range(100):
        p = Process(target=save_to_file, args=(i, lock))
        process_array.append(p)
        p.start()
    for p in process_array:
        p.join()
    print("ex done")
