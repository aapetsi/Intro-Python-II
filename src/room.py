# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None
        self.items = items

    def add_item(self, name, desc):
        new_item = Item(name, desc)
        self.items.append(new_item)

    def __str__(self):
        item_list = [item for item in self.items]
        return f"Name: {self.name}; description: {self.description}; items: {item_list}\n"
