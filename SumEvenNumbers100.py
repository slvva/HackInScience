def sum():
    s=0
    for n in range(101):
        if n%2==0:
           s=s+n
    return s
        
print(sum())
