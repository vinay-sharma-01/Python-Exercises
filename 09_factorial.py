# using normal for loop
# a=int(input("Enter a number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# using recursion
def fact(a):
    if a==0:
        return 1
    else:
        return (a*fact(a-1))

n=int(input("Enter a number: "))
print(fact(n))