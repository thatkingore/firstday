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