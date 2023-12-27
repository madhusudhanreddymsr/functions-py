def fact(a,n=1):
    if a==n:
        return n
    return n*fact(a,n+1)
print(fact(5))