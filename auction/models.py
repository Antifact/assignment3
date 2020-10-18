from .user import User

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