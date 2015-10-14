__author__ = 'Alex'


def prime(n):
    div = 2
    verd = True
    if n <= 1:
        verd = False
    else:
        while 2 * div <= n and verd is True:
            if n % div == 0:
                verd = False
            else:
                div += 1
    return verd
quant = int(input())
for i in range(quant):
    a = int(input())
    print(prime(a))
