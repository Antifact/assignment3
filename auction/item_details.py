from flask import Blueprint, render_template
from .models import Item

bp = Blueprint('item', __name__, url_prefix='/item_details')

@bp.route('/<id>') 
def show(id): 
    item = get_item()
    return render_template('item_details/show.html', item=item)

def get_item():
    name = "Gold Amber Ring"
    originalprice = "$230.35"

    item = Item(name, "https://i.pinimg.com/474x/b0/dc/40/b0dc40f5a5bc0ae02e2ba0dafe7926de.jpg", "Talisa", "ring", "MaryP", 1, 2, 1992, "$120.90", originalprice, "3.5cm", "8g", "Good", "Worn twice")

    return item