def upper(a):
    if 'A'<=a<='Z':
        return True
    else:
        return False
out=filter(upper,'aB@15$67DEfg4')
print(list(out))
