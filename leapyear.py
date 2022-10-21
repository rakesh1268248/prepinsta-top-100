year=int(input("Enter the number:"))
#logic-1

if (year % 4 ==0  or year % 100 !=0) and year % 400 == 0:
    print("leap")
else:
    print("not a leap")

#logic-2
if (year % 4 ==0  and year % 100 !=0) or year % 400 == 0:
    print("leap")
else:
    print("not a leap")
