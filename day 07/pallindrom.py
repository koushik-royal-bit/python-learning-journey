v= input('enter string:').lower()
m="" 
for char in v:
    m= char+m
if v==m:
    print('palindrome')
else:
    print('not palindrome')