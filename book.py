print('Welcome To BookMyShow')
name=input('Enter your Name:-')
seats=int(input('Enter Number of seats:-'))
select=int(input('enter 1 for diamond enter 2 for gold enter 3 for silver'))
price1=200
price2=150
price3=100
if select==1:
    price1=price1*seats
    print('your booking successful and amount is:-'+str(price1))
elif select==2:
    price2=price2*seats
    print('your booking successful and amount is:-'+str(price2))
else:
    price3=price3*seats
    print('your booking successful and amount  is:-'+str(price3))