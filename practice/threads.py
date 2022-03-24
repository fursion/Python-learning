from threading import Thread, Lock


zero = 0
lock = Lock()

def ex():
    global zero
    for i in range(10**6):
        with lock:
            zero+=1
            zero-=1


if __name__ == "__main__":
    thread_array = []
    for i in range(3):
        th = Thread(target=ex)
        thread_array.append(th)
        th.start()
    for th in thread_array:
        th.join()

    print(zero)