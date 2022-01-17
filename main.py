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









