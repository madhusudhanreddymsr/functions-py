var=[1,2,3,4,5,6,7,8,9]
def add(var,i=0):
    if len(var)-1==i:
        return var[i]
    return var[i]+add(var,i+1)
print(add(var))
    