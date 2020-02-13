# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def add_to_inventory(self, item):
        new_item = Item(item.name, item.description)
        self.inventory.append(new_item)
    
    def get_item(self, item):
        if item in [x.name for x in self.current_room.items]:
            self.current_room.items.remove(item)
            self.inventory.append(item)

    def __str__(self):
        return f"Name: {self.name}; current room: {self.current_room}"
