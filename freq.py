def frequency(a,b):
    count=0
    for i in a:
        if i==b:
            count+=1
    print(count)
frequency('madhu','a')
frequency([1,2,3,4,5,5,4,3,3,2,1],2)