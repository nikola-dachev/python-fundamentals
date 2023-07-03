class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        selt.items = []

    def add_item(self,item):
        if self.capacity > len(self.items):
            self.items.append(item)
            self.capacity -=1
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '. join(items)}.\nCapacity left: {self.capacity}"