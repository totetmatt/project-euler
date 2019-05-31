number = 600851475143 
import math
def isPrime(n):
    for j in range(int(n/2)+1,2,-1):
        if n % j == 0:
            return False   
    return True  
i = int(math.sqrt(number))
while i:
    if number % i == 0:
        if isPrime(i):
            print(i)
            break
    i -=1