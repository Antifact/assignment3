from flask import Blueprint, render_template, request, session
from .models import Item, Gemstone, Metal

bp = Blueprint('main', __name__)

def get_item():
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
    
    item = Item(name, picture, brand, itemtype, owner, metalamount, gemamount, yrcreated, startprice, originalprice, size, weight, condition, description)
    return item

def get_gem():
    name = "Amber"
    amount= 1
    cuttype="rectangle"
    colour="burnt orange"
    clarity="n/a"
    height="2.5cm"
    width="1.5cm"
    depth="0.5cm"
    weight="5g"
    description="Validated from Jewels Australia"
    
    gem = Gemstone(name, "Gold Amber Ring", amount, cuttype, colour, clarity, height, width, depth, weight, description)
    return gem

def get_metal():
    name="14K Yellow Gold"
    metaltype="Gold"
    karat="14k"
    plating="copper"
    length="4cm"
    width="1.3cm"
    weight="8g"

    metal = Metal(name, "Gold Amber Ring", metaltype, karat, plating, length, width, weight)
    return metal

@bp.route('/')
def index():
    item = get_item()
    return render_template('index/show.html', item=item)

@bp.route('/watchlist')
def watchlist():
    item = get_item()
    return render_template('watchlist/show.html', item=item)

@bp.route('/item_details')
def item_details():
    item = get_item()
    gem = get_gem()
    metal = get_metal()
    return render_template('item_details/show.html', item=item, gem=gem, metal=metal)

@bp.route('/list_item')
def list_item():
    return render_template('list_item/show.html')

@bp.route('/login', methods=['GET' , 'POST'])
def login():
    session['email']=request.values.get('email')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)