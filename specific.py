try:
    a=2+'2'
    print(a)
except TypeError:
    print('Error Handled')
finally:
    print('Exception Handled')
def sum(a,b):
    return a+b
print(sum(2,3))