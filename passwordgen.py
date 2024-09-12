import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
digits = '0123456789'
symbols = '!@#$%^&*()/{}[]*-+<>?;":|`~.,_'
plen = int(input("\nEnter the password length : "))
s = []
s.extend(list(upper))
s.extend(list(lower))
s.extend(list(digits))
s.extend(list(symbols))
 
random.shuffle(s)
print("".join(s[0:plen]))