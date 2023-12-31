ar=[0,1,-3,2,-1]
sum=int(input('enter:'))
for i in range(len(ar)):
    for j in range(len(ar)):
        if j>i:
            for k in range(len(ar)):
                if k>i:
                    if ar[i]+ar[j]+ar[k]==sum:
                        print({ar[i],ar[j],ar[k]})