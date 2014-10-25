 ##Pn=n(3n-1)/2.
def P(n):
    return n * (3 * n - 1)/2
penlist = {} 
for r in range(1,100000):
    penlist[P(r)] = True
for r in range(1,10000): 
    for s in range(1,10000): 
        if P(r) + P(s) in penlist and P(r) - P(s) in penlist :
            print P(r) - P(s)
            exit()
       
        

