class Anilinterrupt:
    pass
a=input('Enter any String:')
if a[0] in 'aeiouAEIOU':
    raise Anilinterrupt('first character should be a vowel')

