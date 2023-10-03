from ToluFunctions import *
greet_user_('tolu', 'joel')
course_ = 'Python for Beginners'
print(course_[:])
# future teller
usr_name = input("Name: ")
usr_age = input('Age: ')
print('hello ' + usr_name + ' you will be ' + str(int(usr_age) + 1) + ' next year')
# future teller(modified)
user_name = input("Name: ")
user_age = int(input('Age: '))
print(f"hello {user_name} you will be {user_age + 1} next year")

#  if and else
# name length validation
name_id = input('Create a User Name: ')
if len(name_id) < 3:
    print('Name is a minimum of 3 characters')
elif len(name_id) > 15:
    print('Name is a maximum of 15 characters')
else:
    print('Name looks good')

# granted loan
has_good_credit = True
has_criminal_record = False
has_high_income = True
if has_good_credit and has_high_income and not has_criminal_record:
    print('Eligible for loan')
else:
    print('''Not eligible for loan

Try getting an higher income and good credit

And if you have ny criminal case just forget''')

# Weight conversion 2(pounds to kilos and otherwise)
weight_ = float(input('Weight: '))
weight_type = input('(L)bs or (K)g: ')
if weight_type.upper() == "L":  # it could also have been weight_type.lower() == "l"
    converted = weight_ * 0.45
    print(f"you weigh {converted} kilograms")
elif weight_type.upper() == "K":
    converted = weight_ / 0.45
    print(f"you weigh {converted} pounds")
else:  # if the weight_type was neither 'k' 'l'
    converted = weight_ * 0
    print(f"you weigh {converted} currently ")
    print("unknown weight type")

# while loop
# guess game
guess_number = 23
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the Number: '))
    guess_count += 1
    if guess == guess_number:
        print('Nice one, won\'t make the next one easy')
        break
else:
    print('Sorry, i made it easy enough, but you decided to fail')

# car game
car_engine = ''
car_started = False
car_name = input('Your car name please: ')
print('GAME STARTED ')
while True:
    car_engine = input("> ").lower()
    if car_engine == 'help':
        print('''
start - to start the car
stop - to stoop the car 
quit - to exit''')
    elif car_engine == 'start':
        if car_started:
            print('Car\'s started already, what were you thinking of?!!')
        else:
            car_started = True
            print('Car started...Ready to go!')
    elif car_engine == 'stop':
        if not car_started:
            print('You\'ve got family problems?, cos you\'ve stopped the car before')
        else:
            car_started = False
            print('Car stopped...')
    elif car_engine == 'quit':
        break
    else:
        print('I don\'t understand that, try typing in "help"...')

# for loop(DON'T UNDERSTAND SHIT)
items = [4, 5, 6]
total = 0
for item in items:
    total += item
    print(f'Total: {total}')# prints out 15

numbers = [2, 2, 2, 2, 5]  # x_count
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# lists
number_in_list = [12, 3, 6, 6, 9, 'john']
list_ = number_in_list[:]
number_in_list.pop()
number_in_list.reverse()
number_in_list.sort()
number_in_list.append(5)
new_list = number_in_list.copy()
print(list_[2:])
number_in_list.clear()
print(new_list)
print(list_)
print(number_in_list)

# finding largest number in a list
list___ = [23, 45, 678754, 845, 1]
greatest_number = list___[2]
for listr in list___:
    if listr > greatest_number:
        greatest_number = listr
print(greatest_number)

# 2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])
for rows in matrix:
    for row in rows:
        print(row)# prints numbers in all lists

# tuple
# tuples are like lists but are written
# with a () rather than a [] and they
# can't be modified  except from finding
# their indexesE.G;
tuple_1 = (1, 2, 3)

# unpacking
coordinates_ = (1, 2, 3)
x_, y_, z_ = coordinates_
print(x_)

# dictionaries
# they are verified with the {curly braces}
customer_1 = {'name': "Tolu Joel", 'age': 15, 'class': 'SSS3A', 'shoe_size': 43, 'is_verified': True,
              'birth_date': 'Dec 19 2005'}
customer_1['name']
print(customer_1.get('hair_color'))
print(customer_1)

# number to words converter
phone_no = input('Phone: ')
phone_ = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
output____ = ''
for ch in phone_no:
    output____ += phone_.get(ch, ' !') + ' '
print(output____)

# emoji converter
message = input('> ')
words = message.split()
emojis = {
    ':)': '😃',
    ':(': '😔'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)


# defining functions
# greet_user function(ToluFunctions-Line_25)
# parameters___square_root function(ToluFUnctions-Line_30)
# keyword arguments___greet_user_ function(ToluFunctions-Line_21)
# emoji converter function(ToluFunctions-Line_9)
# weight_converter function(ToluFunctions-Line_34)
# function that finds the max number in a list(ToluFunctions-Line_1)

# exceptions
try:
    age_ = int(input('Age: '))
    income = 20000
    risk = income / age_
    print(age_)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be zero')

# classes
class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point2 = Point()
point1.x = 20
point1.y = 10
point2.y = 30
point2.x = 56
point1.draw()
point2.move()
print(point1.x)
print(point2.y)
print(point2.y + point1.x)

#
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        print(f'Hi I am {self.first_name} {self.last_name} and i can talk')


tolu = Person('Tolu', 'Joel')
tolu.talk()

bob = Person('Bob', 'Daniels')
bob.talk()

try:
    peerson = Person('hello', 'world')[:]
    peerson.talk()
except TypeError:
    peerson = Person('hello', 'world')
    peerson.talk()

import random
# dice
# my way
class Dice:
    def roll_dice(self):
        dice_numbers = (1, 2, 3, 4, 5, 6)
        dice_numbers2 = (1, 2, 3, 4, 5, 6)
        return random.choices(dice_numbers, dice_numbers2), random.choices(dice_numbers, dice_numbers2)


dice = Dice()
print(dice.roll_dice())


# mosh's way
class Dice:
    def roll_dice(self):
        first_number = random.randint(1, 6)
        second_number = random.randint(1, 6)
        return first_number, second_number


dice2 = Dice()
print(dice2.roll_dice())
