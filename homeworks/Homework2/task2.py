__author__ = 'Alex'
def prime(n):
    div = 2
    verd = True
    if n <= 1:
        verd = False
    else:
        while 2 * div <= n and verd == True:
            if n % div == 0:
                verd = False
            else:
                div += 1
        if verd == True:
            print('True')
        else:
            print('False')
quant = int(input())
for i in range (quant):
    a = int(input())
    prime(a)
