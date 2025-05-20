# rooms = {
#     "stone room":
#         {"description": "You are in a dark room.",
#          "items": ["key"],
#          "exits": ["large room"]},
#     "large room":
#         {"description": "You are in a larger furnished room",
#          "items": ["dagger", "scrawled note", "match box"],
#          "exits": ["stone room", "bin room"]},
#     "bin room":
#         {"description": "you are in a room lined with bins. Rubbish is scattered everywhere",
#          "items": ["revolver"],
#          "exits": ["large room"]}
# }
#
# room_name = input("Enter a room name: ").lower()
#
# if room_name in rooms:
#     print("description: " + (rooms[room_name]["description"]))
#     print("items: " + ", ".join(rooms[room_name]["items"]))
#     print("exits: " + ", ".join(rooms[room_name]["exits"]))
# else:
#     print("You made that up.")
#
# print("-----------------------")
#
# weapons = {
#     "dagger": "A small blade. Easy to conceal. Easy to wield.",
#     "revolver": "A rusted revolver with intricate line engravements. 5 bullet capacity.",
#     "nuclear warhead": "A massive, unwieldy atomic bomb. You can barely lift it up."
# }
#
# weapon = input("Choose a weapon: ").lower()
#
# if weapon in weapons:
#     print(weapons[weapon])
# else:
#     print("You made that up.")
# print("-----------------------")

areas = {
    "cell":
        {"description": "A small dank room with a stained bed and window with iron bars.",
         "items": ["key"],
         "exits": {
            "north": "wall",
            "east": "window",
            "south": "bed",
            "west": "door"}}

}

print(areas["cell"]["exits"])


