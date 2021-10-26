import numpy as np
import sys

l = []
day, night = 0,0

for line in sys.stdin:
    ll = line.split(" ")
    for triple in ll:
        lll = triple.split(",")
        if (0.07*float(lll[0]) + 0.72*float(lll[1]) + 0.21*float(lll[2])) > 78:
            day += 1
        else:
            night += 1

if day > night:
    print('day')
else:
    print('night')