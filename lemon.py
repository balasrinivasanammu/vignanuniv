#print(chr(3128)+chr(3137),chr(3118),chr(3112))
#a,b,c=20,30,40
#print(a if a>b and a>c else b if b>c else c)
#a,b=20,30
#print(a if a>b else b)
'''
lemon=int(input('Enter the lemon:'))
if lemon>21:
    print(lemon-21,"we have an extra ")
elif lemon<21:
    print(21-lemon,"we want to buy")
else:
    print("sufficeint lemon")
'''

lemon=int(input('Enter the lemon'))
print((lemon-21,"we have an extra ") if lemon>21 else (21-lemon,"we want to buy") if lemon<21 else ("sufficient") if lemon==21 else "")







