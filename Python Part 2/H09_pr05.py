def printPattern(n): 
    for i in range(n): 
        print("*"*(n-i))

n = int(input("Enter the n value: "))
printPattern(n)