firstNumber=int(input("Enter firstNumber"))
secondNumber=int(input("Enter the secondNumber"))
print("Before swapping:")
print(firstNumber)
print(secondNumber)
firstNumber=firstNumber+secondNumber
secondNumber=firstNumber-secondNumber
firstNumber=firstNumber-secondNumber
print("After swapping:")
print(firstNumber)
print(secondNumber)