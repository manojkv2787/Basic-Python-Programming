def cel2far(cel): 
    return (cel * 9/5) + 32

cel = int(input("Enter tempareture in celsius: "))
a = cel2far(cel)
print("The tempareture in fahrenhit is:", a)