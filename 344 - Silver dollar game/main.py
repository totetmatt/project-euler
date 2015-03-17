from itertools import * 
import re
#a = "OCOCSC"
#print a, re.search("C(O?)C(O)?S",a)

def jam(lol):
    totalInterval =0 
    totalO = 0
    for e in re.compile("C|S").split(lol):
        if e !='':
            totalO+=len(e)
            totalInterval+=1
    return totalO%2 == totalInterval%2

a = "OCOCSCOOC"

def ok(pattern) :
        if pattern.index('S') < pattern.index('C'):
            return 1
        #if pattern[:pattern.index('S')].count('C')%2 == pattern[pattern.index('S'):].count('C')%2:
        #    if pattern[:pattern.index('S')].count('O')%2 == 0 and pattern[pattern.index('S')].count('O')%2 == 0 :
        #        return 1
        if jam("".join(pattern)):
            return 1
        if pattern[:pattern.index('S')].count('C')%2 == 0:
            if pattern[:pattern.index('S')].count('O') == 0:
                return 1
            else :
                return 0
            if pattern[pattern.index('S'):].count('C')%2 == 1 or  pattern[pattern.index('S'):].count('C')==0 :
                return 1
        else :
            return 1
        
            
        return 0
class W():
    def __init__(self,n,c):
        self.n = n
        self.c = c
        self.total=0
        self.board= "S"+ "C"*(c) + "O"*(n-(c+1))
        lol = {}
        for it in permutations(self.board, 10):
            if it not in lol:
                lol[it]=ok(it)
                self.total += lol[it]
        #for l in lol:
        #    print l,ok(l)
       
            
        
w = W(10,2)
print w.total