"""Exercise 5-3

Book:    Python Crash Course, 3rd ed. (Eric Matthes)
Reading: Chapter 5
Log:     pcc-05 · if Statements

The task, in my own words:
    TODO

What I learned or what tripped me up:
    TODO
"""

# Your code below.
alien_color = 'red'

if alien_color == 'green':
    print('you earned 5 points')

if alien_color == ' yellow':
    print('you earned 10 points')
if alien_color == 'red':
    print('you earned 15 points')
######
age = 20
if age < 2:
    print('your a baby')
elif age >= 2 and age < 4:
    print('your a toddler')
elif age >= 4 and age < 13:
    print('your a kid')
elif age >= 13 and age < 20:
    print('your a teenager')
else:
    print('your aN ELDER')
#######
favorite_fruits = ['apple', 'banana', 'kiwi']
if 'mango' in favorite_fruits:
    print('you really like it')
if 'banana' in favorite_fruits:
    print('you really like it')

#####
names = ['sarah', 'elli', 'lisa' ,'admin' , 'ali']
for greeting in names:
    if greeting == 'admin':
        print('Hello admin')
    else:
        print(f'Hello {greeting} thanks for logging.')

else:
    print('we need some users!!')

#######
current_user = ['sarah', 'ali', 'john', 'elli', 'neli']
new_user = ['sarah', 'goli', 'john', 'admin', 'giso']
for user in new_user:
    if user in current_user:
        print(f' {user} will need to enter new username')
    else:
        print(f' {user} available')

####
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number  == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')




