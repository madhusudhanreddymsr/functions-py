def mul(a):
    for i in range(1,200):
        if a%3==0 and a%5==0:
            return True
        else:
            return False
out=filter(mul,range(1,200))
print(list(out))