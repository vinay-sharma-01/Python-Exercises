n=int(input('Enter the number of table you need: '))
tb=1
for i in range(1,11):
    tb=n*i
    print(n,' * ',i,' = ',tb)
    i=i+1
