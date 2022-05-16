import os, base64
import argparse
import sys

ap = argparse.ArgumentParser()
ap.add_argument('-s', '--imageBase64Str', help='Base64编码的图片字符串')
ap.add_argument('-S', '--image_source', help='image的路径')
args = vars(ap.parse_args())


def base64ToImage(base_str):
    imagedata = base64.b64decode(base_str)
    file = open('./temp.jpg', 'wb')
    file.write(imagedata)
    file.close()
    print('转换完成')


def imageToBase64(source):
    with open(source, 'rb') as file:
        base64_data = base64.b64encode(file.read())
        return base64_data


print(len(sys.argv))
imgs = imageToBase64(args['image_source'])
print(imgs)
base64ToImage(imgs)
# base64ToImage(args['imageBase64Str'])
