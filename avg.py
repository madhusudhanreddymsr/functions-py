def avg(a):
    for i in a:
        if len(a[i])%2==0:
            yield(i[0]+i[-1]/2)
        else:
            yield i[len(i)//2]
out=avg([(1,2),[1,2,3,4,5],(1,2,3,3),[1,2,4,6]])
print(list(out))
                
