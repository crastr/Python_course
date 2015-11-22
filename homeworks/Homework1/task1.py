__author__ = 'Alex'
__author__ = 'Alex'
a = input('')
b = int(input())
d = (b%100)
if a =='ложка':
    if d == 1 or d == 21 or d == 31 or d == 41 or d == 51 or d == 61 or d == 71 or d == 81 or d == 91:
        print (b, a)
    elif 2<=d<=4 or 22<=d<=24 or 32<=d<=34 or 42<=d<=44 or 52<=d<=54 or 62<=d<=64 or 72<=d<=74 or 82<=d<=84 or 92<=d<=94:
        print(b, a[0:4]+'и')
    else:
        print(b, a[0:3]+'ек')
else:
    if d == 1 or d == 21 or d == 31 or d == 41 or d == 51 or d == 61 or d == 71 or d == 81 or d == 91:
        print (b, a)
    elif 2<=d<=4 or 22<=d<=24 or 32<=d<=34 or 42<=d<=44 or 52<=d<=54 or 62<=d<=64 or 72<=d<=74 or 82<=d<=84 or 92<=d<=94:
        print(b, a+'а')
    else:
        print(b, a+'ов')