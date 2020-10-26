from flask import Blueprint, render_template
from .models import Item, Gemstone, Metal

bp = Blueprint('item', __name__, url_prefix='/item_details')

@bp.route('/<id>') 
def show(id): 
    item = get_item()
    return render_template('item_details/show.html', item=item)

def get_item():
    item = Item("Gold Amber Ring", "https://i.pinimg.com/474x/b0/dc/40/b0dc40f5a5bc0ae02e2ba0dafe7926de.jpg", "Talisa", "Ring", "MaryP", 1, 2, 1992, "$120.00", "$230.35", "3.5cm", "8g", "Good", "Worn twice to parties")
    gem = Gemstone("Amber", "Gold Amber Ring", 1,"Rectangle", "Orange","n/a",  "2cm", "1cm", "0.5cm", "5g", "Rare quality")
    metal = Metal("Gold", "Gold Amber Ring", "gold", "14k", "copper", "3.5cm", "1cm", "4g")
    metal1 = Metal("Silver", "Gold Amber Ring", "silver", "n/a", "copper", "1cm", "1cm", "4g")
    item.set_items(gem)
    item.set_items(metal)
    item.set_items(metal1)
    return item