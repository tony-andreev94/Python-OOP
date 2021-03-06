class Store:

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.current_quantity = 0

    @staticmethod
    def from_size(name: str, type: str, size: int):
        return Store(name, type, int(size/2))

    def add_item(self, item_name: str):
        if not self.capacity > self.current_quantity:
            return f"Not enough capacity in the store"

        self.current_quantity += 1
        if item_name in self.items.keys():
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items.keys() and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            self.current_quantity -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))

