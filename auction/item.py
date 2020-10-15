from .user import User

class Item:
    def __init__(self, name, brand, itemtype, user, metalamount, gemamount, yrcreated, startprice, originalprice, size, weight, condition, description):
        self.name=name
        self.brand=brand
        self.itemtype=itemtype
        self.user=user
        self.metalamount=metalamount
        self.gemamount=gemamount
        self.yrcreated=yrcreated
        self.startprice=startprice
        self.originalprice=originalprice
        self.size=size
        self.weight=weight
        self.condition=condition
        self.description=description

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Name: {0}, Brand: {1}, Type: {2}, Owner: {3}, Metal types: {4}, Gem types: {5}, Year created: {6}, ${7}, ${8}, Size: {9}, Weight: {10}, Condition: {11}, Description: {12}\n"
        str = str.format(self.name, self.brand, self.itemtype, self.user, self.metalamount, self.gemamount, self.yrcreated, self.startprice, self.originalprice, self.size, self.weight, self.condition, self.description)
        return str