def length(a):
    if type(a) in [str,list,tuple,set,dict]:
        return len(a)
    else:
        return a
out=map(length,[1,[1,2,2],(1,2,3,9),'sudhan'])
print(list(out))