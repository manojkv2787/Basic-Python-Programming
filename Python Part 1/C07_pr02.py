name = input("Enter your name: ")
date = input("Enter your date: ")

template = '''
Deat <|name|>,
you born on
<|date|>
'''

print(template.replace('<|name|>', name).replace('<|date|>', date))