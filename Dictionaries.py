rooms = {
    "stone room": "You are in a dark room.",
    "large room": "You are in a larger furnished room",
    "bin room": "you are in a room lined with bins. Rubbish is scattered everywhere"
}

room_name = input("Enter a room name: ").lower()

if room_name in rooms:
    print(rooms[room_name])
else:
    print("You made that up.")

print("-----------------------")

weapons = {
    "dagger": "A small blade. Easy to conceal. Easy to wield.",
    "revolver": "A rusted revolver with intricate line engravements. 5 bullet capacity.",
    "nuclear warhead": "A massive, unwieldy atomic bomb. You can barely lift it up."
}

weapon = input("Choose a weapon: ").lower()

if weapon in weapons:
    print(weapons[weapon])
else:
    print("You made that up.")
