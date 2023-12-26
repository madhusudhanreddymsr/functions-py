def sum_list(l):
    sum=0
    for i in l:
        if type(i)==int:
            sum+=i
    print(sum)
sum_list([1,2,3,'asd',[1,2,3]])