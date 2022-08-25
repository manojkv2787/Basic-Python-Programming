a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

if(a>b):
    maxNum1 = a
else:
    maxNum1 = b
    
if(c>d):
    maxNum2 = c
else:
    maxNum2 = d

if(maxNum2>maxNum1):
    maxNum = maxNum2
else:
    maxNum = maxNum1

print("Maximum number out of these four numbers is", maxNum)