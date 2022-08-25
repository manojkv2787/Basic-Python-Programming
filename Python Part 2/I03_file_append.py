f = open("I02_write.txt", "w") # Write mode
f = open("I02_write.txt", "a") # Append mode
f.write("This is a text, I want to write to this file\n")
f.write("Second line: This is a text, I want to write to this file")
f.close()