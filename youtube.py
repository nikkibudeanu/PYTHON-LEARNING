# PYTHON-LEARNING - youtube video https://www.youtube.com/watch?v=rfscVS0vtbw

# variables

character_name = "John"
character_age = "35"
print("There once was a man name "+ character_name +",")
print("he was"+ character_age+" years old.")
print("He really liked the name" + character_name+",")
print("but didn't like being "+ character_age+".")

# strings
print("Giraffe\nAcademy")
phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.isupper())
print(phrase.upper())
print(len(phrase))
print(phrase[1])
print(phrase.index("G"))
print(phrase.replace("Giraffe", "Elephant"))

# numbers
add this to the file to be able to access more math methods - from math import *
print(3 * 4 + 5)
print(10 % 3)
my_num = 5
print(my_num)
#absolute value
print(abs(my_num))
#first value is the number second is the power
print(pow(3,2))
print(max(4,5))
print(round(3.8))
print(floor(3.6))
print(ceil(3.7))
print(sqrt(36))

# getting input from users

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello "  +  name + "! You are " + age)


# building a basic calculator

Float() is used to be able to add numbers with decimals. 

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)

# mad libs game

color = input("Enter a color")
plural_noun = input("Enter a Plural Noun")
celebrity = input("Enter a celebrity")

print("Roses are" + color)
print(plural_noun +"are blue")
print("I love" + celebrity)

# lists
friends = [ "Kevin" , "Karen" , "Artur"]
print(friends)
print(friends[2])
print(friends[1:3])
# first and the rest
print(friends[1:])


# lists functions
lucky_numbers = [4, 5, 15, 14, 16, 24, 32]
print(lucky_numbers)
lucky_numbers.extend(friends)
friends.append("Creed")
# insert an item in the middle of a list
friends.insert(1, "Nikki")
friends.remove("Nikki")
friends.clear()
# pop last item in the list
friends.pop()
# tells the index of an element
friends.index("Kevin")
# how many times a value shows up
friends.count("Jim")
# sort the list in alphabetical order / order
friends.sort()
friends.reverse()
# copies the list
friends2 = friends.copy()

# tuples are immutable - cannot be changed or modified
coordinates =(4, 5)
print(coordinates[0])
# NOT POSSIBLE
# coordinates[1] = 10

# Functions
def say_hi(name):
    print("Hello " + name)
# parameter is given to be able to call it inside the function
# call function
say_hi("Mike")

# return statement - return key breaks us out of the function
def cube(num):
    return num*num*num

print(cube(3))

# if statement
is_woman = True
is_tall = True
if is_woman or is_tall:
    print("You are a woman or tall or both")
else:
    print("You are neither woman nor tall")

if is_woman and not(is_tall):
    print("You are short woman")
else:
    print("You are either not woman or not tall")

# if statements and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(2,3,4))


# building a better calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")


# dictionaries - store information
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Jan"])
print(monthConversions.get("Dec"))

# while loop
i = 1
while i <= 10:
    print(i)
    i = i + 1

print("Done with loop")

# Build a basic guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You Lose")
else:
    print("You win!")

# For loops
friends = ["Jim", "Karen"]
for friend in friends :
    print(friend)

for index in range(3, 10) :
    print(index)

for index in range(len(friends)) :
    print(index)

for index in range(5) :
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

# exponent function

# 2 raised to the 3rd power
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))

# 2D lists and nested loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# access element inside , first is list and second is column
print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)

# build a translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:")))

# try except - catching errors


try:
    value = 10 / 0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

