date=int(input("enter the date:"))
month=int(input("enter the month:"))
year=int(input("enter the year:"))
#f = k + [(13*m-1)/5] + D + [D/4] + [C/4] – 2*C
month=month-2
c=year//100
d=year%100
result=0
if (month>0 and month <=12) and (date>0 and date <=31) and (len(str(year))>4 and year<0):
    f=date+((13*month-1)/5)+d+(d/4)+(c/4)-2*c
    result=int(f)%7
    if result==0:
        print("sunday")
    elif result==1:
        print("monday")
    elif result==2:
        print("tuesday")
    elif result==3:
        print("wednesay")
    elif result==4:
        print("thursday")
    elif result==5:
        print("friday")
    else:
        print("saturday")
else:
    print("invalid format")

if flag==1:
    print("yes")
else:
    

    
    
'''
failed test case for this above code: bcas we cant find leap year or not
'''


