from datetime import datetime
from .item import Item
from .user import User

class Bid:
    def __init__(self, item, user, date_added):
        self.item=item
        self.user=user
        self.date_added=date_added
        self.num_guests = 1

    def get_item_details(self):
        return str(self)

    def __repr__(self):
        str = "Item: {0}, User: {1}, {3}\n"
        str = str.format(self.item, self.user, self.date_added)
        return str