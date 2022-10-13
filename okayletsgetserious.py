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
if hungry and meat:
    print("Can I have steak please")
elif hungry and not(meat):
    print("Hmm how about spaghetti & meatballs")
else:
    print("Oh a salad!")
