name = "eric"
print(f"hello {name}, would you like to learn some python?")
print(name.title())
print(name.upper())
#####
famous_person = 'Albert Einstein'
message = "A person who never made a mistake never tried anything new."
print(f"{famous_person} once said, {message}")
#####
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
#####
names= ["sara", "ali", "mary", "lucy"]
print(f"hello {names[0]}, how are you?")
#####
guest = ['dany', 'mary', 'lucy', 'alic']
print(f'dear {guest[0]}, i would like to invite you.')
print(f'{guest[1]} cant make it.')
guest[1] = 'lili'
print(guest)
print('good news! i found a bigger dinner table.')
guest.insert(0, "leonardo")
guest.append("charles")
####
places= ['"Japan","Italy","Iceland", "Switzerland", "New Zealand"']
print(sorted(places))
####
pizzas = ["pepperoni" , "margarita" , "hawaiian"]
for pizza in pizzas:
    print(f'i like {pizza} pizza.')