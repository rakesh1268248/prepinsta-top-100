def sumofnum(sum,num1,num2):
    if num1>num2:
        return sum
    else:
        return num1 + sumofnum(sum,num1+1,num2)
num1,num2=3,6
sum=0
print(sumofnum(sum,num1,num2))
