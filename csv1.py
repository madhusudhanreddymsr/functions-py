import csv
with open('mca.csv','w',newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerows(csvfile)
    data.writerows(['id,''name','mobile','email'])
    data2=[
        [1,'charan','6305238446','fff@gmail.com'],
        [2,'charan1','6305238447','fgf@gmail.com'],
        [3,'charan2','6305238448','fhf@gmail.com'],
        [4,'charan3','6305238449','fif@gmail.com'],
    ]
    data.writerows(data2)
