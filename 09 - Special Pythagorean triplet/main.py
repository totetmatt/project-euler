import itertools
import math

p = [r*r for r in range(1,1000)]
for a in itertools.permutations(p, 2):
    if a[0] + a[1] in p:
        if  math.sqrt(a[0]) + math.sqrt(a[1]) + math.sqrt(a[0] + a[1]) == 1000:
            print(int(math.sqrt(a[0]) * math.sqrt(a[1]) * math.sqrt(a[0] + a[1])))
            break
