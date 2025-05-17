'''n= input("Enter a number: ")
if '-' in n:
    n=n.replace('-','')
    rev=int(n[::-1])
    print(0-rev)
else:
    reversed_num = int(n[::-1])
    print("Reversed number:", reversed_num)'''

num=input()
r=(num[::-1] if int(num)>0 or int(num)==0 else '-'+num[:0:-1])
print(r)