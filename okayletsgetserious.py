# Functions

def say_hi(name, age):
    print("Oh hello " + name + ", you are " + str(age))

say_hi("ore", 23)
say_hi("twinnie", 22)

def cube(num):
    return num*num*num
result = cube(4)

print(cube(3))
print(result)

# IF statements

hungry = False
if hungry:
    print("Get some brekky :)")

cloudy = True

if cloudy:
    print("Bring an umbrella")
else:
    print("Sunglasses babe")

if hungry or cloudy:
    print("What is going on today?")
else:
    print("You're good baby girl, you're good")

if hungry and cloudy:
    print("Very very weird")
else:
    print("Don't even worry about it")

meat = False
if hungry and steak:
    print("Can I have steak please")
elif hungry and not(steak):
    print("Hmm how about spaghetti & meatballs")
else:
    print("Oh a salad!")

# Function to compare integers (int) using IF statements

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(4, 3, 1))

# WHILE loop

i = 1
while i <= 10:
    print(i)
    i += 1

print("End of loop.")

# FOR loop

for letter in "Black Girls In Tech":
    print(letter)

# FOR loop and arrays
friends = ["Rieme", "Baba", "Motola", "Tao", "Aiss"]
for friend in friends:
    print(friend)

# FOR loop and range of numbers
for index in range(10):
    print(index)
for index in range(3, 10):
    print(index)
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")

# FOR loop and range of numbers to create an exponent function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))

# 2D Lists and Nested FOR loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    for col in row:
        print(col)

# Accounting for errors using TRY EXCEPT and err

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
# Using err
except ZeroDivisionError as err:
    print(err)
# Using an input
except ValueError:
    print("Invalid Input")
    

'''

# Reading files

# Opening the file
employee_file = open("employees.txt", "r")

# to just read
open("employees.txt", "r")
# to just write
open("employees.txt", "w")
# to read and write
open("employees.txt", "r+")
# to append
open("employees.txt", "a")

# Check if the file can be read from
print(employee_file.readable())

# Reading a particular line from the file starting from the first line
print(employee_file.readline())
# Reading the second line
print(employee_file.readline())

# Reading a particular line using its index in the array
print(employee_file.readline()[1])

for employee in employee_file.readlines():
    print(employee)

# Closing the file
employee_file.close

# to add a webpage (example)
employee_file = open("employees.txt", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close

'''

import useful_stuff

print(useful_stuff.roll_dice(10))

'''
https://docs.python.org/py-modindex
'''

from student import student

student1 = student("Ore", "Mathematics BSc", 3.1, False)
print(student1.degree)

