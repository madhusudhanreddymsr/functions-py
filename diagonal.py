row=int(input('enter rows:'))
col=int(input('enter column:'))
for i in range(row):
    for j in range(col):
        if i==j:
            print('+',end=' ')
        else:
            print(end=' ')
    print()