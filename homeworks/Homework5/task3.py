# put your python code here
import re
import sys

code = sys.stdin.read()
to_test = code.split('\n')
line_counter = 1
results = []
for line in to_test:
    str_test = re.findall('((\w+) = )', line)
    if str_test:
        results.append(str(line_counter) + ' ' + str_test[0][1])
    line_counter += 1

print('\n'.join(results))
