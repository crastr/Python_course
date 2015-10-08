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
    if nondividers == []:
        return 'None'
    else:
        return ' '.join(nondividers)
a = ([int(i) for i in input().split()])
print(rpfilter(a[0], list(a[1::])))