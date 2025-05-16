# without arg without return
a=250 # global
def balaji():
    a=10 # local
    print(a)

a=300
print(a)
balaji()