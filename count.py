def count():

    a=input('Enter any string:')
    count=0
    for i in a:
        if '0'<=i<='9':
            count+=1
    print(count)
count()
count()