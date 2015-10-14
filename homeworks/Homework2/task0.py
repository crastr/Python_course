__author__ = 'Alex'


def plural(x, args):
    if x % 10 == 1 and x % 100 != 11:
        return args[0]
    elif (1 < x % 10 < 5) and (14 < x % 100 or x % 100 < 12):
        return args[1]
    else:
        return args[2]


vocab = {'утюг': ['утюг', 'утюга', 'утюгов'],
         'ложка': ['ложка', 'ложки', 'ложек'],
         'гармошка': ['гармошка', 'гармошки', 'гармошек'],
         'чайник': ['чайник', 'чайника', 'чайников']}
word = input()
number = int(input())
print("%d %s" % (number, plural(number, vocab[word])))
