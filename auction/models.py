from .user import User
from datetime import datetime

class Item:
    def __init__(self, name, picture, brand, itemtype, owner, metalamount, gemamount, yrcreated, startprice, originalprice, size, weight, condition, description):
        self.name=name
        self.brand=brand
        self.itemtype=itemtype
        self.owner=owner
        self.metalamount=metalamount
        self.gemamount=gemamount
        self.yrcreated=yrcreated
        self.startprice=startprice
        self.originalprice=originalprice
        self.size=size
        self.weight=weight
        self.condition=condition
        self.description=description
        self.picture=picture

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Name: {0}, Picture: {1}, Brand: {2}, Type: {3}, Owner: {4}, Metal types: {5}, Gem types: {6}, Year created: {7}, ${8}, ${9}, Size: {10}, Weight: {11}, Condition: {12}, Description: {13}\n"
        str = str.format(self.name, self.picture, self.brand, self.itemtype, self.owner, self.metalamount, self.gemamount, self.yrcreated, self.startprice, self.originalprice, self.size, self.weight, self.condition, self.description)
        return str


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


class Bid:
    def __init__(self, item, user, bid_price, date_added):
        self.item=item
        self.user=user
        self.bid_price=bid_price
        self.date_added=date_added
        self.num_guests = 1

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Item: {0}, User: {1}, ${2}.00, {3}\n"
        str = str.format(self.item, self.user, self.bid_price, self.date_added)
        return str


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


class Watchlist:
    def __init__(self, item, user, date_added):
        self.item=item
        self.user=user
        self.date_added=date_added
        self.num_guests = 1

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Item: {0}, User: {1}, {2}\n"
        str = str.format(self.item, self.user, self.date_added)
        return str