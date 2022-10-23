def say_hi(name, age):
    print("Oh hello " + name + ", you are " + str(age))

say_hi("ore", 23)
say_hi("twinnie", 22)

def cube(num):
    return num*num*num
result = cube(4)

print(cube(3))
print(result)

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

# Function to compare int using IF statements

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(4, 3, 1))
