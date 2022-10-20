num=int(input("enter number:"))
l=[]
for i in range(2,num+1):
    if num%i==0:
        for j in range(2,i):
            if (i % j)==0:
                break
        else:
            l.append(i)
print(l)
