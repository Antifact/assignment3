from .models import Item
from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/index')

@bp.route('/<id>') 
def show(id): 
    index = get_index()
    return render_template('index/show.html', index=index)

def get_index():
    name = "Gold Amber Ring"
    originalprice = "$230.35"
    picture = "https://i.pinimg.com/474x/b0/dc/40/b0dc40f5a5bc0ae02e2ba0dafe7926de.jpg"
    brand = "Talisa"
    itemtype = "ring"
    owner = "MaryP"
    metalamount = 1
    gemamount = 2
    yrcreated = 1992 
    startprice = "$120.00" 
    size = "3.5cm" 
    weight = "8g"
    condition = "Good"
    description = "Worn twice to parties"
    
    index = Item(name, picture, brand, itemtype, owner, metalamount, gemamount, yrcreated, startprice, originalprice, size, weight, condition, description)
    return index