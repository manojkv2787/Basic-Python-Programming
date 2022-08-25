print("Enter Marks Obtained in 6 Subjects: ")
mark1 = int(input("Subject 1: "))
mark2 = int(input("Subject 2: "))
mark3 = int(input("Subject 3: "))
mark4 = int(input("Subject 4: ")) 
mark5 = int(input("Subject 5: "))
mark6 = int(input("Subject 6: "))

total = mark1 + mark2 + mark3 + mark4 + mark5 + mark6
print("The total marks is:", total)
avg = total/6
print("The percentage is:", avg)

if avg>=91 and avg<=100:
    print("Your Grade is S") 
elif avg>=81 and avg<=90:
    print("Your Grade is A")
elif avg>=71 and avg<=80:
    print("Your Grade is B")
elif avg>=61 and avg<=70:
    print("Your Grade is C") 
elif avg>=51 and avg<=60:
    print("Your Grade is D") 
elif avg>=40 and avg<=50:
    print("Your Grade is E") 
elif avg<40:
    print("Your Grade is F")
else:
    print("Invalid Input!")