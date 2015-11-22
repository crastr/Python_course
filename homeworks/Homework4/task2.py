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
print(adj, verb, noun)
multiplier = 0
if adj < 7:
    for i in range(1, (adj+1)):
        multiplier += math.factorial(adj)/(math.factorial(adj-i))
else:
    for i in range(1, 8)
        multiplier += math.factorial(adj)/(math.factorial(adj-i))
print(multiplier * verb * noun)
