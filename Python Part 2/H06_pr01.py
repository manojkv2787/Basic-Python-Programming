def greatest(num1, num2, num3):
    if(num1>num2):
        greater = num1
    else:
        greater = num2
    if(num3>greater):
        greater = num3
    return greater
        
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
a = greatest(num1, num2, num3) 
print("The greatest number is:", a)