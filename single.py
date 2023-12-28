def single(a):
    for i in a:
        if type() in [int,float,complex,bool]:
            return True
        else:
            return False
out=filter(single,[1,(1,2,3),4,4+3j,0])
print(list(out))