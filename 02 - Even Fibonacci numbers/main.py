
total = 0
p = [2,1]
while True:
    p.insert(0,sum(p))
    n = p.pop()
    if n <=4000000:
        total += n * (n%2==0)
    else:
        break
print total