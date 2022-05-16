#!/usr/bin/python3
import argparse
import os
import csv

print('文件合并工具')
ap = argparse.ArgumentParser()
ap.add_argument('-R', '--Remove_Duplicate', type=bool, default=False, help="控制是否去除重复项 默认 False不去重")
ap.add_argument('-f', '--files', nargs='*', help='需要操作的文件')
args = vars(ap.parse_args())
if args['Remove_Duplicate']:
    print('去重')
else:
    print('done')


def read_f():
    print(args['files'])


def Remove_Duplicate():
    print('')


read_f()
