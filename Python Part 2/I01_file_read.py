f = open("I01_this.txt", "r") 

# text = f.read()
# print(text)
# text = f.read(10)
# text = f.readline()
# text = f.readline()
# print(text)
# text = f.readline()
# print(text)

textList=f.readlines() 
print(textList)
f.close()