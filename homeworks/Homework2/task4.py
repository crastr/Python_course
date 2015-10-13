__author__ = 'Alex'
def euclid(n, m):
    if n % m == 0:
        return m
    else:
        return euclid(m, n % m)
def rpfilter (number, args):
    nondividers = []
    for arg in args:
        if euclid(number, arg) == 1:
            nondividers.append(str(arg))
    return ' '.join(nondividers)
a = ([int(i) for i in input().split()])
if len((rpfilter(a[0], list(a[1::])))) == 0:
    print('None')
else:
    print(rpfilter(a[0], list(a[1::])))