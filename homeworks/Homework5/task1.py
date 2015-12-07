import re
import sys
text = sys.stdin.read()
number = len(re.findall('[Y|y]ou', text))
print(number)
