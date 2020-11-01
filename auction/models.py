from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'users'
    Username = db.Column(db.String(100), primary_key=True, unique=True, nullable=False)
    Password = db.Column(db.String(100), unique=True, nullable=False)
    Phone = db.Column(db.String(100), unique=True, nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Address = db.Column(db.String(100), unique=True, nullable=False)
    WatchlistNo = db.Column(db.Integer(), unique=True, nullable=False)
    UserNo = db.Column(db.Integer())

    comments = db.relationship('Comment', backref='user')

class Item(db.Model):
    __tablename__ = 'items'
    ItemNo = db.Column(db.String(80), primary_key=True, nullable=False)
    Picture = db.Column(db.String(400), nullable=False)
    ItemName = db.Column(db.String(80), nullable=False)
    Brand = db.Column(db.String(40), nullable=False)
    ItemType = db.Column(db.String(40), nullable=False)
    Owner = db.Column(db.Integer(), nullable=False)
    MetalAmount = db.Column(db.Integer(), nullable=False)
    GemAmount = db.Column(db.Integer(), nullable=False)
    YrCreated = db.Column(db.Integer(), nullable=False)
    OriginalPrice = db.Column(db.String(10), nullable=False)
    StartingPrice = db.Column(db.String(10), nullable=False)
    Size = db.Column(db.String(5), nullable=False)
    Weight = db.Column(db.String(5), nullable=False)
    Condition = db.Column(db.String(40), nullable=False)
    Description = db.Column(db.String(200), nullable=False)


    comments = db.relationship('Comment', backref='item')

    def __repr__(self):
        return "<Name: {}>".format(self.name)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.String, db.ForeignKey('users.UserNo'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.ItemNo'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)


    

# class User:

#     def __init__(self):
#         self.user_type='guest'

#     def register(self, name, password, email, phone, address):
#         self.username=name
#         self.password=password
#         self.email=email
#         self.phone=phone
#         self.address=address

#     def __repr__(self):
#         s = 'Name: {0}, Email: {1}, Phone: {2}, Address: {3}, Type: {4}\n'
#         s = s.format(self.username, self.email, self.phone, self.address, self.user_type)
#         return s


# class Item:

#     def __init__(self, name, picture, brand, itemtype, owner, metalamount, gemamount, yrcreated, startprice, originalprice, size, weight, condition, description):
#         self.name=name
#         self.brand=brand
#         self.itemtype=itemtype
#         self.owner=owner
#         self.metalamount=metalamount
#         self.gemamount=gemamount
#         self.gems=list()
#         self.metals=list()
#         self.items=list()
#         self.bids=list()
#         self.yrcreated=yrcreated
#         self.startprice=startprice
#         self.originalprice=originalprice
#         self.size=size
#         self.weight=weight
#         self.condition=condition
#         self.description=description
#         self.picture=picture

#     def set_gems(self, gem):
#         self.gems.append(gem)

#     def set_metals(self, metal):
#         self.metals.append(metal)

#     def set_items(self, item):
#         self.items.append(item)

#     def set_bids(self, bid):
#         self.bids.append(bid)

#     def get_item_details(self):
#         return str(self)

#     def __repr__(self):
#         str = "Name: {0}, Picture: {1}, Brand: {2}, Type: {3}, Owner: {4}, Metal types: {5}, Gem types: {6}, Year created: {7}, ${8}, ${9}, Size: {10}, Weight: {11}, Condition: {12}, Description: {13}\n"
#         str = str.format(self.name, self.picture, self.brand, self.itemtype, self.owner, self.metalamount, self.gemamount, self.yrcreated, self.startprice, self.originalprice, self.size, self.weight, self.condition, self.description)
#         return str


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

    def __init__(self, item, name, bid_price, date_added):
        self.item=item
        self.name=name
        self.bid_price=bid_price
        self.date_added=date_added

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Item: {0}, User: {1}, ${2}.00, {3}\n"
        str = str.format(self.item, self.name, self.bid_price, self.date_added)
        return str


class Gemstone:

    def __init__(self, name, item, amount, cuttype, colour, height, width, depth, weight):
        self.name=name
        self.item=item
        self.amount=amount
        self.cuttype=cuttype
        self.colour=colour
        self.height=height
        self.width=width
        self.depth=depth
        self.weight=weight

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Name: {0}, Item: {1}, Amount: {2}, Cut Type: {3}, Colour: {4}, Height: {5}, Width: {6}, Depth: {7}, Weight: {8}\n"
        str = str.format(self.name, self.item, self.amount, self.cuttype, self.colour, self.height, self.width, self.depth, self.weight)
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