def vowelindex(a):
    l=[]
    for i in range(0,len(a)):
        if a[i] in 'aeiouAEIOU':
            l=l+[i]
        i+=1
    return l
b=vowelindex('madhusudhan')
print(b)
