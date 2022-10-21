#Check Whether a Number is a Prime or Not in Python

num=int(input("Enter the number:"))
#The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
if num >1:
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num,"is a prime")
