"""Exercise 6-1

Book:    Python Crash Course, 3rd ed. (Eric Matthes)
Reading: Chapter 6
Log:     pcc-06 · Dictionaries

The task, in my own words:
    TODO

What I learned or what tripped me up:
    TODO
"""

# Your code below.
Sam = {
    'name': 'Sam', 'age': 43 , 'country': 'USA'
}
print(Sam['name'])

###
favorite_number = {
    'sarah': 42, 'edward': 23 , 'ali' : 12 , 'eli' : 90
}
for name, number in favorite_number.items():
    print(f'{name}: {number}')
#print( favorite_number['sarah'])
#print(f"sarah favorite number is {favorite_number['sarah']}")
######
rivers = {
    'nile' :'egypt', 'lil' :'shanghai' , 'aras' : 'iran'
}
for river, country in rivers.items():
    print (f"the {river.title()}  runs through {country.title()}.")
for river in rivers:
    print(river.title())
for country in rivers:
    print(country.title())
 ####
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
people = ['jan' , 'edward' , 'tom' , 'anna', 'sarah']
for person in people:
    if person in favorite_languages:
        print(f"thanks for taking the poll, {person.title()}.")
else:
    print(f"{person.title()}, please take the poll.")