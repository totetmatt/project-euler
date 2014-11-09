pyr = [9,range(1,5)]
cub = [6,range(1,7)]
import itertools

from collections import Counter
pyrlist = list(itertools.product(pyr[1],repeat=pyr[0]))
pyrlist = Counter([sum(r) for r in pyrlist])

cublist = list(itertools.product(cub[1],repeat=cub[0]))
cublist =  Counter([sum(r) for r in cublist]) 

freqpy= {}
freqcub = {}
# Distribution Sum = Freq to have <=k 
freqcubt = {}

for result in pyrlist:
    #print "Stat for %s"%result
    freqpy[result] =  float(pyrlist[result])/(pow(4,9))
    
temp = 0

for result in cublist:
    #print "Stat for %s"%result
    freqcub[result] = float(cublist[result])/(pow(6,6))
    temp += freqcub[result]
    freqcubt[result] = temp

total = 0
for result in freqpy:
    total += freqpy[result]* freqcubt[result-1]
print '%.7f'%total
