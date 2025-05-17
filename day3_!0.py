def sumd(num):
    total = sum(int(d) for d in str(num))
    print("sum of digit",total)
    slen=str(total)
    if len(slen)!=1:
        sumd(int(total))
num=int(input("enter a number"))
sumd(num)
    
    





'''num = int(input("Enter a number: "))
total = sum(int(d) for d in str(num))
print("Sum of digits:", total)'''
