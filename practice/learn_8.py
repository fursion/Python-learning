def coro_agr():
    total = 0
    length = 0
    while True:
        try:
            value = yield total / length
        except ZeroDivisionError:
            value = yield 0
        total += value
        length += 1


my_avg = coro_agr()
next(my_avg)
my_avg.send(48)
my_avg.send(67)
my_avg.send(76)
print(my_avg.send(43))
