import re
import sys

text = sys.stdin.read()
text = re.sub('\W+', ' ', text)

print(text)
