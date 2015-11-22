__author__ = 'Alex'


def combinations(n, k):
    if k > n:
        return (0)
    elif k == n or k == 0:
        return(1)
    else:
        return combinations(n - 1, k - 1) + combinations(n - 1, k)
a = ([int(i) for i in input().split()])
print(combinations(a[0], a[1]))
