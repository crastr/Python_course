__author__ = 'Alex'
def plural (x, *args):
    if x % 10 == 1 and x % 100 != 11:
        return args[0]
    elif (1 < x % 10 < 5) and (14 < x % 100 or x % 100 < 12):
        return args[1]
    else:
        return args[2]
word = input()
number = int(input())
if word == 'утюг':
    print("%d %s" % (number, plural(number, 'утюг', 'утюга', 'утюгов')))
if word == 'ложка':
    print("%d %s" % (number, plural(number, 'ложка', 'ложки', 'ложек')))
if word == 'гармошка':
    print("%d %s" % (number, plural(number, 'гармошка', 'гармошки', 'гармошек')))
if word == 'чайник':
    print("%d %s" % (number, plural(number, 'чайник', 'чайника', 'чайников')))