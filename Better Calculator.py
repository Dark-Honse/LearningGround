print("A better calculator")

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
ops = ["+", "-", "*", "/"]

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Invalid operator")

if op == "+" or op == "-" or op == "*" or op == "/":
    print(result)
