
import random
from itertools import permutations

maxSum = 0

import copy
def findOverlap(s):
    for s1 in range(0,len(s)):
        for s2 in range(s1,len(s)):
            if s1 != s2:
                if s[s1][0] == s[s2][0] or s[s1][1] == s[s2][1] or s[s1][0] == s[s2][1] or s[s1][1] == s[s2][0]:
                    return (s[s1],s[s2])
    return False

def ssum(s):
    st = 0
    for t in s:
        st+= t[2]
    return st
def matrixsum(X,Y):
    r = []
    for x in range(0,len(X)):
        for y in range(0,len(Y)):
            if x != y:
                r  +=[(x,y,X[x]+Y[y])]
    #newlist = sorted(r, key=lambda k: k[2],reverse=True) 
    return r
X = [[7,53,183,439,863,497,383,563,79,973,287,63,343,169,583],
[627,343,773,959,943,767,473,103,699,303,957,703,583,639,913],
[447,283,463,29,23,487,463,993,119,883,327,493,423,159,743],
[217,623,3,399,853,407,103,983,89,463,290,516,212,462,350],
[960,376,682,962,300,780,486,502,912,800,250,346,172,812,350],
[870,456,192,162,593,473,915,45,989,873,823,965,425,329,803],
[973,965,905,919,133,673,665,235,509,613,673,815,165,992,326],
[322,148,972,962,286,255,941,541,265,323,925,281,601,95,973],
[445,721,11,525,473,65,511,164,138,672,18,428,154,448,848],
[414,456,310,312,798,104,566,520,302,248,694,976,430,392,198],
[184,829,373,181,631,101,969,613,840,740,778,458,284,760,390],
[821,461,843,513,17,901,711,993,293,157,274,94,192,156,574],
[34,124,4,878,450,476,712,914,838,669,875,299,823,329,699],
[815,559,813,459,522,788,168,586,966,232,308,833,251,631,107],
[813,883,451,509,615,77,281,613,459,205,380,274,302,35,805]]
X  = [[7,53,183,439,863],
[497,383,563,79,973],
[287,63,343,169,583],
[627,343,773,959,943],
[767,473,103,699,303]]
listOfMax = []
for x in range(0,len(X)):
    for y in range(x,len(X)):
        if x != y:
            #print X[x] , X[y]
            listOfMax += matrixsum(X[x] , X[y])
slistOfMax = sorted(listOfMax, key=lambda k: k[2],reverse=True) 
print slistOfMax
soluce = []
for x in range(0,len(X)):
    soluce += [slistOfMax.pop()]
x = 0
print findOverlap(soluce)
"""while x != len(X)-1:
    s = findOverlap(soluce)
    if s: 
        print s
    x += 1"""
"""ov = findOverlap(soluce)
while ov and slistOfMax:
    soluce.remove(ov[1])
    soluce += [slistOfMax.pop()]
    ov = findOverlap(soluce)

print ssum(soluce),soluce
"""
for c in permutations(slistOfMax,len(X)):
    if not findOverlap:
        print ssum(c)

    