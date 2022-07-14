import cv2
import glob
import requests
import pandas as pd
import numpy as np

# 实例化
detect_obj = cv2.QRCodeDetector()
# 获取固定路径下的所有jpg格式图片
path = glob.glob(r"/Users/fursion/PycharmProjects/Python-learning/practice/*.png")
for i in range(len(path)):
    # 加载图片
    img = cv2.imread(path[i])
    # QR检测和解析
    qr_info, points, qr_img = detect_obj.detectAndDecode(img)
    # 可视化检测效果，绘制其外接矩形
    # cv2.drawContours(img, [np.int32(points)], 0, (0, 0, 255), 2)

    print(f'{path[i]}  info:', qr_info)


def DownloadImage(url):
    response = requests.get(url)
    img = response.content
    with open('ceshi.png', 'wb') as f:
        f.write(img)


def Read_CSV():
    db = pd.read_csv('4-5.csv')
    print(db.shape[0])
    for item in db.nrows:
        print(item[6])
    #print(db.iloc[0])


Read_CSV()
#DownloadImage('https://sf3-cn.feishucdn.com/obj/ee-oi-cdn/6939758083077849116-2022-04-29-01-31-29-952471.png')
