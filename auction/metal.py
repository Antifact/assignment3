from .item import Item

class Metal:
    def __init__(self, name, item, metaltype, karat, plating, length, width, weight):
        self.name=name
        self.item=item
        self.metaltype=metaltype
        self.karat=karat
        self.plating=plating
        self.length=length
        self.width=width
        self.weight=weight

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Name: {0}, Item: {1}, Type: {2}, Karat: {3}, Plating Material: {4}, Length: {5}, Width: {6}, Weight: {7}\n"
        str = str.format(self.name, self.item, self.metaltype, self.karat, self.plating, self.length, self.width, self.weight)
        return str