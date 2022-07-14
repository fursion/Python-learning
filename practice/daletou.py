import random
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-C', '--Count', type=int, default=5, help='需要生成的注数')
args = vars(ap.parse_args())


def creat(star, end):
    var = random.randint(star, end)
    return var


def start():
    red_count = 5
    blue_count = 2
    red_arry = []
    blue_arry = []
    for red in range(red_count):
        var = creat(1, 35)
        while var in red_arry:
            var = creat(1, 35)
        red_arry.append(var)
    for blue in range(blue_count):
        var = creat(1, 12)
        while var in blue_arry:
            var = creat(1, 12)
        blue_arry.append(var)
        red_arry.sort()
        blue_arry.sort()
    print(red_arry + blue_arry)


for x in range(args['Count']):
    start()
