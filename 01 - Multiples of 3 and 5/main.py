total = 0
for n in range(0,1000):
    total += n * (n%5==0 or n%3==0)
print total