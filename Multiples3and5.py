def multiples():
    s=0
    for n in range(1000):
        if n%3==0 or n%5==0:
            s=s+n
    return s
        
print(multiples())
