import string

alphabet=string.ascii_lowercase

x=y=0

for _ in range(len(alphabet)**2):
 
    if y<len(alphabet)-1:
        print(alphabet[x]+alphabet[y])
        y=y+1
    else:
        print(alphabet[x]+alphabet[y])
        y=0
        x=x+1
