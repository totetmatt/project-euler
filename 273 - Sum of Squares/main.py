import itertools
from functools import reduce 
import operator
def solve(n=65):
    r = n/2
    ret = []
    for b in range(r+1,1,-1):
        for a in range(1,b+1):
            if (a*a)+(b*b) == n:
                ret+=[a]
                
    return ret   
def isPrime(n):
    for j in range(int(n/2)+1,2,-1):
        if n % j == 0:
            return False   
    return True  
def issqrtfree(n=10):
    for k in range(2,n):
        print k
def sqrfreeprimegen():
    k = 0
    while 4*k+1 <150:
        if isPrime(4*k+1):
            yield 4*k+1
        k+=1
        
def s(n=65):
    return sum(solve(n))
    
prime = [x for x in sqrfreeprimegen()]

def validN(prime):
    for i in range(2,len(prime)+1):
        for ee in itertools.combinations(prime,r=i):
            yield reduce(operator.mul, ee, 1)
        
total =0
for N in validN(prime) :
    total += s(N)
print total

