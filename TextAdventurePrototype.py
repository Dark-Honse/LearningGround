playing = False

import random

inventory = []
unknown_response = ["huh?", "I don't understand that..", "try again chief"]
unknown_count = 0

player_location = ""
areas = {
    "cell":
        {"description": """A small dank room with a stained bed and a grimy window with iron bars.
An old paint chipped door is to your left.""",
         "items": ["key"],
         "exits": {
            "north": "wall",
            "east": "window",
            "south": "bed",
            "west": "door"}}

}

def look_around(location):
    print(areas[location]["items"])
door_locked = True
bed_found = False
door_found = False

print("Welcome")
print("Ready to play?")
response = input("> ")
if response.lower() == "yes" or response.lower() == "y":
    playing = True
    player_location = "cell"
    print("You are in a dark room")

while playing:
    command = input("> ").strip().lower()
    if command in ["quit", "stop playing", "exit"]:
        playing = False
        print("Thanks for playing!")

    elif command == "help":
        print("You can:.. ")
        print("'Look around'")
        print("'Inventory'")
        print("'Go -direction-'")
        print("'Quit'")

    elif command == "inventory":
        if len(inventory) == 0:
            print("You have nothing.")
            print("Broke ass.")
        else:
            print("You have: " + ", ".join(inventory))

    elif command == "look around":
        look_around(player_location)
        bed_found = True
        door_found = True

    elif command == "go north":
        print("You are standing in front of a nasty, stained wall.")
        print("It doesn't smell too good.")

    elif command == "go east":
        print("You can't see out of this window very well.")
        print("It looks like it doesn't know what soap is.")

    elif command == "go west":
        print("From close, it looks like some of the marks")
        print("on this door were intentional.")
        door_found = True

    elif command == "try door" or command == "open door":
        if door_found:
            if door_locked:
                print("The door is locked")
            else:
                print("The door creaks open...")
                print("You have escaped the room...")
                playing = False
        else:
            print("What door?")

    elif command == "use key":
        if "key" in inventory:
            if door_found:
                if door_locked:
                    print("You unlocked the door with the key.")
                    door_locked = False
                elif not door_locked:
                    print("You already unlocked the door")
            else:
                print("You stare at the key quizzically.")
        else:
            print("What key?")


    elif command == "go south":
        print("A bed. It is low and lumpy.")
        print("That dull orange stain makes you cringe.")
        bed_found = True

    elif command == "search bed":
        if bed_found == True and "key" not in inventory:
            print("You found a key under the pillow!")
            inventory.append("key")
        elif bed_found == True and "key" in inventory:
            print("There's nothing else here.")
            print("Only that nasty stain...")
        else:
            print("What bed?")


    else:
        print(random.choice(unknown_response))
        unknown_count += 1
        if unknown_count <5:
            print(random.choice(unknown_response))

        else:
            print("You're not cut out for this.")







