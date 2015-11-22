# put your python code here
a = input()
c = 1
for i in range(len(a)):
        if i == (len(a)-1):
            break
        elif sorted(a)[i] == sorted(a)[i+1]:
            c = c+1
        elif sorted(a)[i] != sorted(a)[i+1]:
            print(sorted(a)[i], c)
            c = 1
print(sorted(a)[-1], c)
