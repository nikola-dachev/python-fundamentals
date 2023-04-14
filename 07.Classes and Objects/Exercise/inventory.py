class Inventory:
    def __init__(self,capacity):
        self.__capacity = capacity
        self.items =[]
        self.current_capacity = self.__capacity

    def add_item(self,item: str):

        if self.current_capacity <= 0:
            return f"not enough room in the inventory"

        self.items.append(item)
        self.current_capacity -= 1

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.current_capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
