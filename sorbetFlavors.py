flavors= [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

x=y=0

nFlavors=sum([6, 5, 4, 3, 2, 1]) 

for flavor in range(nFlavors):
    if x==y:
       y=y+1

    if y<len(flavors)-1:
        print(f'{flavors[x]}, {flavors[y]}')
        y=y+1
    else:
        print(f'{flavors[x]}, {flavors[y]}')
        x=x+1
        y=x+1
