__author__ = 'Alex'
import math
with open("dict.txt", "r") as f:
    text = f.read()
word = text.split('\n')
adj = 0
verb = 0
noun = 0
for line in word:
    if line[-2::] == 'yo':
        adj += 1
    if line[-2::] == 'ka':
        noun += 1
    else:
        verb += 1

a = adj//7
print(a)
print(noun)
print(a * math.factorial(7) * verb * noun)
print('12345'[-2::])