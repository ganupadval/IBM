def toBinary(x):
    arr=[]
    while x>0:
        if x%2==1:
            arr.append(1)
        else: 
            arr.append(0)
        x=x//2
    arr.reverse()
    return(arr)
print(toBinary(70))