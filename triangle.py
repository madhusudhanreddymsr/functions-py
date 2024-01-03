row=int(input('enter:-'))
stars=1
spaces=row-1
for i in range(1,row+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    stars+=1
    spaces-=1