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
    if car_colour == "red" or car_colour == "blue":
        print("You wasted my time a little bit.")

