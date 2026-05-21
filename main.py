# Variable is a container for value it have: (string integers float boolean)

# #string
# we use string with (''; "")
first_name = "Levinho"
activity = "listening to music"
age = "19y"
food = "noodle"
print(f"Hello {first_name}")
print(f"In the free time you like {activity}")
print(f"You are {age}")
print(f"You like {food}")

# Integer
# For an integer we don't use (quote)
quantity = 1
num_of_student = 40
print(f"you buying {quantity}noodles")
print(f"Your class have {num_of_student}students")

# Float
# Float is a number 
price = 299.99
gpa = 90.20
distance = 16
print(f"The price is $ {price}")
print(f"Your gpa is {gpa}")
print(f"You ran for {distance}km")

# Boolean
# We use "Boolean" to create true or false
is_student = True
for_sale = False

if is_student:
    print("Your are a student now")
else:
    print("Your are not a student")

# Typecasting is the process of converting to variable from the data type str(), int(), float(), bool().
name = "Levinho"       #str
age = 19               #Int
gpa = 90.1             #float
is_student = True      #bool
# we can change any variable from str to bool to float or.
# let see the example 
age = str(age)
print(type(age))
# Do the same of this Ex if u wanna change variable from 1 to another 1.

# input() = A function that prompts to enter data 
#           Returns entered data as a string 
name = input("What is your name?: ")
age = input("How old are you?:  ")
age = int(age) # From str to int the easy one, we use this instead "age = int(input(".......")).
age = age + 1
print(f"Hello {name}!")
print("Happy Birthday to you vanntham")
print(f"Your are {age} year old!")

# Exercise 1 Rectangle are calculator.
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

# shopping card programme
item = input ("What item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("How many do you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")

# Mad-lib game 
# word game where you create a story 
# By filling in the Blanks with random words
adjective1 = input("Enter an adjective description: ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective description: ")
verb1 = input("Enter verb that ending with ing: ")
adjective3 = input("Enter an adjective description: ")

print(f"Today i went to a {adjective1} library.")
print(f"When i was sitting there, I saw {noun1}")
print(f"I was very {adjective2}, when i see him!")
print(f"{noun1} was {adjective2} and he is {verb1}")
print(f"I was {adjective3} to see him !")


# New lesson we gonna learn about "Arithmetic Operator, Math function,".

# Friends = 10
# Friends = Friends + 1
# Friends += 1
# friends = friends - 2
# Friends -= 2
# Friends = Friends * 3
# Friends *= 3
# Friends = Friends / 2
# Friends /= 2
# Friends = Friends ** 2
# friends **= 2
# remainder = friends % 3
# print (remainder, Friends)

x = 3.14
y = 4
z = 5
# result = round(x)
# result = abs(y) # "aby" the absolute value of y
# result = pow(4, 3) # It mean 4*4*4=64
# result = max(x, y, z)
result = min(x, y , z)
print(result)

import math 
x = 9
print(math.pi)
print(math.e)
result = math.sqrt(x) # "sqr" = square root.
result = math.ceil(x) # In Python, ceil (short for ceiling) is a function that rounds a number up to the nearest whole number.
result = math.floor(x) #n Python, floor (from the math module) means round a number down to the nearest whole number*. 
print(result)

import math 
x = 10 
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is {round(circumference) ,2 } cm") # ​បរិមាណរង្វង់​​ = Circumference = 2 × π × r

import math 
radius = float(input("Enter the radius of circle: "))
area = math.pi * pow(radius, 2) # ផ្ទៃ​ = Area = π × r²
print(f"The area of the circle is: {round(area, 2)}cm^2")

import math 
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2)) # ពីតាគ៍រ​ = c=a2+b2
print(f"The side = {c}")

# if = Do some code only IF some condition is True
#      Else do something else 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up")
elif age >= 0:
    print("You are not born yet")
elif age >= 1000: # This is not running until you change "age >=100".
    print("You are too old to sign up")
else:
    print("Your are too young to sign up")

# New
response = input("Would you like to have some food? (Y/N): ")

if response == "Y":
    print("Ohh sweetie you got some food here!")
else:
    print("No food for you stupid bastard!")

# New
name = input("Enter your name: ")

if name == "":
    print("You have not enter your name yet!")
else:
    print(f"Hello prime's {name} your are back!")

# Python calculator
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"The {operator} is not valid")

# Python wight converter
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid!")

# Temperature converter
unit = (input("Is this temperature is in Celsius or Fahrenheit (C/F): "))
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1 )
    print(f"The temperature in Fahrenheit is: {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}C")
else:
    print(f"{temp} is not valid!")

# Logical operator = evaluate multiple condition (or , and , not )
#               or = at least one condition must be true 
#              and = both condition must be true 
#              not = inverts the condition (not false , not true)

# How to use "or"
temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("We are going to play football")
else:
    print("We are stay at home")

# How to use "ended"
temp = 30
is_sunny = True

if temp >= 20 and is_sunny:
    print("It is HOT outside🌞")
    print("It is SUNNY☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside❄️")
    print("It is SUNNY☀️")
elif 38 > temp > 0 and is_sunny:
    print("It is WARM outside⛅️")
    print("It is SUNNY☀️")

# Usage of "Not"
if temp >= 20 and not is_sunny:
    print("It is HOT outside🌞")
    print("It is CLOUDY☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside❄️")
    print("It is CLOUDY☁️")
elif 38 > temp > 0 and not is_sunny:
    print("It is WARM outside⛅️")
    print("It is CLOUDY☁️")

# Condition1 expression = A one - line shortcut fo the "if - else" statement (Ternaary operator)
#                          print or assign of two value based on condition
#                          formula = "X if condition else Y"
num = 5 
a = 6 
b = 10 
age = 19
temperature = 16
user_role = "Admin Vantham!"
print("positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 38 else "COULD"
access_level = "Full access" if user_role == "Admin" else "Limited access"

print(result)
print(max_num)
print(min_num)
print(status)

# String Methods
name = input("Enter your username: ")
phone_number = input("Enter your phone number: ")
# result = len(name) # Counting character "we also can put the letter in(" ")" to find.
# result = name.find(" ") # Find the first current space of character.
# result = name.rfind(" ") # last current space.
# result = name.capitalize() # Set the first of smt capital letter. 
# result = name.upper() # All letter is capital.
# result = name.lower() # All letter is lowercase.
# result = name.isdigit # string true if we only enter number(1, 2, 3).
# result = name.isalpha # String true if we only enter the alphabetical = " no space"
# result = phone_number.count("-") # Dashes = "-"
phone_number = phone_number.replace("-", "") # use this for no dashes or with space or no space.


print(phone_number)


# Exercise
# Validate user input 
# 1. User name is no more than 12 character
# 2. Name must not contain space
# 3. Name must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't be more than 12 character")
elif not username.find(" ") == -1:
    print("Your username can't contain space")
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}")


# Indexing = accessing elements of sequence using [] (Indexing operator )
#            [start : end : step]

credit_number = "1234-5678-9456"

print(credit_number[0]) # output '1'
print(credit_number[0:4]) # output '1234'
print(credit_number[0:]) # output all of credit number will appear
print(credit_number[-1]) # output is 6 bc it negative so it count from back 
print(credit_number[::2]) # print second character of a string: ( or we can put it ::3, ::4 or ::n )

last_digits = credit_number[-4:] # show last numbers
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Format specifiers = (value:flags) format a value based on what flags are interested

price1 = 4.4443
price2 = -35505.454
price3 = 4500.45

print(f"Price 1 is ${price1:,.2f}") # 2f...nf use for to cut last number after 0.343
print(f"Price 2 is ${price2:,.2f}") # , use for a lot of number
print(f"Price 3 is ${price3:,.2f}")

# while loop = executed some code WHILE some condition remain true 
#Difference btw if and while 

name = input("Enter your name: ")
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello Gods {name}")

# While use to enter something like we need to do 
# if we enter nothing it will appear again and again like infinite loop but only we enter it 
name = input("Enter your name: ")
# age = int(input("Enter your age: "))
while name == "":
# while age < 0:
    print("You did not entre your name")
    name = input("Enter your name")
#   age = int(input("Enter your age: "))


print(f"Hello Gods {name}")

# infinite loop it run forever we cannot stop and scroll it to see the ended of it 
name = input("Enter your name: ")
while name == "":
    print("You did not entre your name")


print(f"Hello Gods {name}")

# we use "quit" to exit while loop or stop a code to run 

car = input("Enter a name of your favorite cars (q to quit)")

while not car == "q":
    print(f"Your favorite car is {car}")
    car = input("Enter another name of your favorite cars (q to quit)")

print("bye")

# second 
num = int(input("Enter a # between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a # between 1-10: "))

print(f"Your number is {num}")

# Python compound interest calculator

principle = 0
rate = 0 
time = 0 

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle can't be less than  zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than zero")

while time <= 0:
    time = int(input("Enter a time in years: "))
    if time <= 0:
        print("Time can't be less than zero")

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total}.2f")

# for loop = execute blocked of code a fixed number of time.
#            you can iterate over a range, string , sequence , etc
for x in range(1, 20): # range type for count by 2 3 ...n ( 0, 0, 2 or 3 or n....)
    print(x)

print("Happy prime day")


for x in range(1, 30):
    if x == 13:
        continue # use "continue to skip number 13" , and use "break" to count from 1 to 12 not more than 12 
    else:
        print(x)


# Countdown timer program 

import time

my_time = int(input("Enter your time in seconds: "))

for x in range(my_time, 0, -1): # reversed function need to use "range(0, my_time):"
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x % 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("It on time for you!")

# Nested loop = a loop within another loop(outer, inner)
#              outer loop:
#                inner loop:


for x in range(1, 10):

    print(x, end="") 
# use (end="") to make straight line 
# # you can put (dashes- or space in "- or ")

# To repeat that loop 

for x in range(3): # outer loop 
    for y in range(1, 10): # inner loop 
        print(y, end= " ")
    print() # use this if you don't want straight line


# Rows and Columns of rectangle 

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
# Straight line we call "columns"
# Down line we call "Rows"


# Collection = single "variable" used to store multiple value
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} understood and immutable, but Add/remove OK. No Duplicates
#   Tuple = () ordered and unchangeable. Duplicate OK FASTER 



cars = ["BMW", "AUDI", "LAMBORGHINI", "BUGATTI","FERRARI"]

# Description methods
# print(dir(cars))
# print(help(cars))
# print(len(cars))
print("BMW" in cars) # It true because BMW have in cars[], not true if smt is not in []

# To change values we use 
cars[0] = "TOYOTA" # it will print TOYOTA instead of BMW.
car.append("MECERDEZ") # append mean append means “add something to the end of a list.”
car.remove("BMW")
car.insert("LAMBORGHINI")
car.sort() # alphabetical order 
car.clear() # delete all the element
car.add("MOTOR")
car.pop() # Random remover

print(car.index("BMW")) # To find index
print(car.count("LAMBORGHINI")) # To count sth in element 

# print(cars[0])
for cars in cars:
   print(cars)


# Shopping card program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy ( q to quite): ")
    if food.lower() == "q":
        break

    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("-----YOUR CARD ------")
for food in foods:
    print(food, end= " ")

for price in prices:
    total += price

print() # New line 
print(f"Your total is : $ {total}")


# 2D collection 

groceries = [("BMW", "LAMBO", "FERRARI", "BUGATTI"),
             ("VASPA", "SCOOPI", "PG-1", "DIO", "CLICK"),
             ("KAWASAKI NINJA H2R", "BMW S1000RR", "DUCATI PANIGLE V4")]


for collection in groceries:
    for transportations in collection:
        print(transportations, end=" ")
    print()

# Exercise = " create two demensional keypad"

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# Python quiz game 

questions = ("What is her favorite colors?: ", 
            "How old is she?: ", 
            "Who's her boyfriend?: ", 
            "What grade is she study in?: ")

options = (("A. ❤️💛💚", "B. 💙💜🧡", "C. 💜💙💛", "D. 💖🌸💜"), 
          ("A. 17", "B. 16", "C. 18", "D. 19"), 
          ("A. JAME", "B. RONALDO", "C. VANNTHAM", "D. FINN"), 
          ("A. 9", "B. 11", "C. 12", "D.2"),)

answers = ("D", "A", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print(f"INCORRECT")
        print(f"{answers[question_num]} is CORRECT answer")
    question_num += 1

    print("-----------------------------")
    print("             RESULT          ")
    print("-----------------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

score = int(score / len(questions) * 100)
if score == len(questions):
      print(f"Your score is: {score}%")
elif score >= 90:
    print("Grade: A - Amazing you got one kiss from her!")
    print(f"Your score is: {score} ♾️ 🎉!")
elif score >= 80:
    print("Grade: B - Great Job you got an Aura 💫 !")
elif score >= 70:
    print("Grade: C - Not bad chill 4ever 😗 ! ")
elif score >= 60:
    print("Grade: D - Try it more keep moving 🏃 !")
elif score >= 50:
    print("Grade: E- Keep practising 😖 !")
else:
    print("Grade: F - You got smash from her lol 💥 !")


# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. duplicates

capitals = {"USA": "Washington D.C.", 
                "CAMBODIA": "Phnom Penh ", 
                "UK": "New York N.Y. ", 
                "RUSSIA": "Moscow"}

# print(dir(capitals))
#print(help(capitals))

print(capitals.get("USA"))
if capitals.get("Japanese"):
    print("That capital is exist")
else:
    print("The capital is not exist")

print(capitals)

capitals.update({"USA": "Detroit"}) # use to update information
capitals.pop("UK") # Remove only uk
capitals.popitem() # Remove the last one 
capitals.clear()   # remove all 

# keys = capitals.keys() # key is an object 
# for key in capitals.keys():
#  print(keys)

# you can use for loop to iterate over every key that is return from the key methods of your dictionary

# values = capitals.values()
# if value in capitals.values():
#    print(values)

# "item" : is return a dictionary object which is resembles a 2D list of tuples
items = capitals.items
for key, value in capitals.items():
    print(f"{key}: {value}")


# concession stand program

menu = { "BMW": 70,
             "LAMBO": 100,
             "BUGGATI": 150,
             "FERRARI": 90,
             "AUDI": 60
             }

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: $M{value:.2f}")
print("--------------------------")

while True:
    car = input("What cars would you like to buy (q to quit): ").upper()
    if car == "q":
        break
    elif menu.get(car) is not None:
        cart.append(car)

    print(cart)


print("------YOU HAVE BUY------")
for car in cart:
        total += menu.get(car)
        print(car, end=" ")
print()
print(f"The total is $M{total:.2f}")


# Ai style 

menu = {
    "BMW": 70,
    "LAMBO": 100,
    "BUGGATI": 150,
    "FERRARI": 90,
    "AUDI": 60
}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: $M{value:.2f}")
print("--------------------------")

while True:
    car = input("What car would you like to buy (q to quit): ").upper()

    if car == "Q":
        break

    if car in menu:
        cart.append(car)  # correct append
        print(f"Added {car} to cart.")
    else:
        print("Car not found in menu — try again.")

print("\nYour Cart:", cart)

for car in cart:
    total += menu[car]

print(f"Total: $M{total:.2f}")


# Number guessing games
import random 

lowest_num = 1 
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please Select a number between {lowest_num} and {highest_num}")
        
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"COORECT! The answer was {answer}")
            print(f"Number of guess: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Plese Select a number between {lowest_num} and {highest_num}")


# Shuffle game
import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card = random.shuffle(cards)

print(cards)

# Choice games 

# choice game
import random
options = ("rock", "paper", "scissors")

running = True


while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")


    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You won!")
    elif player == "paper" and computer == "rock":
        print("You won!")
    elif player == "scissors" and computer == "paper":
        print("You won!")
    else:
        print("You lose!")

    # play_again = input("Play again? (y/n): ").lower() 
    # if not play_again == "y": # use not if the player don't want to play again
        # running = False
    # Or we can use 
    if not input("Play again? (y/n): ").lower() == "y":
        running = False


    print("Thanks for playing!")

# dice roller program
# ASI unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
import random 

# ● ┌ ─ ┐ │ └ 

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"


dice_art = {
    1 : ("┌─────────┐", 
         "│         │", 
         "│    ●    │", 
         "│         │", 
         "└─────────┘"),
    2 : ("┌─────────┐", 
         "│  ●      │", 
         "│         │", 
         "│       ● │", 
         "└─────────┘"),
    3 : ("┌─────────┐", 
         "│  ●      │", 
         "│    ●    │", 
         "│       ● │", 
         "└─────────┘"),
    4 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│         │", 
         "│  ●   ●  │", 
         "└─────────┘"),
    5 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│    ●    │", 
         "│  ●   ●  │", 
         "└─────────┘"),
    6 : ("┌─────────┐", 
         "│  ●   ●  │",  
         "│  ●   ●  │", 
         "│  ●   ●  │",  
         "└─────────┘")
}
 
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#       print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")


# foucntion 

def greet(name):
    print("Damm bro!", name)

greet("Vanntham!")


def total_price():
    return 5 + 3 # if not use return so the ouput will be none value

def calculate_tax():
    return "10 USd"

# calling 
x = 10
x = calculate_tax()
x = total_price()

print(f"${x}")
print(calculate_tax)



# 
pi = 'global'
def bigger():
    pi = 'enclose'
    def smaller():
     nonlocal pi # n Python, nonlocal means:

#                 Use a variable from the nearest enclosing function (not global).

#                It allows a nested function to modify a variable that belongs to its outer function.
     print(pi)
     pi = 'local'

    smaller()
    print(pi)

bigger()

# Founction = A block of reusable code
#             place () after the fouction name to invoke it 

def happy_birthday(name, age):
    print(f"Happy birthday to you {name}!")
    print(f"Your are {age} year old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Vanntham", 20)
happy_birthday("Sengly", 19)
happy_birthday("levinho", 20)

# Another example 

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of $ {amount:.2f} is due: {due_date}")

display_invoice("levinho", 1500.90, "01/19")

# return = statemnt used to end a function
#          and send a result back to the caller



def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(10, 5))

#
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Thieng", "vanntham")
print(full_name)

#

def create_name(surname, nickname):
    surname = surname[0].upper() + surname[1:]
    nickname = nickname[0].upper() + nickname[1:]
    return surname + " and " + nickname

surname = "vanntham"
nickname = "levinho"

print(create_name(surname, nickname))


# default = A default value for certain parameters
#           default is used what that argument is omitted
#           make your function more flexuble, reduces # of arguments
#           1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(600))
# print(net_price(500, 0.1, ))
print(net_price(500, 0.1, 0))

# default = A default value for certain parameters
#           default is used what that argument is omitted
#           make your function more flexible, reduces # of arguments
#           1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

import time
def count(start, end): # non- default argument (start=0, end+1)
 #                       change it to (end, start=0)
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0, 15) # or count(15) for non- def
# count(30, 15) or we can change to start with 15


# keyword arguments = an argument procceded by indentifier
#                     help with readability 
#                     order of arguments doesn't matter
#                  1. positional 2. default 3. KEYWORD 4. arbitrary

# python keyword = (
# if, else, elif, for, while, def, return, class,
# import,from,
# True,False,None,and,or,not
# )
# how to see al keywords python
# import keyword
# print(keyword.kwlist)


def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Prime", "Thieng", "Vanntham")
# Or we can change the value place [ 'hello("Hello", title ="Prime", last ="Vanntham", first="Thieng") ']
# what ever you want 

for x in range(1, 5):
    print(x, end=" ") # use (end=" ") for straight line or space 
#                      wihtout space no need to space in (end="")

print("1", "2", "3", "4", "5", sep="-") # add dashes (-)


# function to generate phone number

def get_phone(country, area, first, last):
    return f"{country}--{area}--{first}--{last}"

phone_num = get_phone(country=855, area=089, first=427, last=847)

print(phone_num)

# *args and **kwargs
# *args    = allow you to pass multiple non-key arguement OR *args is aguement
# **kwargs = allow  you to pass multiple keyword-arguement OR **kwargs is keyword arguement
#           * unpacking operator
#           1. positional 2. default 3. keyword 4. ARBITRARY

# *args
def add(*args): # or you can change it to (*num)
    total = 0
    for arg in args:
        total += arg
    return total
    
print(add(1, 2)) # output will plus number in ()

#

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Prime", "Vanntham", "Tyrann")
print()

# **kwargs
def print_address(**kwargs):
    for key, value in kwargs.items(): # display key value
    # for value in kwargs.values():
        print(f"{key}: {value}")

print_address(Street="168", # key in address
              Songkat="labanseak", 
              district="Ochum", 
              province="Ratanakiri", 
              City="Banlung")

# Exercise use *args + **kwargs
def shipping_label(*args, **kwargs): # we can't add **kwargs be fore args
    for arg in args:             # (**kwargs, args) error syntax
        print(arg, end=" ")
    print()

    if "apt" in kwargs: 
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('continent')} {kwargs.get('countries')} {kwargs.get('zip')}")
# If we didn't use if elif statement and the keyword don't have in
# value so the output will be none 
# example : shipping_label("Prime", "vanntham",
# street=0111)
# 
        
                                   
shipping_label("Mr", "Renn-Je", "Levinho", 
               street="165",
               apt="#90",
               continent="United kingdom",
               countries="England",
               zip="3700")

# Iterable = An object/collection that can return its elements one at a time
#             allowing it to be interate over in a loop 

# 1. Tuple ()
numbers = (1, 2, 3, 4)

for number in numbers: # or you can reversed(number)
    print(number)

# 2. Set {}
# for set we can't reversed
drinks = {"coffee", "juice", "coca","milk"}

for drink in drinks:
    print(drink)

# 3. String ""
# name = "Sika Nita"
# for character in name:
#    print(character, end=" ")

# 4. dictionaries the most complicated {} same set 
#    but each element is a key value pair
my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(key, value) # display both (key and value) print(f"{key} = {value}")
# for key in my_dictionary: # display (key)
# for value in my_dictionary.value(): # display (value)

# Membership operators = used to test whether a value or variable is found in sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in 

word = "APPLE"
letter = input("Guess a letter in the secret word: ")

if letter  in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

# set 
students = {"Vanntham", "Levinho", "Nita"}

student = input("Enter a name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

# reverse version
# students = {"Vanntham", "Levinho", "Nita"}

# student = input("Enter a name of a student: ")

# if student not in students:
#    print(f"{student} was not found")
# else:
#    print(f"{student} is a student")

# Dictionaries of grade
grades = {"Vanntham": "A", 
          "Levinho": "A", 
          "Nita": "A+"}

student = input("Enter a name of a student: ")

if student in grades:
    print(f"{student}'s grade is ")
else:
    print(f"{student} was not found")

#
email = "vanthamtyrano@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

# List comprehension = A concise way to create lists in python
#                      compact and easier to reas than traditional loops
#                     [expression for value in iterable if condition]

# with list 
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

#
# formula = doubles = [expression for value in iterable if condition]
#                     [x * 2]     for x in range(1, 11)]

doubles = [x * 2 for x in range(1, 11)] # Double = mutiple by 2
triple = [y * 3 for y in range(1, 11)]  # Triple = mutiple by 3
squares = [z * x for z in range(1, 11)] # Squares = muultiple by itself
print(squares)

# with string 
drinks = ["matcha", "green tea", "coffee", "ice latte"]
drinks = [drink.upper() for drink in drinks]
drinks_char = [drink[0] for drink in drinks] # letter of drink with index "0"
print(drinks)
print(drinks_char)

# Now work with if condition
numbers = [1, -2, 3, -4, 5, -6, -7, 8]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num > 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(even_nums)

# 
grades = [90, 84, 50, 41, 39, 70, 60]
passing_grade = [grade for grade in grades if grade >=50]

print(passing_grade)

# match - case statement (switch): An alternative to using many 'elif' statement
#                                  Excute some code if a value match 'case'
#                                  Benefits: cleaner and syntax is more readable

# elif statement 
def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Wednesday"
    elif day == 4:
        return "It is Thursday"
    elif day == 5:
        return "It is Friday"
    elif day == 6:
        return "It is saturday"
    else:
        return "Not a valid day"
    
# use match - case
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is saturday"
        case 7:
            return "It is sunday"
        case _:
            return "Not a valid day"
        
print(day_of_week(4))

  # Find weekend day 
def is_weekend(day):
    match day:
        case "Saturday" | "sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thurday" | "Friday":
            return False
        case _:
            return False
    
print(is_weekend("pizza"))
        
# module = a file constaining codse you want to include in your program
#          use 'import' to include module (built-in or your own)
#          useful to break up a large program reusable separate files

# import example

# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
# result = example.area(3)

# print(result)
# print(help("modules"))

# variable scope = where a variable is visible and accessible in 
# scope resolution = (LEDGB) local -> Enclosed -> Global -> Built-in

#  variable scope                  
def func1():
    a = 1 
    print(a)

def func2():
    b = 2
    print(b)
# invoke the functions
func1()
func2()
# If we use the same variable name (x) in different functions, they will not interfere with each other because they are in different scopes. Each function has its own local scope, so the variable x in func3 is different from the variable x in func4.
def func3():
    x = 3
    print(x)

# 3 Local scope
def func5():
    x = 1
    print(x)
    def func6():  # Output is 1 and 8
        x = 8
        print(x)
    func6()

func5()
# 4 Enclosed scope
def func7():
    z = 100

    def func8(): # Output is 100 because in func8, don't have the value of Z, so it will look for the value of Z in the outer scope, which is func7, and it will find the value of Z as 100.
        print(z)
    func8()

func7()

# 5 Global scope meaning outside of all functions
def func9():
    # no local version of x
    print(x)

def func10():
    # no local version of x
    print(x)

# global variable
x = 200  # out put is 200 with both func9 and func10 because they will look for the value of x in the global scope, and they will find the value of x as 200.

func9()
func10()

# Built-in scope
from math import e

def func11():
    print(e) # Output is 2.718281828459045 because e is a built-in constant in the math module, and it is accessible in the built-in scope.

e = 3 # The output is 3 instead of "e math constant" because we have defined a global variable e with the value of 3, and it will override the built-in constant e in the math module when we call func11().

func11()

# if __name_ == "_main_": (this script can be imported OR run standalone)
# Function and classes im this module can be reused without the main block of code executing
# Good practice (code is modular,
#                help readability,
#                leave no global variables,
#                avoid unintended execution)

#                EX, library = import library for functionality
#                              when running library directly, display page


# Python Banking program
# 1. Show Balance
# 2. Deposit
# 3. Withdraw

def show_balance():
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print("That not a valid amount. Please enter a positive number.")
        return 0 # return something to stop the function
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero.")
        return 0
    else:
        return amount
balance = 0
is_running = True

while is_running:
    print("Welcome to banking program!")
    print("1. show balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice. Please try again.")

print("Thank you! Have a nice day!👋")


# use Enclose scope 

def show_balance(balance):
    print("************************************")
    print(f"Your current balance is ${balance:.2f}")
    print("************************************")

def deposit():
    print("************************************")
    amount = float(input("Enter the amount to deposit: "))
    print("************************************")

    if amount < 0:
        print("************************************")
        print("That not a valid amount. Please enter a positive number.")
        print("************************************")
        return 0 # return something to stop the function
    else:
        return amount

def withdraw(balance):
    print("************************************")
    amount = float(input("Enter amount to withdraw: "))
    print("************************************")

    if amount > balance:
        print("************************************")
        print("Insufficient funds.")
        print("************************************")
        return 0
    elif amount < 0:
        print("************************************")
        print("Amount must be greater than zero.")
        print("************************************")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
       print("************************************")
       print("*    Welcome to banking program!*   ")
       print("************************************")
       print("1. show balance")
       print("2. deposit")
       print("3. withdraw")
       print("4. exit")
       print("************************************")

       choice = input("Enter your choice (1-4): ")

       if choice == "1":
           show_balance(balance)
       elif choice == "2":
           balance += deposit()
       elif choice == "3":
           balance -= withdraw(balance)
       elif choice == "4":
           is_running = False
       else:
           print("************************************")
           print("Invalid choice. Please try again.")
           print("************************************")
    print("************************************")
    print("Thank you! Have a nice day!👋")
    print("************************************")

if __name__ == "__main__":
    main()


# python slot machine 
import random

def  spin_row():
    symbols = ['🍕', '🍔', '🍟', '🌭', '🍿']

    # results = []
    #for symbol in range(3): # this for loop will iterate 3 time
    #    results.append(random.choice(symbols))
    #return results
    # pro code 
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍕':
            return bet * 3
        elif row[0] == '🍔':
            return bet * 4
        elif row[0] == '🍟':
            return bet * 5
        elif row[0] == '🌭':
            return bet * 10
        elif row[0] == '🍿':
            return bet * 20
    return 0

    

def main():
    balance = 10000

    print("************************")
    print("Welcome to python slot!")
    print("Symbol: 🍕 🍔 🍟 🌭 🍿")
    print("************************")

    while balance > 0:
        print(f"Your current balance is ${balance}")
        
        bet = input("Place your bet amount:")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue # use continue keyword will skip the current iteration of this loop
                     # and start from the beginning
        
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("spinning....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round!")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N):").upper()

        if play_again != 'Y':
            break

    print("*******************")
    print(f"Game over! Your final balance is ${balance:.2f}")
    print("*******************")

if __name__ == "__main__":
    main()


# Encryption program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")

# encrypt
plain_text= input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypt message  : {cipher_text}")

# Decrypt
cipher_text_input= input("Enter a message to decrypt: ")
decrypted_text = ""

for letter in cipher_text_input:
    index = key.index(letter)
    decrypted_text += chars[index]

print(f"encrypt message  : {cipher_text_input}")
print(f"original message : {decrypted_text}")

# Hangman game in python
# from word-list import words
import random

words = (
    "toyota", "honda", "ford", "bmw", "audi",
    "nissan", "mazda", "hyundai", "kia", "chevrolet",
    "mercedes", "volkswagen", "tesla", "lexus",
    "porsche", "ferrari", "lamborghini", "mitsubishi",
    "aston-martin",

    "civic", "corolla", "camry", "accord", "mustang",
    "ranger", "prius", "supra", "golf"
)

# dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\"
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

def display_man(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses) # begin the game 
        display_hint(hint) # represent the answer we gave to guess

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha: # use for guess only 1 alphabet and not a number
            print("Invalid input")
            continue
        
        if guess in guessed_letters: # for a execute when the letter is already guess no second time 
            print(f"{guess} is already guess")
            continue

        guessed_letters.add(guess)
            
      # we put if in while loop
        if guess in answer:
           for i in range(len(answer)):
               if answer [i] == guess:
                   hint[i] = guess
        else:
            wrong_guesses += 1
        if "_" not in  hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False
        


if __name__ == "__main__":
    main()

# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book 
#          You need a "class" to create many objects
# Attributes = variables that belong to an object or a class
# class = (blueprint) used to design the structure and layout of an object 
# 3. Attributes vs Methods (data vs behavior)
# Type	What it is	Example
# Attribute : Stores data	self.brand
# Method	: Does something	def drive()

# folder 1
from car import Car

car1 = Car("BMW", 2025, "blue", False)
car2 = Car("Lamborghini", 2026, "black", True)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

# car2.drive()
# car2.stop()
car2.describe()

# folder 2
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


# class variables = shared among all instance of a class
#                   Defined outside the constructor 
#                   Allow you to share data all objects create form that class

class Student: 

    class_year = 2026
    num_students = 0

    def __init__(self, name, age ):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Levin", 19)
student2 = Student("Nita", 17)
student3 = Student("Vanntham", 19)
student4 = Student("Tra", 21)

# print(student1.name)
# print(student2.age)
# print(student2.name)
# print(student2.age)
# print(student2.class_year)
# print(Student.class_year)
# print(student1.name, student1.age)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

# Inheritance = Allow a class to inherit attributes and methods from another class
#               Help with code reusability and extensibility
#               class Child(parent)

# Simple real-life idea

#      Person → name, age

#      Student → person + student_id

#      Teacher → person + salary

# parent class
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

# children class
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Bennie")
cat = Cat("Bob")
mouse = Mouse("Eri")

# print(dog.name)
# print(dog.is_alive)
dog.speak()
dog.sleep()

# 1. multiple inheritance = inherit more than one class 
#                        C(A, B)

# 2. multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <= B(A) <= A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
class Prey(Animal):  
    def flee(self):
        print(f"{self.name} is fleeing")
#              Prey and predator is parent class 
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass
#              Hawk and fish is children class
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Tom")
hawk = Hawk("John")
fish = Fish("Nemo")

fish.hunt() # in hunt 
fish.flee() # in prey
rabbit.hunt() # error because rabbit is in prey 

# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allow you to extend the functionality of the inheritance methods
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super() .__init__(color, is_filled)
        self.width= width

    
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=4)
triangle = Triangle(color="black", is_filled=True, width=6, height=7)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

square.describe()


# Polymorphism = Greek word that mean to "have any forms or faces"  
#                Poly = Many 
#                Morphe = Form
#                TWO WAY TO ACHIEVE POLYMORPHISM
#             1. Inheritance = An object could be treat of  the same type as a parent class
#             2. "Duck typing" = Object must have necessary attribute / method

 # 1 . Inheritance
from abc import ABC, abstractmethod

class Shape:
   @abstractmethod

   def area(self):
       pass
   

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base 
        self.height =  height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
       

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()} cm^2")

# "Duck typing" = Another to way to achieve polymorphism besides the Inheritance
#                 Object must have the minimum necessary attributes / methods
#                "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEW!")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)


# static methods = A method that belong to th class rather than any object from that class (instance)
#                  Usually used for general utility function 

# Instance methods = Best for operation on instances of the class (objects)
# Static methods   = Best for utility functions that do not need access to the class 

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer,", "Cyber security"]
        return position in valid_positions

employee1 = Employee("Levin", "Developer")
employee2 = Employee("Nita", "Manager")
employee3 = Employee("Randy", "Cybersecurity")


print(Employee.is_valid_position("Developer"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

# Class methods = Allow operations related to the class  itself 
#                 Take (cls) as the first parameter, which represents the class itself.
# Instance methods = Best for operations on instance of the class (Object)
# Static methods   = Best for utility function that do not need to the class itself
# Class methods    = Best for class-level data or require access to the class itself
class Student:
    count = 0 
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa


    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total # of student: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Nita", 9.0)
student2 = Student("Levin", 8.9)
student3 = Student("Randy", 10.0)

print(Student.get_count())
print(Student.get_average_gpa())

# Magic methods =  Dander methods (double underscore) __init__, __str__, __eq__
#                  They are automatically called by many of python's built-in operation.
#                  They allow developers to define or customize the behavior of objects

    
class Book:
    def __init__(self, title, author, num_page):
        self.title = title
        self.author = author
        self.num_page = num_page

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_page < other.num_page
    

    def __add__(self, other):
        return f"{self.num_page + other.num_page} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_page":
            return self.num_page
        else:
            return f"key '{key}' was not found"

book1 = Book("The legendary Levin", "S.K.I Nita", 304)
book2 = Book("My love", "T.G Vanntham", 278)
book3 = Book("An Emotional", "R.D.Y Levin", 213)

# print(book1)
# print(book1 == book2)
# print(book2 > book3)
# print(book1 + book2)
# print("Levin" in book3)
# print(book1['title'])
# print(book2['author'])
# print(book1['num_page'])
print(book3['Prime'])


# @property = Decorate used to define a methods as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter # to write
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter # to write
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter # To delete width
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter # To delete height
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 7

print(rectangle.width)
print(rectangle.height)

del rectangle.width # delete
del rectangle.height # delete

# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function 
#             Pass thr base function as an argument to be decorate

def add_sprinkles(func): # Decorator
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊 *")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func): # Decorator
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫 *")
        func(*args, **kwargs)
    return wrapper

# Base function
@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor}ice cream 🍦")

get_ice_cream("chocolate")

# exception = An event that interrupt the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#             1. Try, 2. except, 3. finally


try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only number please!")

except Exception:
    print("Something went wrong!")
finally: # Execute
    print("Do some clean up here!")

# Python file detection

import os

file_path = "C:/Users/DELL/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("That location doesn't exist")


# Python writing file (.txt, .json, .csv)

# 1. txt file writing
employees = ["Nita", "Levin", "Vanntham"]
text_data = "I love Nita!"

# file_path = "output.txt"
file_path = "C:/Users/DELL/Desktop/output.txt" # to generate the file within the same folder

# with open(file=file_path, mode="w") as file: "w = Write file"
# # with open(file_path, "w") as file: "a = Append"
# with open(file=file_path, mode="x") as file: "x = create"
try:
    with open(file_path, "a") as file: # w = write a file
       for employee in employees:
           file.write(employee + "\n")
       print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exist!")

# 2. json file writing
import json
employee = {
    "name": "Nita",
    "age": 17,
    "job": "Accounting"
}

file_path = "C:/Users/DELL/Desktop/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4) # indent = add key value and number of key value is space
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# 3. csv file writing
import json
import csv
employees = [["name", "age", "job"],
            ["Levin", 18, "Web Developer"],
            ["Nita", 17, "Cyber Security"],
            ["Vanntham", 19, "Software Developer"]]

file_path = "C:/Users/DELL/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# Python reading file (.txt, .json, .csv)

# txt file reading
file_path = "C:/Users/DELL/Desktop/input.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read this file")

# Json file reading
import json

file_path = "C:/Users/DELL/Desktop/input.txt"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You have no permission to read that file")

# csv file reading

import csv

file_path = "C:/Users/DELL/Desktop/input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file) # give a memory address
        for line in content:
            print(line[0]) # output =  name 
            print(line[1]) #           age
            print(line[3]) #           job
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You have no permission to read that file")

# Date and time
import datetime

date = datetime.date(2026, 3, 14)
today = datetime.date.today()

time = datetime.time(1, 0, 0)
now = datetime.datetime.now()

# format appearance of the string
now = now.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2030, 3, 14, 1, 0, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("target day has NOT passed")


# Python alarm clock
# Not yet test sound because it can work on python old version 

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP 😖")
            
            # Noted
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False



        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

# multithreading = used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bund tasks like reading file or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time 

def walk_with_girlfriend(first, last):
    time.sleep(8)
    print(f"You finish walking with {first} {last}")

def take_photo():
    time.sleep(4)
    print("You take a photo")

def get_call():
    time.sleep(5)
    print("You get a call")

# Noted = def 1 it spent 8 second 
# Then it will continue to df 2 and 3 with the S that we put

# walk_with_girlfriend()
# take_photo()
# get_call()

# To complete it in order one by one we use "Chore"
chore1 = threading.Thread(target=walk_with_girlfriend, args=("Dream", "Girl"))
chore1.start()

chore2 = threading.Thread(target=take_photo)
chore2.start()

chore3 = threading.Thread(target=get_call)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete !")


# Connect to API

import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {name}. Status code: {response.status_code}")

    pokemon_name = "pikachu"
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"{pokemon_info['name']}.capitalize()")
        print(f"{pokemon_info['height']}")
        print(f"{pokemon_info['weight']}")
        print(f"{pokemon_info['id']}")
        
       
# PyQt5 Graphic User Interface (GUI) Application Template

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QtIcon

def MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My love languages")
        self.setGeometry(100, 100, 600, 400) # (x, y, width, height)
        self.setWindowIcon(QtIcon("IMG_3939.JPG")) # Set your own icon path here

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())


# PyQt5 Labels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 500)
        label.setStyleSheet("color: red;"
                            "background-color: yellow;"
                            "font-weight: bold;"
                            "border-radius: 10px;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":    
    main()


# PyQt5 images
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("profile_pic.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True) # Scale the image to fit the label

        label.setGeometry(self.width - label.width(), # For the bottom left corner we will set x to 0 
                           self.height - label.height(), # Bottom right corner
                           label.width(), 
                           label.height())
        
        # label.setGeometry(self.width - label.width()) //2, 
                           # self.height - label.height()) //2, # image the middle of window
                           # label.width(), 
                           # label.height())


       
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":    
    main()    


# Pyqt5 layouts

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout


class MainWindow(QMainWindow):  # parent class
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: pink;")
        label4.setStylesheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        vbox = QVBoxLayout(central_widget)  # You can change it to "hbox"
                                            # h = ឈរ and v = ដេក
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

 # For Grid
        # grid = QGridLayout()
        # grid.addWidget(label1, 0, 0) # ( label, row, column)
        # grid.addWidget(label2, 0, 1)
        # grid.addWidget(label3, 1, 0)
        # grid.addWidget(label4, 1, 1)
        # grid.addWidget(label5, 1, 2)

        central_widget.setLayout(vbox)



def main():
    app = QApplication(sys.argv)  # app object
    window = MainWindow()  # window object
    window.show()
    sys.exit(app.exec_())  # exec = execute


if __name__ == "__main__":
    main()


# PyQt5 Button

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click Me", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        # print("Button clicked!")
        # self.button.setText("Clicked!")
        # self.button.setDisabled(True) # Disable the click method
        self.label.setText("Goodbye") # When tap click the word will appear 

       
   
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# PyQt5 Button

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you love me?", self)
        self.initUI()

    
    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # print(state) # state value of 2 = checked, 0 = unchecked
        if state == Qt.Checked:
            print("You love me!")
        else:
            print("You DON'T LOVE me!")
       

   
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



# PyQt5 Radio buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        # Payment type 
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        # Payment method
        self.radio4 = QRadioButton("In-Stored", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()


def initUI(self):
    self.radio1.setGeometry(0, 0, 300, 50)
    self.radio2.setGeometry(0, 50, 300, 50)
    self.radio3.setGeometry(0, 100, 300, 50)
    self.radio4.setGeometry(0, 150, 300, 50)
    self.radio5.setGeometry(0, 200, 300, 50)

    # Apply style to the entire group of radio buttons
    self.setStyleSheet("QRadioButton{"
                       "font-size: 40px;"
                       "font-family: Arial;"
                       "padding: 10px;"
                       "}")
    
    self.button_group1.addButton(self.radio1)
    self.button_group1.addButton(self.radio2)
    self.button_group1.addButton(self.radio3)
                                 
    self.button_group2.addButton(self.radio4)
    self.button_group2.addButton(self.radio5)

    self.radio1.toggled.connect(self.radio_button_changed)
    self.radio2.toggled.connect(self.radio_button_changed)
    self.radio3.toggled.connect(self.radio_button_changed)
    self.radio4.toggled.connect(self.radio_button_changed)
    self.radio5.toggled.connect(self.radio_button_changed)

def radio_button_changed(self):
    radio_button = self.sender() # sender method returns the widget that sent the signal, in this case the radio button that was toggled
    if radio_button.isChecked():
        print(f"{radio_button.text()} is selected")


if __name__ == "__main__":    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# PyQt5 LineEdits

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100,40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name")
        
        self.button.clicked.connect(self.submit)

        def submit(self):
           text = self.line_edit.text()
           print(f"Hello {text}!")


if __name__ == "__main__":    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



# PyQt5 setStyleSheet

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,  QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
       
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)
        
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

# Greater variety of color you can search "color picker" in google and copy the hex code of the color you want to use
        self.setStyleSheet("""
                           QPushButton{
                               font-size: 40px;
                               font-family: Arial;
                               padding: 15px 75px;
                               margin: 25px;
                               border: 3px solid #555;
                               border-radius: 15px;
                           }
                           QPushButton#button1{
                               background-color: hsl(136, 57%, 44%);
                           }
                           QPushButton#button2{
                                background-color: hsl(311, 69%, 64%);
                           }
                           QPushButton#button3{
                               background-color: hsl(182, 57%, 51%);
                           }
                           QPushButton#button1:hover{
                               background-color: hsl(136, 57%, 84%);
                           }
                           QPushButton#button2:hover{
                                background-color: hsl(311, 69%, 84%);
                           }
                           QPushButton#button3:hover{
                               background-color: hsl(182, 57%, 84%);
                           }
                           """)


if __name__ == "__main__":    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# Python PyQt5 Digital Clock Example

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(130, 90%, 32%);")

        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
  

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


# Python PyQt5 Stopwatch Example

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0) # hours, minutes, seconds
        self.time_label = QLabel("00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;

            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(278, 83%, 52%);
                border-radius: 20px;
                }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10) 

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time())

    def format_time(self):
        hour = self.time.hour()
        minute = self.time.minute()
        second = self.time.second()
        millisecond = self.time.msec() // 10
        return f"{hour:02}:{minute:02}:{second:02}:{millisecond:02}"

    def update_display(self):
      self.time = self.time.addMSecs(10)
      self.time_label.setText(self.format_time())  # No extra arg


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())


# Python Weather API Example

import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.city_input.setObjectName("city_input")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Arial;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 30px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: "Segoe UI Emoji";
            }
            QLabel#description_label{
                font-size: 50px;
            }
            """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        api_key = "3aa69a23bbba1ed4c5e6af082631f166"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nInvalid API key")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API")
                case 403:
                    self.display_error("Forbidden:\nAccess is Denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error(
                        "Internal server:\nPlease try again later")
                case 502:
                    self.display_error(
                        "Bad Gateway:\nInvalid response from server")
                case 503:
                    self.display_error("Server Unavailable:\nServer is down")
                case 504:
                    self.display_error(
                        "Gateway Timeout:\nNo responses from the server")
                case _:
                    self.display_error("HTTP error accured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error(
                "Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request time out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirect:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error("Request error")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px")
        temperature_K = data["main"]["temp"]
        temperature_C = temperature_K - 273.15
        temperature_F = (temperature_K * 9/5) - 459.67
        # print(temperature_K)
        # print(temperature_C)
        # print(temperature_F)
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_C:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return " "

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())