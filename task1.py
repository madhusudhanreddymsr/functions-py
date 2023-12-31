print("WELCOME TO BOOK MY SHOW")
name=input('Please Enter your name:-')
dt,gt,st=30,30,40
print('seats in Diamond:-30 \nseats in Gold:-30 \nseats in Silver:-40')
db,gb,sb=23,26,28
print('Filled in Diamond:-23 \nFilled in Gold:-26 \nFilled in Silver:-28')
seats=int(input('Please Enter no.of seats do you want:-'))
cls=int(input('Enter class \n 1 for Diamond:- \n 2 for gold:- \n 3 for silver:-'))
if cls==1:
    aval1=dt-db
    if seats<=aval1:
        amt=seats*200
        print(f'Hi {name} you booked {seats} seats and amount is RS {amt}')
    else:
        print('Sorry...! seats are insufficient')
elif cls==2:
    aval2=gt-gb
    if seats<=aval2:
        amt=seats*150
        print(f'Hi {name} you booked {seats} seats and amount is RS {amt}')
    else:
        print('Sorry...! seats are insufficient')
elif cls==3:
    aval3=st-sb
    if seats<=aval3:
        amt=seats*100
        print(f'Hi {name} you booked {seats} seats and amount is RS {amt}')
    else:
        print('Sorry...! seats are insufficient')
else:
    print('Please Enter valid class')
