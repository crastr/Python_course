# put your python code here
import re
import sys

code = sys.stdin.read()
to_test = code.split('\n')
line_counter = 1
results = []

for line in to_test:
    if re.match(' *#+', line):
        line_counter += 1
    else:
        str_test = re.match(' *([\w,. ]+) = ', line)
        if str_test:
            str_test = str(str_test.groups())
            str_test = re.sub('[()\']', '', str_test)
            results.append(str(line_counter) +
                           ' ' + ' '.join(str_test.split(',')))
        line_counter += 1

print('\n'.join(results))
