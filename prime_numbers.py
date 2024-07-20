import math

def is_prime(n):
    numbers = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            numbers.append(i)

    if n == 1:
        return False
    elif len(numbers) > 1:
        return False
    else:
       return True
    
