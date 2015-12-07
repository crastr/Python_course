# put your python code here
import re
import sys

text = sys.stdin.read()
neat = re.findall('(\d*(1{3}|2{3}|3{3}|4{3}|5{3}|'
                  '6{3}|7{3}|8{3}|9{3}|0{3})\d*)', text)
print('\n'.join([x[0] for x in neat]))
