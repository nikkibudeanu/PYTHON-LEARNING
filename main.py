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


# slicing lists challenge
names = ["Mark", "Betty", "John", "Sally", "Bill", "Steven", "Mary", "Emily", "Adam"]


name = names[2]
print(name)

two_names= slice(2, 4)
print(names[two_names])

other_names= slice(1,6,2)
print(names[other_names])

#slicing list challenge option 2
names = ["Mark", "Betty", "John", "Sally", "Bill", "Steven", "Mary", "Emily", "Adam"]

# write your code here
name = names[2]
print(name)

two_names = names[2:4]
print(two_names)

other_names = names[1:6:2]
print(other_names)



# list methods 
#list.append(x)	Add an item to the end of the list.
#list.extend(list)	Extend the list by appending another list.
#list.insert(i, x)	Insert an item at a given position. The first argument is the index of the element before which to insert
#list.remove(x)	Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
#list.pop(i)	Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
#list.clear()	Remove all items from the list.
#list.index(x, start, end)	Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation.
#list.count(x)	Return the number of times x appears in the list.
#list.sort(key=None, reverse=False)	Sort the items of the list in place
#list.reverse()	Reverse the elements of the list in place.
#list.copy()	Return a copy of the list. Equivalent to a[:].


menu = ['eggs', 'bacon', 'spam', 'spam']
print(menu)
print(menu.count('spam'))
print(menu.count('eggs'))
print(menu.index('eggs'))
print(menu.reverse())
print(menu)
print(menu.append('lobster thermidor'))
print(menu)
print(menu.sort())
print(menu)
print(menu.pop())

#outcome of the example above
#['eggs', 'bacon', 'spam', 'spam']
#2
#1
#0
#None
#['spam', 'spam', 'bacon', 'eggs']
#None
#['spam', 'spam', 'bacon', 'eggs', 'lobster thermidor']
#None
#['bacon', 'eggs', 'lobster thermidor', 'spam', 'spam']
#spam

# list methods challenge 
crew = ["Jean-Luc", "Wesley", "Warf", "Deanna", "William", "Data", "Geordie", "Tasha"]
print(crew)

crew.pop() 
print(crew)

crew.append("Beverly")
print(crew)

crew.extend(["Miles", "Guinan"])
print(crew)

crew.sort(key=len, reverse=True)

# tuples
#In the Determining The Data Type unit, we saw that a tuple is a data type. 
# It is one of the four collection data types. Unlike a list, it is not changeable. 
# It can contain duplicate items. Those items can be of different types such as strings, integers, 
# floats or even another tuple. A tuple can be created by separating values with commas. 
# An empty tuple is created with empty parentheses, and a singleton tuple is one value with a trailing comma. Creating a tuple is referred to as packing. So when you want to get the values back, it is referred to as unpacking.
#  It is also possible to get a value with indexing.


empty = ()
singleton = 'hello',
tup = 12345, 54321, 'hello!' # packing two ints and a string in a tuple
print(empty)
print(singleton)
print(tup)
print(tup[1])
x, y, z = tup # unpacking tuple into variables
print(z)


# tuples challenge
cars = ("Tesla", "BMW", "Ferrari")

print(cars)

get_car = cars[1]
print(get_car)

car_one, car_two, car_three= cars
print(car_one)
print(car_two)
print(car_three)

# dictionaries
# Dictionaries allow us to take things a step further when it comes to storing information in a collection. 
# Dictionaries will enable us to use what are called key/value pairs. In the example above, 'immutable' 
# is the key, and its derivation is the value. When using a dictionary in Python, 
# we define our key/value pairs enclosed in curly braces ({}). 
# After that, we use a string as our key or any other immutable data type. 
# Then we use a colon to separate the key from the value, and then we have the value.
#You would choose a dictionary as a data structure when you have values you want to associate with a key. 
# For example, if you want to map a phone number to a name. 
# A dictionary is very efficient to search as you have the key. Lists are on the other hand, much slower to search.

# dictionary example
user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
print(user['age'])
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user))
print(sorted(user))
print(user)
print('username' in user)

# dictionary challenge
spaceship = {
   "name": "Red Dwarf",
   "type": "Mining vessel",
   "owner": "Jupiter Mining Corporation",
   "captain":"Frank Hollister"
}

print(spaceship)

# getting and setting items in dictionaries
# A dictionary can be thought of as a mapping between indexes (known as keys) and values. 
# Each key must be unique and unchanging as that key maps to a particular value. 
# The value can be any type of object and can appear in the same dictionary multiple times. 
# This association is called a key:value pair or an item. The order of a dictionary is not fixed. 
# It does not have an index as a list has. 
# Two people creating the same dictionary on different computers might get a different order of items. 
# To get the value of a dictionary, you have to use the key.



#This time in the runnable example, we have created our dictionary with default values of empty strings. 
# In this case, we have used the dict() function, which can create dictionaries from lists. 
# The fromkeys() method is used to specify the keys list as the keys and a variable of an empty string as the values.
# To set a value, you can use the items key in square bracket notation and the assignment operator with a value. 
# The default values are all overridden with the new values.
# To get a value, you can use the same notation without the assignment. 
# Here we have printed the age of 100. 
# However, if we attempted to get the value of a nonexistent key, then an error would occur. 
# To avoid this you can use the get() method which will get the value if the key exists and return None if it does not. 
# More methods will be covered in the next unit.
# As key 'home' returns None lets add a key:value pair. 
# The same syntax is used as when we were setting the 'username', 'first_name', 'last_name' and 'age' values. 
# As 'home' key is new, it is added to the dictionary with its value. 
# As the 'age' key already exists, the value is changed from 100 to 99. 
# If we delete a key the value is deleted with it.
# If we want to get a list of the keys only you can use the keys() method and wrap that in a list() function. 
# The same syntax but using values or items will get a list of the dictionary values or items instead.

keys = ['username', 'first_name', 'last_name', 'age']
default_value = ''
user = dict.fromkeys(keys, default_value)
print(user)
user['username'] = 'tombombadil'
user['first_name'] = 'Tom'
user['last_name'] = 'Bombadil'
user['age'] = 100
print(user)
print(user['age'])
print(user.get('home', "doesn't exist"))
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user.keys()))
print(list(user.values()))
print(user)


# dictionaries challenge
data = {
    "first_name": "Arthur",
    "last_name": "Dent",
    "species": "Human"
}

# add your code here
name = data["first_name"]
print(name)


species = data["species"]
print(species)

data['age'] = 42



# this will print the data to the terminal
print(data)


# dictionary methods

##clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a new dictionary with the specified keys and value
#get(keyname, value)	Returns the value of the specified keyname. Used in the previous unit. Returns default None if the keyname doesn't exist unless you override this default with a optional value.
#items()	Returns a list containing a tuple for each key:value pair
#keys()	Returns a list containing the dictionary's keys. Used in the previous unit.
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key:value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key:value pairs
#values()	Returns a list of all the values in the dictionary. Used in the previous unit.

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
print(user.items())
print(user.get('age', 0))
user.update({'home': 'Withywindle, Middle-Earth'})
print(user)
print(user.popitem())
print(user)
user.clear()
print(user)

#-->>>>> outcome

#{'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100}

#dict_items([('username', 'tombombadil'), ('first_name', 'Tom'), ('last_name', 'Bombadil'), ('age', 100)])
100

#{'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100, 'home': 'Withywindle, Middle-Earth'}

#('home', 'Withywindle, Middle-Earth')

#{'username': 'tombombadil', 'first_name': 'Tom', 'last_name': 'Bombadil', 'age': 100}

#{}


# dictionaries methods challenge
challenger = {
	"name": "Katniss Everdeen",
	"age": 16,
	"district": 12,
	"weapon": "Bow and Arrow", 
	"status": "Victor"
}

# add your code here

challenger.update({'occupation': "Hunter"})
occupation = challenger.get('occupation', 0)
print(occupation)
challenger.update({'age': 17})
challenger.pop("status")




print(challenger)


#sets


#A set is another useful Python data type. 
# It is a mathematical concept of a collection of items with no duplicates. 
# It also uses curly brackets, but commas separate items in the collection. 
# However, this means that to create an empty set; you have to use the method set() as {} would create an empty dictionary. 
# You can use the in keyword to see if an item is in a set.


#first example

#In the first runnable example, we have added multiple identical items to the set. 
# However, when we print the set, the duplicates have been removed. 
# You cannot change the items in a set, but you can add an additional single item with add() or add new multiple items as a list with update(). 
# To remove an item use discard() rather than remove() as it will error where the item does not exist. 
# Sets are unordered so using pop() is not recommended as you will not necessarily know which 'last item' will be removed except by the return value.


breakfast = {'bacon', 'egg', 'spam', 'spam', 'spam', 'spam', 'spam'}
print(breakfast)
print('egg' in breakfast)
breakfast.add('sausage')
print(breakfast)
breakfast.update(['Lobster Thermidor', 'truffle pate', 'crevettes', 'shallots','aubergines'])
print(breakfast)
breakfast.discard('aubergines')
print(breakfast)

# ---> outcome
#{'bacon', 'egg', 'spam'}
#True
#{'bacon', 'sausage', 'egg', 'spam'}
#{'bacon', 'shallots', 'sausage', 'egg', 'truffle pate', 'crevettes', 'spam', 'aubergines', 'Lobster Thermidor'}
#{'bacon', 'shallots', 'sausage', 'egg', 'truffle pate', 'crevettes', 'spam', 'Lobster Thermidor'}


#second example

#Sets have mathematical operations like union, intersection, difference, and symmetric difference. 
# A union is all values that are in either set or both. 
# The intersection is the values that are in both sets. 
# The difference is the values that are in the first set but not the second. 
# The symmetric difference is all values that are in one of the sets but not both of them.

hello = set("Hello")
world = set("World")
print(f"The unique letters in hello are: {hello}")
print(f"The letters in hello or world or both are: {hello|world}") # | is the symbol for union
print(f"The letters in both hello and world are: {hello&world}") # & is the symbol for intersection
print(f"The letters in hello but not world are: {hello-world}") # - is the symbol for difference
print(f"The letters in hello and world but not both are: {hello^world}") # ^ is the symbol for symmetric difference

#---> outcome
#The unique letters in hello are: {'l', 'e', 'o', 'H'}
# The letters in hello or world or both are: {'o', 'l', 'e', 'W', 'r', 'H', 'd'}
# The letters in both hello and world are: {'o', 'l'}
# The letters in hello but not world are: {'e', 'H'}
# The letters in hello and world but not both are: {'e', 'W', 'd', 'r', 'H'}


# sets challenge

product_list = ['hammer', 'saw', 'nails', 'wood', 'screws', 'paint', 'brushes', 'light bulbs']
products_bought = {'nails', 'screws', 'hammer', 'wood', 'saw', 'hammer', 'saw', 'nails', 'nails', 'screws', 'hammer'}

# add your code here

products_bought.add('light bulbs')
products_bought.update( ['wood', 'screws', 'saw'])
has_nails = "nails" in products_bought 
has_paint = "paint" in products_bought
unsold_items = set(product_list) - products_bought

print(has_nails)
print(has_paint)
print(unsold_items)

# Iterating python data structures

#Dictionaries are more complicated due to the key: value structure. You can use the keyword in for dictionaries but what will be returned is just the key. You could, of course, return the value using the square bracket notation. However, there is a better way to iterate over a dictionary.

#If we needed access to both keys and values, we’d have to use a dictionary method called .items()

#In the first runnable example, we define two new variables in our for loop, key and value. These variables don’t need to be called key and value, but as the first variable will be the key and the second variable will be the value, it’s considered to be a good convention. Then after that, we just print out the key and the value, with some nice formatting to denote each key/value with which we’re working.


user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("------------------")


#Here is how you would iterate over a set. It is much like for a list. However, remember that the order may not remain static. You could also use range() and len() to get index values.

# Create a set
directions = set(['north', 'south', 'east', 'west'])

# Print its members
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

print()
# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)

# iterating data structures challenge
data = {
	"first_name": "brian",
	"last_name": "johnson",
	"occupation": "student"
}

scores = [6, 9, 8, 7, 8, 9]

# write your code here

for key, value in data.items():
	if value != "student":
		data[key] = value.capitalize()

print(data)	


for ind in range(len(scores)):
	scores[ind] += 1

print(scores)


#list comprehensions

#List comprehensions are available in Python as a concise way to create a list. 
# It is commonly used where you want to generate a list based on an operation or to create a new sub-list of an existing list.

# 1. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i for i in range(10)])

# 2. [0, 2, 4, 6, 8, 10]
print([i for i in range(0,11,2)])

# 3. [0, 1, 4, 9, 16, 25, 36, 49]
print([x**2 for x in range(0,8)])

# 4. [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print([((i,(i+1))) for i in range(5)])

# 5. ['woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo']
print(['woohoo' for i in range(7)])

# 6. ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
hw = 'hello world'
print([i for i in hw])

# 7. [('A', 'D'), ('A', 'E'), ('A', 'F'), ('B', 'D'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('C', 'F')]
ab = 'ABCDEF'
print([(ab[i],ab[j]) for i in range(0,3) for j in range(3,6)])

# list comprehension challenge

letters = [i for i in "Marvin"]

print(letters)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [num for num in numbers if num % 2 == 0]

print(evens)


# GET THE PRIME NUMBERS FROM A LIST
evens = [num for num in numbers if num % 2 == 0]


#Dictionary Comprehensions

#Dictionary comprehensions are just like list comprehensions. The difference in the syntax is that curly rather than square brackets are used. Also, before the for keyword you need to include the key and value separated with a colon.

# 1. {'cherry': 6, 'mango': 5, 'apple': 5, 'banana': 6}
fruits = ['apple', 'mango', 'banana','cherry']
print({f:len(f) for f in fruits})

# 2. {0: '', 1: '*', 2: '**', 3: '***', 4: '****'}
print({i:(i*'*') for i in range(0,5)})

# 3. {0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
print({i:(True if i%2==0 else False) for i in range(10)})

# 4. {(0, 1): False, (1, 2): False, (3, 2): False, (0, 0): True, (3, 3): True, (3, 0): False, (3, 1): False,
# (2, 1): False, (0, 2): False, (2, 0): False, (1, 3): False, (2, 3): False, (2, 2): True, (1, 0): False,
# (0, 3): False, (1, 1): True}
print({(i,j): (True if i==j else False) for i in range(4) for j in range(4)})


# dictionary comprehension challenge
cards = ['king', 'queen', 'jack', 'ace']

# write your code here

cards_dict = {card:card.upper() for card in cards}
print(cards_dict)


# nested data structures 
matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
]

print([[row[i] for row in matrix] for i in range(4)])

# In this runnable example, we see the type of nesting dictionary structure you might find in a database. 
# To access the nested dictionary, you string together the commands you would normally use. 
# Therefore payroll['emp1']['name'] goes down one level to get the name of the first employee. 
# The get() method can also be used; payroll['emp1'].get('Wage') as in this case to get the first employees wage. 
# We can add and delete values as before using their keys. 
# To print this data out in an easily readable fashion, it is best to use a nested loop. 
# The first loop gets the key-value pairs and prints the key. 
# The nested loop gets the key-value pairs from the nested dictionary and prints both.

payroll = {'emp1': {'name': 'Precious', 'job': 'Mgr', 'Wage': 50000},
     'emp2': {'name': 'Kim', 'job': 'Dev', 'Wage': 60000},
     'emp3': {'name': 'Sam', 'job': 'Dev', 'Wage': 70000}}

print(payroll)

print(payroll['emp1']['name'])
print(payroll['emp1'].get('salary'))
print(payroll['emp1'].get('Wage'))
payroll['emp4'] = {'name': 'Max', 'job': 'Admin', 'Wage': 30000}
print(payroll)
del payroll['emp3']

for id, info in payroll.items():
    print(f'\nEmployee ID: {id}')
    for key in info:
        print(f'{key} : {info[key]}')


# nested data structures challenge
student_data = [
    {
        "name" : "John Smith",
        "email": "john@gmail.com",
        "subjects": ["Math", "Psychology", "Physics", "Chemistry", "Biology"]
    },
    {
        "name" : "Mary Jones",
        "email": "mary@gmail.com",
        "subjects": ["Fine Art", "Music", "Biology", "Geography", "Politics"]
    }
]

print(student_data)
	

# naming variables 

#Python is quite forgiving when it comes to naming. 
# However, there are suggested style rules that you should follow. 
# Variable names should be lowercase and if including multiple words, should use underscores as separators. 
# Giving a variable a name that explains its purpose is encouraged. 
# Where the meaning is obvious, you can use a single letter variable name. 
# There is a convention where you prefix a global variable with an underscore 
# if you are using it in a module imported into another module. 
# There is no constant in Python unlike the const in JavaScript, 
# so if you have a variable you do not want to be changed, then use capital letters to denote this. 
# Generally, it is a bad idea to use lowercase L, uppercase O and uppercase 
# I for single-character names as they are easily confused by eye with other characters.




# naming functions

#A function within a class is known as a method. 
# A method has the same naming conventions as a class. 
# If you have a method in a class you don't wish to be public, then start its name with an underscore. 
# This is just a convention for saying "Please don't touch" to other developers who are working on your code.

#If you use a double underscore prefix (dunder) for an attribute in a method, 
# then the attribute name will be altered, so it cannot be accessed by the regular methods. 
# The attribute name is “mangled.”

def divide(num, denom):
    return num / denom
    
def my_country(country):
    print(f"I am from {country}.")


# naming class 

#When naming a class, try and give it a name that gives the reader an idea of the purpose of the class. 
# Class names should have their first character capitalised.

class ComplexNumber:
def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart


#Indentation in Python
# Correct:

# It is aligned with the opening delimiter, e.g. the opening parentheses.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add four spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)



#reserved keywords

#Keywords are reserved words in Python. 
# That means they cannot be used as ordinary identifiers like a variable, function, method or class name. 
# They have a specific meaning and purpose within Python and cannot be used for anything other than that purpose.


#Defining Functions in Python Refresh

# Most code will be broken out into functions. 
# Functions are a grouping of statements that work together to perform any actions that we may need

#There is another type of function in Python known as Lambda. 
# A lambda function is a small anonymous function. 
# It can take any number of arguments but only has one expression. 
# As you can see the function has no name (hence anonymous) so we have assigned it to the variable add.

add = lambda a, b : a + b
print(add(5, 12))




#call a function

# Calling a function is executing the code. 
# When you defined a function, you used the def keyword but to call 
# it you simply use the function name followed by parentheses. 
# You can pass information into the function as arguments inside the 
# parentheses separated by commas. 
# A parameter is the variable listed in the parentheses when the function is 
# defined, and the argument is the value you pass into the function 
# parentheses when it is called. You have to supply the same number of arguments 
# as there are parameters. A function can be called by another function or even by itself.


# 2. This function runs for the name and age function calls
def get_user_input(prompt):
    return input(prompt)

# 4. This function runs twice
def print_out_to_console(value_to_be_printed):
    print(value_to_be_printed)

# 1. name and age are the first two function calls to run sequentially
name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

# 3. Then function calls run sequentially
print_out_to_console(f"Your name is {name}")
print_out_to_console(f"You are {age} years old")


# function calling challenge 

def print_hello_world():
    print("Hello World!")
    
print_hello_world()


#Taking Parameters & Returning Results

#A function's parameters are the special variables used by a function to handle this input, 
# whereas the arguments are the values provided for the parameters when we run the function. 
# For example, on line 1, we create a function that has a parameter named name, and then on line 5 
# we run that function and pass in the value of the variable username as the argument for that parameter.

def print_message(name):
    print(f"Hello {name}")

username = input("What's your name? ")
print_message(username)

#We don’t provide an argument when we invoke the function as we do on line 5, the function will just print out Hello World. 
# Notice that we initially stored the value in a variable called username, but inside the function, we’ve called in a name. 
# This is because we’re passing a new variable to the function called name, with the value of username. 
# The name variable cannot be accessed outside of the function. 
# Therefore if we were to try to print name outside of the function, it wouldn’t work. 
# This is known as variable scope.

#Rather than printing the result in the function, we have returned it. 
# This is how a computer program expects to see the result of a function. 
# However, to see the output as a human, we then need to wrap the function 
# calls in print() , so the result is printed to the terminal.

def print_message(name="World"):
    return f"Hello {name}"

username = input("What's your name? ")
print(print_message())
print(print_message(username))

#Up until now, we have been using the print() in all our examples. 
# This is because it prints the result to the console. 
# This is useful as a developer as you get a human-readable result printed in the console. 
# Of course, computers do not need a human-readable output. In a program consisting of functions, 
# you will instead get the function to return a result. The return statement returns the result of 
# the function and is the point where the code stops running. Statements after a return statement are not executed. 
# A return statement can only be used within a function. 
# As we have seen in previous lessons if no expression is included in the return statement, then None is returned.

def add_two_nums(num1 , num2):
    sum=num1+num2
    return sum

result = add_two_nums(2, 3)
print(result)


def add_three_nums(num1, num2, num3):
    sum=num1 +num2+ num3
    return sum
    
result= add_three_nums(2,3,2)
print(result)

#function challenge

#Define a function named add_numbers that takes two parameters named: nums_tuple, min_value
#The function should return the sum of all the values in the nums_tuple that are greater or equal to the min_value
# Outside of the function
# Create a variable named: total and assign it the return value from calling the add_numbers function and passing in the two arguments: (21, 4, 7, 19, 1), 15
# print total

def add_numbers(nums_tuple, min_value):
    return sum([x for x in nums_tuple if x >= min_value])

total = add_numbers((21, 4, 7, 19, 1), 15)
print(total)

    
#Splat! *args & **kwargs

#In a function, you can list the parameters separated with commas. 
# An elementary function is one that takes parameters a, b and adds their argument values together. 
# This function is then reusable as you can add any two numbers together. 
# But what if you want to add three numbers together? 
# One possible solution is to pass in a list as an argument containing all the numbers you wish to add. 
# This does require you though to have created the list in advance. 
# This is inconvenient. 
# The purpose of *args is to allow you to pass in a varied number of positional arguments. 
# The iterable object *args can be renamed to any other name as long as it is preceded by the unpacking operator *. 
# Rather than a list, the *args operator is a tuple so is immutable and needs to be unpacked to use the values.

#The **kwargs object behaves very similarly but rather than a tuple is a dictionary. 
# Like with *args you can change the name as long as the ** unpacking operator precedes it. 
# Where you would use **kwargs over *args is when you have a keyword or named arguments.

#In the first function below, you can only ever add two arguments. 
# The add_integers function is an improvement, but you still have to create a list of the arguments ahead of time. 
# In the add_many_integers function, we have used *args but renamed them as *integers thus allowing us to use as many integers as we 
# like when calling the function. 
# The concatenate_words function uses **kwargs but renamed as **words. 
# In this case, we have passed in many strings as named arguments, and as this is a dictionary within the function, 
# we have iterated over the dictionary values.

def addition(a, b):
    return a + b

print(addition(2,2))

def add_integers(list_integers):
	total = 0
	for x in list_integers:
		total += x
	return total

list_integers = [1, 2, 3, 4]
print(add_integers(list_integers))

def add_many_integers(*integers):
	# Rename *args to something suitable
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))

def concatenate_words(**words):
	result = ""
	# As **kwargs is a dict you need to iterate over .values()
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))


#challenge kwargs, args and splat
def make_string(*strings):
    return ' '.join(strings)

my_string = make_string("Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth")
print(my_string)

def get_age(**data):
    return data.get("age", "no age provided")
     
pats_age = get_age(name="pat", level=4, age=33, occupation="postman")            
print(pats_age)


#Scope - Local vs Global Variables

#Scope when referring to variables means where within the program can that variable be accessed. 
# The broadest scope is built-in which are the variables that come with the Python coding language. 
# You don't need to declare or import these variables as they are available to you throughout Python. 
# If you declare a variable in your program and it is not within any functions, then it is a global variable. 
# A global variable is available to use anywhere in the program. 
# However, if you declare a variable inside a function, then it is only available for use within that function. 
# Therefore it is known as local scope.

#You can, of course in Python create functions inside functions, so a local scope variable in a parent function is also 
# available in the child function with use of a special keyword (that will be described in an upcoming unit).
#  If you use the variable from the parent function in the child function, then the scope is neither local nor global. 
# A Python variable scope that is neither local nor global is referred to as nonlocal. This is called the enclosing scope.

#The global Keyword

#While in many or most other programming languages variables are treated as global if not otherwise declared, 
# Python deals with variables the other way around. They are local, if not otherwise declared. 
# This will cause problems, for example, if you access a variable declared outside a function (global) within a 
# function and try and reassign its value. If you then access the global variable outside the function, 
# it will still have its original value rather than the new one reassigned within the function. 
# One workaround would be to return the variable from the function so now it's reassigned value is available outside the function. 
# However, there is a better option, and that is to use keywords to state which scope is to be used unambiguously.


#In this second example you will see as you step through that if you input an age greater than or equal to 18 the 
# global variable can_access changes to True even in the global scope. This is because the global keyword has been used.

can_access = False
	
def update_access():
    global can_access
    age = int(input('Enter your age: '))
    if age >= 18:
        # The global keyword is used
        can_access = True
        return('You are old enough to enter')
    else:
        return('You are too young, you may not enter');

update_access()

print(can_access) # will now print True if an age >= 18 is entered

# global keyword challenge

test_passed = False
answer = "friend"

def speak_friend_and_enter():
    global test_passed # use global keyword
    if answer == "friend":
      test_passed = True
        
speak_friend_and_enter()
print(test_passed)


#The nonlocal Keyword

#In the nested function example below you will see that line 4 does not work. 
# The variable my_age is local to the which_scope function not the inner_scope one. 
# Scroll down to the second runnable example to see how to fix this.

def which_scope():
    my_age = 49 # local variable my_age
    def inner_scope():
        my_age += 1 # Issue when we try to run this line.
        print(my_age)
    inner_scope()

which_scope()


#To prevent this you use the nonlocal keyword.

def which_scope():
    my_age = 49 # local variable my_age
    def inner_scope():
        nonlocal my_age # No longer an issue because of this
        my_age += 1
        print(my_age)
    inner_scope()

which_scope()

# non local keyword challenge
def outer_function():
    age = 10
    def become_adult():
        nonlocal age
        age = age + 11
        
    become_adult()
    return age

result = outer_function()
print(result)

#Passing Functions Around

#One thing you may have noticed in the calling functions example is that functions are passed around to other functions. 
# This is possible in Python as a function is itself an object. 
# A function object can be referred to in the same way as a string object. 
# You can assign a function to a variable or even store it in a data structure. 
# A function can be passed into another function or even to itself. 
# In the image, the input x can be another function.


def print_arguments( **args ):
    """Prints the arguments"""
    print(f'The arguments are {args}')

def pass_function(function_name, **args):
    """Takes a function as an argument
    Passes the argument 'l' to the function passed in 
    """
    print("This function takes another function as an argument")
    function_name(f=args['l'])

pass_function(print_arguments, l='spam')

#Decorators

#A decorator is a way in Python to add new functionality to an existing function without modifying its structure. 
# This is useful as you do not need to create new functionality in your code if a decorator already exists for that purpose. 
# A decorator is said to wrap a function to modify its behaviour. 
# Python has something called the “pie syntax” to make decorator use simpler. 
# The @ symbol is used to prefix the decorator name.



#Here is a very simple decorator. 
# It modifies the function say_hello by printing a string before it is called and after it is called. 
# The decorator is modifying the behaviour of the function. 
# It wraps the function and extends the behaviour of the wrapped function without modifying the function permanently.

def my_decorator(func):
    def wrapper():
        print("The function has not been called yet. Let's call it.")
        func()
        print("The function was called and has returned a result.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")
    
say_hello()


# Now let's look at a real-world example of using a decorator. 
# We have a decorator that defines what units you want to display your function results in. 
# It is demonstrated with a function to calculate area. 
# The decorator is then used to say that on this occasion you want the result in meters squared. 
# By changing the argument in the decorator, you can change this to acres, for example, without altering the function. 
# This same decorator could be used for any function that outputs a value with units.

def define_units(unit):
    """Define the units"""
    def decorator_define_units(func):
        func.unit = unit
        return func
    return decorator_define_units

@define_units('m^2')
def area(length, width):
    """Calculate area of rectangle or parallelogram"""
    return length * width

# The unit defined in the decorator can be used with dot notation
# In this case the function area units can be used as area.unit
print(f'The area is {area(3,5)}{area.unit}')

#decorator challenge
def add_author(func):
    """
    Decorator to add string with author information
    to print after decorated function runs
    """
    def wrapper(*args):
        r = func(*args)
        return f"{r}\nBy Code Institute"
    return wrapper
        
# write your code here
@add_author
def print_article_title(title):
    return 'Article Title: Python Decorators'

result = print_article_title('Python Decorators')
print(result)

# odd numbers challenge 

numbers = [12, 45, 60, 87, 999, 200, 84, 42, 85, 77, 2, 3, 77, 99, 20]

def get_odd_numbers(numbers):
    #create an empty list
    odd_numbers = []
    #
    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)
            
    return odd_numbers
    
print(get_odd_numbers(numbers))

# classes

#Classes are a good way of combining data and methods and are useful when dealing with hierarchies. 
# They are generally used to model more complex data types which can’t be 
# modelled using Python’s built-in data structures such as lists and dicts.

#We define a class by using the class keyword followed by the name. 
# Like functions, a class does not do anything until it is executed. 
# Scope also applies to classes so global and nonlocal scope have to be taken into consideration. 
# A class name should start with a capital letter and should have a docstring. 
# Classes can contain functions and other statements.

class HelloWorld:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hello, world!'

#The __init__() Method
# The first thing to note is that a function within a class is known as a method. 
# A particular type of method that runs when an instance of the class is created is an initializer. 
# The __init__ method is known as a dunder, double-underscore or magic method, and these tend to be used on classes mainly. 
# They use double underscores so as not to conflict with your own defined classes.


# An __init__() method on its own would simply create an empty class object. 
# However, an __init__() method can take arguments. 
# One of the advantages of object-orientated programming is the ability to model the real world in code. 
# If you were writing software to use in a car factory or dealership, you could use a class to create an object 
# Car that has the same properties and attributes as a real car.

class Car:
	def __init__(self, color, make, model, fueltype):
		self.color = color
		self.make = make
		self.model = model
		self.fueltype = fueltype

bullitt = Car('Green', 'Ford', 'Mustang', 'Gasoline')


# init challenge
class Customer():
    """
    Creates an instance of Customer
    """
    
    def __init__(self, fname, lname, email, phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone

customer_one = Customer("Theon", "Greyjoy", "t.gj@email.com", "123456789")
print(customer_one)
print(customer_one.fname)
print(customer_one.lname)
print(customer_one.email)
print(customer_one.phone)

#The "self" Keyword

# The self keyword associates functions and properties with a class. 
# It also holds references to data and behaviour of particular instances of a class. 
# It’s customary to use self to refer to the class instance, but in fact, any variable could be used. 
# It must be the first parameter of any function in the class. 
# Python simply uses self to state to what instance to assign an instance attribute. 
# In the previous unit, we created an object bullitt with color of Green. 
# The self keyword is used to confirm that the argument "Green" for the object instance bullitt is a reference 
# to the color attribute of the class Car.

class Bird:
   """
   Bird class
   """
   def __init__(self, kind, call):
      #properties
       self.kind = kind
       self.call = call

   #behaviour
   def description(self):
       """
       describe the bird
       """
       return f"A {self.kind} goes {self.call}" 
       
owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())

# self keyword challenge 
# Write your code here
class OrderItem():
    """
    Creates an instance of OrderItem
    """
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
    
    def description(self):
        """
        Describes the order item
        """
        return f"{self.quantity} x {self.item} at ${self.price} each"


# The code below will use your class to print values to the terminal after 
# it has been written. Comment the lines below back in to test it  

order_item_one = OrderItem("bowtie", 10, 3)
print(order_item_one.description())

order_item_two = OrderItem("Fez", 25, 1)
print(order_item_two.description())


#Creating Class Instances

#You can create multiple instances of a class. 
# An instance is an individual object of the class in memory. 
# It exists live in RAM until the point it is removed.

#Let's return to the Bird class. 
# When you create an instance of the class, it is the initializer code that runs. 
# This is the __init__ method. This method assigns the values to the object properties.
#  The self keyword is a reference to the current instance of the class and is used to access variables that belong to the class. 
# To create an instance of the class, you need to provide the same quantity of values as there are properties (in this case two). 
#  Once you have an instance of that class, you can access the variables and methods using the dot notation.



owl = Bird('Owl', 'Twit Twoo!')
owl.call
owl.description()


class Bird:
   """
   Bird class
   """
   def __init__(self, kind, call):
      #properties
       self.kind = kind
       self.call = call

   #behaviour
   def description(self):
       """
       describe the bird
       """
       return f"A {self.kind} goes {self.call}" 
  
   def bird_call(self):
       print(self.call.upper())

owl = Bird('Owl', 'Twit Twoo!')
print(owl.call)
print(owl.description())
crow = Bird('Crow', 'Caaaw!')
print(crow.description())
owl.call = 'screech'
print(owl.description())
del owl.call
print(owl.description())

# challenge instances
class User():
    """
    Creates an instance of User
    """
    def __init__(self, username, email, subscribed):
        self.username = username
        self.email = email
        self.subscribed = subscribed
    
    def description(self):
        """
        Describes the instance of User
        """
        return f"user: {self.username}, email: {self.email}, subscribed: {self.subscribed}"


# write your code here
user_one = User("arnold", "arnold@email.com", True)
print(user_one.email)
user_one.email = "murphy@email.com"
print(user_one.description())



#Class Properties & Attributes

# A class can contain data. 
# If you create a Python variable within the class, it is known as a class attribute. 
# As it is created outside the constructor function, it is shared between all objects of this class. 
# However, if you create a Python variable within the constructor function, it is known as an instance attribute. 
# An instance attribute is only accessible from the scope of an object instantiated from the class.

# When we access these attributes from the class or from the object, they are referred to as properties. 
# A class attribute can be accessed as a class property or an instance property. 
# If you try and access an instance attribute as a class property, then you will raise an AttributeError.

class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call}" 
       
owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())
print(owl.definition)
print(owl.call)
print(Bird.definition)
print(Bird.call)


# challenge class properties and attributes
class ContactInfo():
    """
    Creates an instance of ContactInfo
    """
    about =  "Contact information for customer"
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def description(self):
        return f"{self.name} : {self.email}" 

print(ContactInfo.about)  

contact = ContactInfo('dave', 'lister@email.com')
print(contact.description())

#Functions + Classes: Methods

#A method is a function that is within a class or object. 
# When you have seen the term method used in the lessons so far it has concerned the built-in methods such as append() for a list. 
# You can create your methods within your classes. When you create an instance of that class, then you can call the method 
# using dot notation. In the class instance unit, we used the description method on the object owl, which was instantiated from the
#  Bird class. This is referred to as invoking the description() method. 
# Not all methods in a class need to be public. 
# If you want to indicate to other developers that a method is private, then prefix the method name with an underscore. 
# A private method is one that cannot be accessed except within the class. 
# We will use private methods in an upcoming unit.

"""
In the runnable example, there is a method that returns a description of the instance. 
If we create an owl instance, we can call that method and print the result to the terminal. 
The class attribute is within the scope of the method so that it can be used. 
However, the parrot variable created in the method is local to the method so it could not be used in the class.

"""
class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        parrot = "Norwegian Blue"
        return f"A {self.kind} goes {self.call} and is {self.definition} It is not a {parrot}" 
       

owl = Bird('owl', 'Twit Twoo!')
print(owl.description())

# methods challenge 
class BlogPost():
    """
    Creates an instance of BlogPost
    """
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def get_overview(self):
        return f"{self.title} by {self.author}"
    
    def full_info(self):
        return f"Blog post: {self.title}. Content: {self.content}. Author: {self.author}"
        
post = BlogPost("Python Classes", "Python is known as an object-oriented language...", "Code Institute")
print(post.get_overview())
print(post.full_info())


#Subclassing & Inheritance

#Subclassing is a useful way of creating a specialised version of a class with its methods but re-using existing methods and 
# properties of the parent (or base) class. 
# We could create a Parrot class which subclasses the Bird class created in previous units. 
# We can use the existing methods on the parent/base class, and we don’t have to supply the bird kind or call because that’s 
# coded into the Parrot class. 
# To subclass/inherit from a superclass/parent, add the name of the parent class inside parentheses as part of the subclass name. 
# To call a method on the parent class, precede the parent method name with the parent class name and a period.


class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call} and is {self.definition}" 


class Parrot(Bird):
    def __init__(self, color):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.color = color


parrot = Parrot('blue')
print(parrot.color)
print(parrot.description())

# challenge subclasses
class JobListing():
    """
    Creates an instance of JobListing
    """
    def __init__(self, job_title, department):
        self.job_title = job_title
        self.department = department
    
    def description(self):
        return f"Job opening for {self.job_title} in {self.department} department"


# write your code here
class SalesManager(JobListing):
    def __init__(self, salary):
        JobListing.__init__(self, "Sales Manager", "Sales")
        self.salary = salary
        

sales_manager = SalesManager(45000)
print(sales_manager.description())
print(sales_manager.salary)
            
# Mixins

#A mixin is a class that provides methods to other classes but is not itself a parent class. 
# You cannot create a subclass of a mixin. If you find yourself creating methods in your subclasses that are very similar, 
# then this is an opportunity to move that method into a mixin.

#The purpose of a mixin is to reduce the amount of unnecessary duplication of code. 
# If you have a piece of logic that is frequently repeated in the subclasses, then move it to a mixin.


# Here we have a superclass with a method that returns x and two subclasses with methods that return y and z 
# respectively as a tuple including the inherited x from their parent class. 
# However, both subclasses also use a mixin which unpacks a tuple and returns the values in a string with some formatting. 
# The mixin has no __init__ so cannot be a superclass. It is just a class containing a method that you can use in any other 
# class in your program.


class SuperClass:
    """This is the base or parent class"""
    def __init__(self, x):
        self.x = x
    def result(self):
        """Method returns a variable x"""
        return self.x

class Mixin:
    """This mixin can be used with any class"""
    def prettify_string(self, a):
        """Method that returns a string containing variables c and d"""
        c, d = a # Unpacks the tuple a into variables c and d
        return f'{c}, {d}!'

class SubClass1(Mixin, SuperClass):
    def __init__(self, x, y):
        """Inherits x from SuperClass and extends with variable y"""
        SuperClass.__init__(self, x)
        self.y = y
    def result1(self):
        """Returns a tuple of x and y"""
        return self.x, self.y
    
class SubClass2(Mixin, SuperClass):
    def __init__(self, x, z):
        """Inherits x from SuperClass and extends with variable z"""
        SuperClass.__init__(self, x)
        self.z = z
    def result2(self):
        """Returns a tuple of x and z"""
        return self.x, 2 * self.z

hello = SubClass1('Hello', 'World')
world = SubClass2('Hello', 'World')

print(hello.prettify_string(hello.result1()))
print(world.prettify_string(world.result2()))


# In the runnable example, we create a simple Human Resources application. 
# The first class is Employee which is the base class. 
# It takes the necessary information about the employees and increments the employee number for 
# each new employee added to the system. 
# Then we have a mixin class HolidayMixin.
# This is just a piece of logic to calculate the extra holidays you accrue the longer you work for the company. 
# You cannot create an instance of this class. 
# As a mixin, it just contains a method to return the number of holidays a particular employee is due. 
# It bases this on the number of years of service.

#The next class is DirectDeveloper. 
# This subclasses Employee but takes an additional parameter of prog_language, allowing you to specify which 
# programming language this developer uses. 
# There is a method here to calculate the salary and give a bonus to Python developers as they are most in demand. 
# The details method inherits from the Employee class and adds additional information about the programming language.

# We have instantiated two developers here, one Python and one php. 
# See how their details differ. 
# Also, we use the method from the mixin to see how much annual leave they have accrued. 
# You can also call the method to see their salary. 
# Try adding some other developers and see the employee numbers increase. 
# Try different programming languages and years of service to see how the salary or holiday benefits change.


class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, name, no_of_years):
        # instance attribute
        self.name = name
        self.no_of_years = no_of_years
        Employee.employee_no += 1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"Name: {self.name}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"


class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    Note that a mixin has no __init__ as you cannot create an instance of a mixin
    """
    def calculate_holidays(self, no_of_years):
        """
        Method that returns holidays as an integer if given no of years of service
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if no_of_years < 3:
            bonus = holidays + 1
        elif no_of_years <= 5:
            bonus = holidays + 2
        elif no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class but also inheriting from HolidayMixin
    """
    def __init__(self, name, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, name, no_of_years)

    def calculate_salary(self):
        """
        Returns salary plus bonus as an integer
        """
        base = 30000
        if self.prog_language.lower() == 'python':
            bonus = base * 0.10
        else:
            bonus = 0
        return base + bonus

    def get_details(self):
        """
        Method to return direct developer details as a string
        Uses details() method inherited from Employee super class
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}'


eric = DirectDeveloper("Eric Praline", 2, "python")

# Prints out all the attributes of your eric instance using get_details method from DirectDeveloper
# If you use the details method from Employee then the Programming Language will not print
print(eric.get_details())
# The mixin method is usable for instance eric
print(eric.calculate_holidays(eric.no_of_years))
# Uses the calculate_salary method from DirectDeveloper
print(f'${eric.calculate_salary()}')

luigi = DirectDeveloper("Luigi Vercotti", 10, "php")
print(luigi.get_details())
print(luigi.calculate_holidays(luigi.no_of_years))
print(f'${luigi.calculate_salary()}')


# Class Composition

#In object-orientated programming, two significant concepts are inheritance and composition.

# Inheritance is what we have used up until now in this lesson. 
# For example, a subclass Parrot inherits from a Bird class. 
# The inheritance relationship, in this case, is that a Parrot is a Bird. 
# Any code where you use class Bird you could equally use class Parrot without changing 
# the desired outcome of your program.

# Composition is where one class contains the object of another class. 
# In this case, we could have a Bird class and a Tail class. 
# The composition relationship here would be that a Parrot has a tail so would inherit from both Bird and Tail. 
# However, a Kiwi does not have a tail, so would only inherit from Bird. 
# That way, you can have a Duck and a Parrot class that reuse Tail but are themselves not derived from each other. 
# A Parrot is not a Duck, but both of them have a Tail. 
# With composition, you cannot use class Tail interchangeably with Bird. 
# The Tail class is not a subclass of Bird.

# The purpose of both mixin and composite is to reduce the amount of unnecessary duplication of code.
# With the Bird example, you can have many bird subclasses, but if some of them share certain properties, 
# then there is the opportunity to move them into a class with a composite relationship. You could, for example, 
# reuse the Tail class in another program where you have a Reptile base class.


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Engine:
    def __init__(self, capacity, fuel):
        self.capacity = capacity
        self.fuel = fuel
    
class InternalCombustion(Vehicle, Engine):
    def __init__(self, make, model, capacity, fuel):
        Vehicle.__init__(self, make, model)
        Engine.__init__(self, capacity, fuel)
        
class Electric(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, make, model)
        
volkswagen = InternalCombustion("Volkswagen", "Golf", 1.7, "Diesel")
tesla = Electric("Tesla", "X")


# In this example, Electric inherits from Vehicle. 
# Therefore the tesla object is a Vehicle. 
# However, InternalCombustion class has a composition relationship with Engine. 
# The volkswagen has an engine, but it is not an engine. 
# The Engine class could be reused for a PowerBoat class without PowerBoat and InternalCombustion being derived from one another.

# In the runnable example, we extend our simple Human Resources application. 
# The first additional class is ExternalContract for employees who are not direct employees 
# of the company but are contract employees. 
# This has an instance attribute to take the cost of the contract and a method that returns that added to the employee salary.

# Finally, we have the ContractDeveloper class. 
# This is for developers who are not direct employees. 
# This has a composition relationship with ExternalContract. 
# A contract developer has an external contract. 
# A direct developer does not. 
# You can reuse this ExternalContract for any other job class you create.
# Here we have also included the HolidayMixin. This class uses composition and mixin. 
# The method details for ContractDeveloper inherits from Employee but also provides for the cost of the contract.

# We have instantiated two developers here, one direct and one contract. 
# See how their details differ. 
# Also, we use the method from the mixin to see how much annual leave they have accrued. 
# For the direct developer, you can also call the method to see their salary.



class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, fname, sname, no_of_years):
        # instance attribute
        self.fname = fname
        self.sname = sname
        self.no_of_years = no_of_years
        Employee.employee_no +=1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"First Name: {self.fname}\n Surname: {self.sname}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"

class ExternalContract:
    """
    Class for contract employees
    """

    def __init__(self, contract_cost):
        self.contract_cost = contract_cost

    def cost(self):
        """
        Returns the contract cost added to the salary
        """
        return self.contract_cost + 30000


class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    """
    def calculate_holidays(self, no_of_years):
        """
        Returns holidays as an integer
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if self.no_of_years < 3:
            bonus = holidays + 1
        elif self.no_of_years <= 5:
            bonus = holidays + 2
        elif self.no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class. 
    """
    def __init__(self, fname, sname, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, fname, sname, no_of_years)

    def calculate_salary(self):
        """
        Returns salary plus bonus as an integer
        """
        base = 30000
        if self.prog_language.lower() == 'python':
            bonus = base * 0.10
        else:
            bonus = 0
        return base + bonus

    def details(self):
        """
        Method to return direct developer details as a string
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}'


class ContractDeveloper(HolidayMixin, Employee, ExternalContract):
    """
    Class is subclass of Employee, composition relationship
    with ExternalContract and using HolidayMixin
    """
    def __init__(self, fname, sname, no_of_years, prog_language, contract_cost):
        self.prog_language = prog_language
        self.contract_cost = contract_cost
        Employee.__init__(self, fname, sname, no_of_years)   

    def details(self):
        """
        Returns inherited details plus contract cost
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}\n Contract cost: {ExternalContract.cost(self)}'


dev = DirectDeveloper("Eric", "Praline", 2, "python")
# There is no composition relationship here. A DirectDeveloper is an Employee
print(dev.details())
print(dev.calculate_holidays(dev.no_of_years))
print(f'${dev.calculate_salary()}')

contractor = ContractDeveloper("Luigi", "Vercotti", 10, "python", 100000)
# When the contractor details are printed the Contract cost is obtained from ExternalContract class
# There is a composition relationship as contractor has an ExternalContract
# However, an external contract is not an employee
# ExternalContract is an object that could be reused by many other objects. 
print(contractor.details())
# The mixin can also be used
print(contractor.calculate_holidays(contractor.no_of_years))

# challenge - mixins
class TicketMixin:
    """
    Mixin to calculate ticket price based on age
    """
    def calculate_ticket_price(self, age):
        self.age = age
        price = 0
        if self.age < 12:
            price = 0
        elif self.age < 18:
            price = 15
        elif self.age < 60:
            price = 20
        elif self.age >= 60:
            price = 10
        return price
        
class Customer(TicketMixin):
    """Create instance of Customer"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f'{self.name} age {self.age} ticket price is {self.calculate_ticket_price(self.age)}'


customer = Customer("Ryan Phillips", 22)
print(customer.describe())

# Superclassing: Accessing the Parent

# We have already looked at how to inherit properties from one class to another. 
# The class that inherits is the subclass. 
# Therefore, if you refer to the class, it is inheriting from the superclass. 
# Up till now in this lesson when referring to the superclass in a subclass, 
# we have explicitly used the superclass name in front of the inherited attributes or properties. 
# To improve the maintainability of your code, use the super() function in place of the superclass name. 
# Therefore, if you ever change the superclass you only then need to change the argument in the subclass 
# definition not everywhere else in the code.


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)

# As you can see the reference to superclass Rectangle is replaced with the function super() in the subclass Square.

# In the runnable example, we return to the Bird classes. 
# You can see the use of super() to denote which instance attributes are inherited from the superclass Bird. 
# It is also used in the subclass methods to inherit the superclass description method to avoid repetition of code.

class Bird(object):
    """
    Bird superclass
    """
    def __init__(self, kind, call):
        # instance attributes
        self.kind = kind
        self.call = call

    def description(self):
        """
        Returns description string including instance attributes
        """
        return f'A {self.kind} goes {self.call}'


class Fowl(Bird):
    """
    Subclass of the superclass Bird
    """
    def __init__(self, kind, call, type):
        self.fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds that includes\n'
                                       'turkey, grouse, chicken, New World quail and Old World quail,\n'
                                       'ptarmigan, partridge, pheasant, junglefowl and the Cracidae\n',
                           'waterfowl': 'Waterfowl is an order of birds that comprises about 180 living species\n'
                                        'in three families: Anhimidae (the screamers), Anseranatidae\n'
                                        '(the magpie goose), and Anatidae,the largest family, which\n'
                                        'includes over 170 species of waterfowl,\n'
                                        'among them the ducks, geese, and swans.\n'}
        self.type = type
        # Uses super() function to state kind, call from superclass Bird
        super().__init__(kind, call)


    def description(self):
        """
        Returns string from superclass description method and
        appends a string to include additional information
        """
        return f'{super().description()} \nSome interesting facts about the {self.kind} : A {self.kind} is of type {self.type}. {self.fowl_types[self.type.lower()]}'

class Seabird(Bird):
    """
    Subclass of Bird superclass for sea birds
    """
    def __init__(self, kind, call, diving_depth):
        # super() is used to denote what is inherited from Bird
        super().__init__(kind, call)
        self.diving_depth = diving_depth

    def get_description(self):
        """
        Returns description from superclass using super() function
        Appends additional information as a string
        """
        return f'{super().description()} and also, a {self.kind} dives to a depth of {self.diving_depth} metres.'


gannet = Seabird('Gannet', 'Squawk', 3)
print(gannet.get_description())

duck = Fowl('Mallard', 'Quack!', 'Waterfowl')
print(duck.description())

# super class challenge
class BaseOrderItem():
    """
    Creates instance of BaseOrderItem
    """
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
    
    """
    Returns total based on price * quantity ordered
    """
    def total_price(self):
        return self.price * self.quantity

# write your code here
class ShoeOrderItem(BaseOrderItem):
    """
    Creates instance of ShoeOrderItem
    """
    def __init__(self, product, price, quantity, size):
        super().__init__(product, price, quantity)
        self.size = size
        
    def describe(self):
        return f"Order: {self.product} in size {self.size}, quantity: {self.quantity}, total price: {self.total_price()}"
        

shoe_order = ShoeOrderItem("Ladies Nike Trainers", 40, 2, 42)
print(shoe_order.describe())

# Passing Methods Around

#One thing you may have noticed in the examples is that methods are passed around from superclass or mixin to subclass. 
# This is possible in Python as a method is itself an object. 
# Methods are functions within a class so in the same way functions are passed around so are methods.

class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call} and is {self.definition}" 


class Parrot(Bird):
    def __init__(self, color):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.color = color


parrot = Parrot('blue')
print(parrot.color)
print(parrot.description())

# import statement

# When you create a Python program, you split your code up into different files to avoid repetition. 
# These files are known as modules. We touched on this in the Frameworks, Modules And Libraries unit. 
# Python allows you to import entire modules or individual functions, classes or variables into other modules.

# Python has built-in modules that we can import from as well. We do this with the import statement.

# In the runnable example, we have a division function in a divide.py module. 
# Click on the Files button to see the other files. 
# In main.py, we have imported the division function from the divide.py module, 
# which allows us to use the division function using the division() syntax directly. 
# However, we do not have access to the mod function unless we also add a from divide import mod statement in main.py.

from divide import division


print(division(4, 2))


# challenge import statement

import helpers
list_integers = [1,2,3,4,5]



addition = helpers.add_integers(list_integers)
print(addition)

multiplication = helpers.multiply_intergers(list_integers)
print(multiplication)

# Math

# Python has a plethora of built-in libraries for everyday tasks. 
# One of the most useful is Math. 
# If you need to do a calculation in your code, then it is a good idea to import from this library, 
# rather than reinventing the wheel.



import math

print(math.pi)

print(math.sqrt(4))

#challenge math

round_up = math.ceil(num)
print(round_up)

round_down = math.floor(num)
print(round_down)

square_root = math.sqrt(round_down)
print(square_root)

# datetime

"""
In the runnable example, we have displayed the current date and time on the repl.it server where this code is running. 
The date contains a year, month, day, hour, minute, second and microsecond. 
The library contains methods to access that data. We have obtained the year and printed it to the console. 
A common usage of the datetime library is to get a readable string from the datetime object. 
There is a method called strftime() that takes a parameter format to return the string as you would like 
to display it to your user. In the first part of the runnable example we have shown the day of the week.

We can also access date information with python using datetime instance methods such as date() and time(). 
You can see these in action in the second part of the runnable example below.
"""

from datetime import datetime

x = datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

the_date = datetime.now().date()
print(the_date)

the_time = datetime.now().time()
print(the_time)


# challenge datetime

from datetime import datetime

# write your code here
today =datetime.now().date()
print(today)

# io

"""
There are many basic in/out (I/O) functions in Python, with which some at least you are already familiar. 
A print statement is the most basic output. 
You have also seen examples of taking input from a user with the input() function. 
These are, of course, only useful when using a command-line application where the input and output use the terminal. 
In real-world applications, you might also be reading from and writing to files on the computer where the code is running. We will cover this in more detail in an upcoming module.

In the runnable example, we have included a text file. 
The open() function is used to open this file and to let the computer know that this text file is currently in use 
by the main.py module. 
As we have assigned this to a variable f, we can then use the read() function to read the text and assign it to variable lines. 
We then use the close() function to close the file again. 
This is to ensure that other programs will be able to access it.
"""

f = open('source.txt')
lines = f.read()
f.close()
print(lines)

# io challenge 

file = open('lyrics.txt')
lyrics = file.read()
file.close()
print(lyrics)

# os

"""
The os library provides a way of using the operating system (os) functionality. 
 operating system is the software that interfaces between the hardware and user on a computer. 
 Common operating systems would be Windows, macOS, Linux or iOS. 
 A frequent use for this would be accessing the environment variables. 
 Every computer has a set of environment variables listing information on how the machine is set up. 
 Examples of this would be the directory structure of the home directory or the computers users profile.

"""

# In the runnable example, we use the get current working directory function getcwd() to find the 
# directory in which the python file is located. 
# We can also list the files or directories listdir() within a directory.


import os

print(os.getcwd())
print(os.listdir('/home/user'))


# os.path()

"""
Within the os library, there is a module named path. 
This allows you to manipulate the pathnames on the operating system of the computer on which you are running the code. 
This is useful when saving data to the local operating system. 
If you remember back to the CSS Essentials lessons getting the correct relative or absolute 
pathname was vital in linking files. 
The os.path() methods allow you to dynamically create path names so you can connect to files on the operating system 
and save files where you intend to.

"""

#In the runnable example, we have taken the absolute path and joined it with the current working directory. 
# This uses the join() method of the path module. 
# There is also a split() method allowing you to split a path.
# In this case, we have split the filename from the pathname and assigned them to a tuple. 
# The splitext() method allows you to split the module name from its file extension.

import os

# This is how you would join two paths in your code
print(os.path.join('/home/runner/', 'os'))

path = "/home/runner/os/main.py"
# Splits the path into a pair (head, tail) where the tail is the end of the pathname
# The tail is after the / and the head is the pathname up to that point 
(dirname, filename) = os.path.split(path)
print(f'The directory path is {dirname}')
print(f'The filename is {filename}')
# Splits the filename into a pair (root, ext)
# The root is before the dot and the ext contains the dot with the suffix after it
(module, extension) = os.path.splitext(filename)
print(f'The module is {module}')
print(f'Its file suffix is {extension}')


#random

"""
An everyday computing problem is making a random choice. 
Computers are not good at being random. 
The random library generates pseudo-random numbers that are suitable for most purposes. 
You can use these for games or simple statistical checks.

"""

import random

print(f'A random float between 0 & 1.0: {random.random()}')
print(f'A random int between 0 & 10: {random.randrange(11)}')
print('A random choice from a list: ' + random.choice(['paper', 'scissors', 'rock']))
deck = ['hearts', 'diamonds', 'spades', 'clubs']
random.shuffle(deck)
print(deck)

# random challenge

import random 

def ten_rand_nums():
    return [random.randrange(101) for i in range(0,10)]
    
result = ten_rand_nums()
print(result)

random.shuffle(result)
print(result)
