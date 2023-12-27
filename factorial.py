def fact(a):
    fact=1
    i=1
    while i<=a:
        fact=fact*i
        i+=1
    
    return fact

b=fact(5)
print(b)