def view(a):
    for i in a:
        if type(i) in[list,set,str,tuple,dict]:
            yield(len(i))
        else:
            yield(i)
out=view([1,[4,5,6],{7,8},'efg',9.5,12,{1:8}])
print(list(out))
