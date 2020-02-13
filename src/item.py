class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item):
        print(f"You have picked up {item}")
    
    def on_drop(self, item):
        print(f"You have dropped {item}")

    def __str__(self):
        return f"Name: {self.name}; Description: {self.description}"