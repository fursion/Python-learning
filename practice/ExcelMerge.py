#!/usr/bin/python3
import argparse
import os
import csv

ap = argparse.ArgumentParser()
ap.add_argument('-R', '--Remove_Duplicate', type=bool, default=False, help="控制是否去除重复项 默认 False不去重")
args = vars(ap.parse_args())
if args['Remove_Duplicate']:
    print('去重')
else:
    print('done')
