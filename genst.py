def squ(a,b):
    for i in range(5,15):
        yield(i**2)
        yield(i+i)
out=squ(5,15)
print(out)
print(list(out))
