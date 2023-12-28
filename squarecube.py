def square(a):
    if a%2==0:
        return a**2
    else:
        return a**3
out=map(square,[1,2,3,4])
print(list(out))