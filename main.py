# var 
my_number = 10
print(my_number)

# none 
a = 1
a = None
print(a)

def donothing():
    b = 0

print(donothing())

# quotes

parrot = "It's not pining, it's passed on! This parrot is no more! It has ceased to be!"
print(parrot)

# convert data types
#int()	Converts to an integer
#float()	Converts to a floating-point number
#hex()	Converts a number to a hexadecimal string
#oct()	Converts a number to a octal string
#tuple()	Converts to a tuple
#set()	Converts to a set
#list()	Converts to a list
#dict()	Converts a tuple into a dictionary
#str()	Converts a number into a string


first_number = int(input("Input your first number:"))
second_number = int(input("Input your second number:"))

print(first_number + second_number)

# A common use for the modulo operator is when we need to find out if numbers are odd or even. An even number is always divisible by 2 so % 2 will always return 0 for even and 1 for odd. The modulo is also used when working with time if we wanted to convert minutes into hours and minutes. For example, we know that there are 60 minutes in an hour, so if we wanted to figure out how many minutes are leftover once we convert 10900 minutes into hours, we would use 10900 % 60. The modulo returns an integer. If we recall the division operator returns a float. What if we wanted to do some division that returns an integer instead? In that case, we would use the floor division operator. The floor division operator is // and it rounds the result down to the nearest whole number and returns it as an integer.

# math in python
print(2 + 2) # 4
print(4 - 2) #2
print(2 * 3) #6
print(9 / 3) #3.0
print(2 ** 3) #8
print(18 % 7) #4
print(10900 % 60) #40

# Assignment Operators
num = 100
print(num)
num //=50
print(num)
num_b = 100
print(num_b)
num_b %=3
print(num_b)


# F-STRINGS example: f"{variable}"

name = input("What's your name? ")
# Here we don't need age to be a number as we are not
# going to do any calculations with it so we don't need to wrap the
# input() in the str() method
age = input("What's your age: ")

# The Modern way of formatting a string
print(f"Hello {name}, you are {age} years old")


# CONCATENATION STRINGS 
name = "Igor"
age = 35

# write your code here
concat_string= name +  " is "  + str(age)
print(concat_string)

# string methods

# capitalize()	Capitalizes the first character of the string
# center()	Centers string
#count()	Returns a count of times a specified value occurs in the string
#encode()	Returns an encoded version of the string (use decode() to decode)
#endswith()	Returns True if the string ends with a specified suffix
#expandtabs()	Sets the tab size in spaces of the string
#find()	Returns the lowest index position of where a specified character was found
#index()	Searches for a specified value and returns the position of where it was found or an error if not found
#isalnum()	Returns True if all characters are alphanumeric
#isalpha()	Returns True if all characters are alphabetic
#isdigit()	Returns True if all characters are digits
#islower()	Returns True if all characters are lower case
#isspace()	Returns True if all characters are whitespace
#istitle()	Returns True if the string is titlecased
#isupper()	Returns True if all characters in the string are upper case
#join()	concatenates string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#partition()	Returns a tuple where the string is parted into two strings and the separator
#replace()	Returns a string where a old value is replaced with a new value
#rfind()	Searches highest index in the string for a specified value
#rindex()	Same but with error if nothing found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into uppercase
#zfill()	Fills the string with a specified number of 0 values at the beginning


my_string = "HELLO WORLD"
my_string_lower_case = my_string.lower()

print(my_string_lower_case)

my_string_2 = "hElLo WorLD"
my_string_2_upper_case = my_string_2.upper()

print (my_string_2_upper_case)
print (my_string.isalpha())

greetings = my_string.replace("WORLD", "Dave")
print(greetings)

motion = ("jump", "walk", "run")
new_string = "ing ".join(motion)
print(new_string)

print(my_string_2.split(" "))

spaced_string = "     42       "
print(spaced_string.strip())


#challenge
dwarves = "Grumpy, Dopey, Doc, Happy, Bashful, Sneezy, Sleepy"
print(dwarves)

lowercase_string = dwarves.lower()
print(lowercase_string)

commas_removed=lowercase_string.replace("," ,  "")
print(commas_removed)

split_list=commas_removed.split(" ")
print(split_list)

# containtment
#In coding, it is often useful to check whether a value exists within a sequence. 
#The sequence can be a list or a range or a string. 
# Just like in Javascript when you used the includes method, in Python, you can use the in keyword to do this. 
# The in operator returns a Boolean value (True or False). 
# The operator is a shorthand for calling an object’s __contains__ method.

print( "rat" in "crate")
print ( "ink" not in "sink")
print("robbie" in  ["gary", "howard", "mark", "jason"])


# if/else statement
number = int(input("Please enter a number:"))

if number == 5:
    print(f"{number} is equal to 5")
else:
    print(f"{number} is not equal to 5")

# ternary expressions 
my_boolean = False

my_string = "Hello" if my_boolean else "World"

print(my_string)

# nested else if elements
exit_program = True
manual_override = False
critical_systems_shutdown = False

if not exit_program and not critical_systems_shutdown:
    if manual_override:
        print("Shutting system down manually")
    else:
        print("This program will not exit just yet")
elif exit_program and critical_systems_shutdown is not True:
    print("Critical systems must be safely shut down before exiting the program")
else:
    print("This program will now be terminated...")

    # for loops
    languages = ["HTML", "CSS", "JavaScript"]
for language in languages:
  print(language)


for character in "Python":
  print(character)


    # range
   # If you want to loop through code a specific number of times you can use the range function. 
   # The range() function will generate a sequence of integers. 
   # In passing through an argument of 5, we’re saying that we wish for that sequence to be comprised of 5 numbers. 
   # Most programming languages, including Python, are zero-based. Therefore they start counting at 0 instead of 1. 
   # When we use the range function to generate a sequence of 5 integers, it will create a series ranging from 0-4. 
   # Those numbers are 0, 1, 2, 3 and 4. We use the for loop to iterate each of the numbers in this sequence.

foods = ['bacon', 'sausage', 'egg', 'spam']

for ind in range(len(foods)):
	# In this example only the index is iterated over not the value
    print(ind, foods[ind])
print(foods)
# In this case we need to calculate the length of the foods collection
# Then we generate a range of integers equal to that length
# Then we iterate over that range of integers



users =  ['anna', 'chris', 'brian']

for i in range(len(users)):
       users[i] = users[i].capitalize()
print(users)

# while loop
countdown_number = 10

while countdown_number >= 0:
    print(f"{countdown_number} seconds...")
    countdown_number -= 1

print("And We Have Lift Off!")

# while loop 2

play_game = True

while play_game:
    continue_playing = input("Would you like to continue playing the game? y/n ")
    
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("Now closing the game...")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")


# prints out numbers for 0 to 9 - challenge
i = 0
while(i<=9):
    print(i)
    i += 1

#Controlling Iteration (Break, Continue & Pass)
# break
for number in range(10):
    if number == 5:
        break    # break here

    print(f'Number is  {number}')

print('Left the loop')

# continue
for number in range(10):
    if number == 5:
        continue    # continue here

    print(f'Number is  {number}')

print('Left the loop')

# pass 
for number in range(10):
    if number == 5:
        pass    # pass here

    print(f'Number is  {number}')

print('Left the loop') 

# nested iteration
i = 2
while i < 10:
    j = 2
    while j <= i/j:
        if not i % j:
            break
        j += 1
    if j > i/j:
        print(f'{i} is a prime number')
    i += 1


# lists
 fruits = ['apple', 'orange', 'banana', 'pear', 'plum']

# Print all fruits
for fruit in fruits:
    print(fruit)

print()

# Get an item located in a list
second_item = fruits[1]
print(second_item)
print()

# Add an item to the list
fruits.append('cherries')
print(fruits)
print()

# Reverse the list
fruits.reverse()
print(fruits)

# Sort the list alphabetically:
fruits.sort()
print(fruits)



# slice lists

#Slice notation with indexing is used to slice the list up. We can slice up lists to get subsets of a list. 
# For example, if we wanted to get the first two items in a list, then we would use the following syntax slice(2) 
# which creates a new list with only the first two elements of the existing list.
# This slice object can take three arguments; slice(start, end, step) which takes 
# integer values of the starting position, end position and step size.

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
x = slice(1, 4, 2)
fruits[x]


# shortened slicing
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:2])


fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
# As lists are zero-indexed index 0 is the first element
print(fruits[0])
# Using an index of -1 gives the last element. Negative indexing counts from the right
print(fruits[-1])
print(fruits[2])
