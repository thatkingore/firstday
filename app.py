print("Hello World")

print("         ^")
print("        /|")
print("       / |")
print("      /  |")
print("     /   |")
print("    /    |")
print("   /     |")
print("  /      |")
print(" /_______|")

character_name = "Tom"
character_age = "50"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")

character_name = "John"
character_age = "35"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.lower().islower())
print(len(phrase))
print(phrase[0])
print(phrase.index(" "))
print(phrase.replace("Giraffe", "Elephant"))

pie = -3.142
print(pie)
print(abs(pie))

my_num = 5.2
print(my_num, "is my favourite number")

print(pow(3, 2))
print(max(3, 2))
print(min(3, 2))
print(round(pie))

from math import *

print(floor(abs(pie)))
print(ceil(abs(pie)))

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

num1 = input("Enter a whole number: ")
num2 = input("Enter another whole number: ")
result = int(num1) + int(num2)

print(result)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)
