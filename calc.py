num1 = input("Enter a whole number: ")
num2 = input("Enter another whole number: ")
result = int(num1) + int(num2)

print(result)

num1 = input("What is your favourite number: ")
num2 = input("Another number: ")
result = float(num1) + float(num2)

print(result)

num1 = float(input("Last time, promise, enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("And enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")