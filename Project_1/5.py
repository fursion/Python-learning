import requests
from threading import Thread

result = {}
arr = []


def requests_getinfo(index):
    url = "https://www.baidu.com/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39 "
    }
    re = requests.get(url=url, headers=header)
    print(f"请求序号:{index},返回结果状态码:{re.status_code}")
    result.setdefault(index, re)
    tu = (index, re)
    arr.append(tu)


if __name__ == "__main__":
    print("start")
    thread_array = []
    for i in range(5):
        t = Thread(target=requests_getinfo, args=(i,))
        t.start()
        thread_array.append(t)
    for t in thread_array:
        t.join()
    print("done")
    for r in arr:
        print(r)
