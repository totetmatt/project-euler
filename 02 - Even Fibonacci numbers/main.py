
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
"""
def fib_even(n):
    total = 0
    p = [1,2]
    for r in range(0,n-2):
        local_sum = sum(p[-2:])
        if local_sum <= n:
            p.append(local_sum)
        else:
            break;
    return sum([s for s in p if s%2==0])
print(fib_even(4000000))
"""
