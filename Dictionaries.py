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
