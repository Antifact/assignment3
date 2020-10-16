from datetime import datetime
from auction.user import User
from auction.gemstone import Gemstone
from auction.metal import Metal
from auction.bid import Bid
from auction.item import Item
from auction.watchlist import Watchlist

u = User()
u.register("amy", "1234abc", "amy399@gmail.com", "043928483", "12 Close St, Kangaroo Point, 4169")
print(u)

i = Item("Sapphire Ring", "Prouds", "ring", u.username, 1, 1, 1992, "120.00", "129.00", "3.5cm", "13g", "very good", "worn twice, great quality")
print(i)

gem = Gemstone("sapphire", i.name, 2, "square", "blue", "n/a", "1cm", "1cm", "0.5cm", "8g", "desc")
print(gem)

m = Metal("Sterling silver", i.name, "silver", "n/a", "copper", "12cm", "2cm", "5g")
print(m)

add_date = datetime(2020, 9, 23)
watch = Watchlist(i.name, u.username, add_date)
print(watch)

b = Bid(i.name, u.username, "127", add_date)
print(b)

