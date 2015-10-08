__author__ = 'Alex'
def plural (x, a, b, c):
    if x % 10 == 1 and x % 100 != 11:
        print(str(x), a)
    elif (1 < x % 10 < 5) and (14 < x % 100 or x % 100 < 12):
        print(x, b)
    else:
        print(x, c)
word = input()
number = int(input())
if word == 'утюг':
    plural(number, 'утюг', 'утюга', 'утюгов')
if word == 'ложка':
    plural(number, 'ложка', 'ложки', 'ложек')
if word == 'гармошка':
    plural(number, 'гармошка', 'гармошки', 'гармошек')
if word == 'чайник':
    plural(number, 'чайник', 'чайника', 'чайников')