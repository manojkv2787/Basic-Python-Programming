oxford = {
    "gift": "Something to give",
    "this": "A keyword in c++",
    "youtube": "A video sharing plateform",
    "instagram": "A picture sharing platfornm",
    "myList": [1, 3, 45]
}

oxford.update({"Manoj":"Good boy", "myList": [56, 8]})
print(oxford.items())
for a, b in oxford.items():
    print(a, ":=", b)
    
for key in oxford.keys():
    print(key)
    
print(oxford["this"])
# print(oxford['notpresent'])
print(oxford.get('notpresent'))