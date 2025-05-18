print("Exploring functions")

def sayhi():
    print("Hello User")

sayhi()

print("-----------------")

def sayhi1(name):
    print("Hello " + name)

sayhi1("Peter")
sayhi1("Daniel")

print("------------------")

def cube(num):
    return num*num*num

print(cube(6))

def cube2(num):
    return num*num*num

result = cube2(5)
print(result)

print("-------------------")
print("if statements")

is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")

