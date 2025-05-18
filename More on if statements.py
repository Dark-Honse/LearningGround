is_red = False
is_blue = False

if is_red and is_blue:
    print("The car is red and blue")
elif is_red and not is_blue:
    print("The car is red")
elif not is_red and is_blue:
    print("The car is blue")
else:
    print("The car is neither red nor blue")
    car_colour = input("What is the colour of the car? ")
    print(f"The car is {car_colour}")
    if car_colour.lower() == "red" or car_colour.lower() == "blue":
        print("You wasted my time a little bit.")

print("-------------------")
print("max number function using comparisons")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(50, 999, 60))

print("-------------------")

