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