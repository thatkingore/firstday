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

name = input("What is your name: ")
age = input("What is your age: ")
print("Hello " + name + "! You are " + age)

num1 = input("Enter a whole number: ")
num2 = input("Enter another whole number: ")
result = int(num1) + int(num2)

print(result)

num1 = input("What is your favourite number: ")
num2 = input("Another number: ")
result = float(num1) + float(num2)

print(result)

colour = input("What is your favourite colour: ")
plural_noun = input("Enter a noun in plural form: ")
celebrity = input("Who is your favourite celebrity: ")


print("Roses are " + colour)
print(plural_noun + " are blue")
print("I love " + celebrity)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kunmi", "Edet", "Motola", "Rieme", "Baba"]

print(friends[2])
print(friends[1:4])

friends.append("Creed")
friends.insert(2, "Baba")
friends.remove("Rieme")
friends.pop()
friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()
friends.extend(lucky_numbers)

friends2 = friends.copy()

print(friends2)
print(friends2.index(42))
print(friends2.count("Baba"))

friends2.clear()

coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[1])
