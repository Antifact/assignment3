from .item import Item

class Gemstone:
    def __init__(self, name, item, amount, cuttype, colour, clarity, height, width, depth, weight, description):
        self.name=name
        self.item=item
        self.amount=amount
        self.cuttype=cuttype
        self.colour=colour
        self.clarity=clarity
        self.height=height
        self.width=width
        self.depth=depth
        self.weight=weight
        self.description=description

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Name: {0}, Item: {1}, Amount: {2}, Cut Type: {3}, Colour: {4}, Clarity: {5}, Height: {6}, Width: {7}, Depth: {8}, Weight: {9}, Description: {10}\n"
        str = str.format(self.name, self.item, self.amount, self.cuttype, self.colour, self.clarity, self.height, self.width, self.depth, self.weight, self.description)
        return str