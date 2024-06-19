import string

x=y=0

alphabet=string.ascii_lowercase

for _ in range(len(alphabet)*len(alphabet)-len(alphabet)):

    if x==y:
        y=y+1
        
    if y<len(alphabet)-1:
            print(alphabet[x]+alphabet[y])
            y=y+1
    else:
            print(alphabet[x]+alphabet[y])
            y=0
            x=x+1
