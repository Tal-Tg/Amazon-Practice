from bisect import insort

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self):
        return f"Item: {self.name} -> {self.price}"
    
    def __lt__(self, other):
        if self.price != other.price:
            return self.price < other.price
        return self.name < other.name



class Mart:
    
    def __init__(self):
        self.items = []
        self.index = -1
    
    def insert(self, name, price):
        item = Item(name, price)
        insort(self.items, item)
    
    def view(self):
        self.index += 1
        if self.index == len(self.items):
            return 'None'
        return self.items[self.index].name
    
    
    
m = Mart()
m.insert('Coffee', 3)
m.insert('Milk', 4)
print(m.view())

m.insert('Gum', 1)
m.insert('Pizza', 5)
print(m.view())