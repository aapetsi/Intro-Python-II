from room import Room
from player import Player
from item import Item

# Declare items
items = [
    Item('umbrella', 'test description'),
    Item('knife', 'test2 description'),
    Item('watch', 'test3 description'),
    Item('fork', 'test4 descritpion'),
    Item('spoon', 'test5 description')
]
# print(items[0])

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", items),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
    falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from
    west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Apetsi", room["outside"])
game_over = False
directions = ["n", "s", "e", "w"]

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# direction = input("Enter a direction to move: ")

while not game_over:
    print(f"You are currently in {player.current_room.name}\n")
    print(f"Description: {player.current_room.description}\n")
    print(f"These are the items in {player.current_room.name}")
    for item in player.current_room.items:
        print(item.name)
    print("To move in any direction, use either of n, s, e, w\n")
    print("Enter q or quit to exit\n")

    direction = input("Enter a direction to move: ")

    if direction == 'q' or "quit":
        print("See you next time")
        game_over = True
    elif direction not in directions:
        print("Enter a valid direction\n")
    else:
        direction += "_to"
        if getattr(player.current_room, direction) is None:
            print('No room in that direction, please try again')
        else:
            player.current_room = getattr(player.current_room, direction)
