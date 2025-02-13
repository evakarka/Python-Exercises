# Base class for items
class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} (Weight: {self.weight})"

# Derived class for weapons
class Weapon(Item):
    def __init__(self, name, weight, damage):
        super().__init__(name, weight)
        self.damage = damage

    def __str__(self):
        return f"{self.name} (Weight: {self.weight}, Damage: {self.damage})"

# Derived class for potions
class Potion(Item):
    def __init__(self, name, weight, effect):
        super().__init__(name, weight)
        self.effect = effect

    def __str__(self):
        return f"{self.name} (Weight: {self.weight}, Effect: {self.effect})"

# Inventory class
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item_name} from inventory.")
                return
        print(f"{item_name} not found in inventory.")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.items:
                print(item)

# Testing the inventory system
if __name__ == "__main__":
    # Create item instances
    sword = Weapon("Sword", 5, 10)
    shield = Weapon("Shield", 8, 0)
    bow = Weapon("Bow", 3, 6)
    staff = Weapon("Staff", 2, 8)
    healing_potion = Potion("Healing Potion", 1, "Restores 50 HP")
    mana_potion = Potion("Mana Potion", 1, "Restores 30 MP")

    # Create inventory
    inventory = Inventory()

    # Add items to inventory
    inventory.add_item(sword)
    inventory.add_item(shield)
    inventory.add_item(healing_potion)
    inventory.add_item(mana_potion)
    inventory.add_item(staff)

    # Display inventory
    inventory.display_inventory()

    # Remove an item and display again
    inventory.remove_item("Sword")
    inventory.display_inventory()

    # Try to remove an item not in inventory
    inventory.remove_item("Bow")
