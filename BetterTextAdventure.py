playing = False

areas = {
    "stone room":
        {"description": "The room is dark with stone walls and a concrete floor."
                        "The bed you woke up from sits against one wall."
                        "There's a small grimy window opposite."
                        "An old paint chipped door looks like your only exit",
         "items": [],
         "exits": ["larger room"]}
}
print("Welcome!")
print("Type 'help' at any point to see the list of commands.")
print("Ready to play?")
answer = input("> ").strip().lower()
if answer in ["yes", "y"]:
    playing = True
    print("You wake up in a dark stone room.")
    print("It smells horrid. Like rotten milk and soil.")
else:
    print("Maybe next time! Goodbye!")

while playing:
    command = input("> ").strip().lower()
    if command == "help":
        print("You can type:")
        print("look around")
        print("go [north/east/south/west]")
        print("search [something]")
        print("inventory")
        print("quit/leave - to quit the game")

