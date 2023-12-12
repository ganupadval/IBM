def getHCF(x,y):
    while (x!=y):
        if x>y:
            x=x-y
        else: y=y-x
    return x
    
print(getHCF(70,15))