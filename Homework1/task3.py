# put your python code here
a = ([int(i) for i in input().split()])
b = sorted(a[1::2], reverse=True)
c = sorted(a[::2])
d =[]
i = 0
for i in range(len(b)):
    print(c[i] , b[i], end=' ')
