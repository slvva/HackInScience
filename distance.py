points=[1, 2]

def dist(points):
    distMax=max(points)
    distMin=min(points)
    bigger=distMax-distMin
    return bigger
    
print(dist(points))
