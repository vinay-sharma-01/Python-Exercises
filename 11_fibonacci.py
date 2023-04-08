num=int(input("Enter number of elements"))
a=0
b=1 
if(num==0):
    print(0)
elif(num==1):
    print(0,1)
else:
    print(0, 1,end=" ")
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c,end=" ") 