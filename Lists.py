print("Lists and accessing specific indexes")

main_characters = ["Dan", "Zenith", "Brutus", "Clara", "Sid"]

print(main_characters)

print(main_characters[0])

print(main_characters[-1])

print(main_characters[1:])

print(main_characters[1:3])

print(main_characters[-1:])

print(main_characters[-3:])

print("--------------------------")
print("Modifying values within a list")

print(main_characters)

main_characters[1] = "Zenith (Ascended)"

print(main_characters)

print(main_characters[1])

print("--------------------------")
print("Other list functions")

lucky_numbers = [6, 51, 19, 25, 2, 91]

print(lucky_numbers)

main_characters.extend(lucky_numbers)

print(main_characters)

main_characters.append("Altair")

print(main_characters)

main_characters.insert(1, "Clatt")

print(main_characters)

main_characters.remove("Clatt")

print(main_characters)

main_characters.clear()

print(main_characters)

main_characters = ["Dan", "Zenith", "Brutus", "Clara", "Sid"]

print(main_characters)

main_characters.pop()

print(main_characters)

main_characters.append("Sid")

print(main_characters.index("Zenith"))

print(main_characters.count("Brutus"))

main_characters.sort()

print(main_characters)

lucky_numbers.sort()

print(lucky_numbers)

lucky_numbers.reverse()

print(lucky_numbers)

main_characters2 = ["Dan", "Zenith", "Brutus", "Clara", "Sid"]

main_characters2.insert(1, "Zenith (Ascended)")
main_characters2.remove("Zenith")

print(main_characters2)

print(main_characters)

main_characters2.sort()

print(main_characters2)




