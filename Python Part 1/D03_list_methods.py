myListOfNumber = [1,8,7,2,21,15]
print(myListOfNumber)
a = myListOfNumber.sort() # Not returning any thing but moudifing the orginal list
print(a)

myListOfNumber.sort() # Sorts the original list
print(myListOfNumber)
myListOfNumber.reverse() # Reverse the original list
print(myListOfNumber)
myListOfNumber.append(0) # Add 0 at the end of the original list
print(myListOfNumber)
myListOfNumber.insert(2, 9) # Inserts 9 at index 2 of the original list
print(myListOfNumber)
myListOfNumber.pop() # Remove an item from the end of the original list
print(myListOfNumber)
myListOfNumber.pop(2) # Remove an item from the given index from the original list
print(myListOfNumber)
myListOfNumber.remove(21) # Removes the first accurance of a given item from the list
print(myListOfNumber)