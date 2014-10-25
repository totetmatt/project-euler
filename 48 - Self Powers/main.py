### A Special Pow function that trash everything more than 10 digit
def lastTenPow(X,Y):
    tmp = X
    for r in range(1,X):
        tmp *= X
        if len(tmp.__str__()) > Y:
            tmp = int(tmp.__str__()[-Y:])
  
    return tmp
    
### Begin
s = [lastTenPow(x,10) for x in range(1,1001) ]
t = "%s"%sum(s)
print t[len(t)-10:]