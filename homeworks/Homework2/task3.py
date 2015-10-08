__author__ = 'Alex'
def euclid(n, m):
    if n % m == 0:
        return(m)
    else:
        return(euclid(m, n % m))
a = sorted(([int(i) for i in input().split()]), reverse=True)
print(euclid(a[0],a[1]))