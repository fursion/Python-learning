import os
import csv


def asset():
    with  open("33c365-360.csv") as f:
        for line in f:
            print(line)


def list_all_file(rootpath):
    files = []
    lists = os.listdir(rootpath)
    for i in range(0, len(lists)):
        path = os.path.join(rootpath, lists[i])
        if os.path.isdir(path):
            files.extend(list_all_file(path))
        if os.path.isfile(path):
            files.append(path)
    return files


print("请输入文件夹路径")
tar = "/Users/fursion/Downloads/33F汇总"
filelist = list_all_file(tar)
with open(f"{tar}.csv", 'ab') as tarfile:
    for filepath in filelist:
        with open(filepath, 'rb') as s_data:
            for line_data in s_data:
                line_data = line_data + f"\"{filepath}\""
                tarfile.write(line_data)
print("汇总完成")
