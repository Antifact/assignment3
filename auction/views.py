from flask import Blueprint, render_template, request, session
from .models import Item, Gemstone, Metal


def get_item():
    item = Item("Gold Amber Ring", "https://i.pinimg.com/474x/b0/dc/40/b0dc40f5a5bc0ae02e2ba0dafe7926de.jpg", "Talisa", "Ring", "MaryP", 1, 2, 1992, "$120.00", "$230.35", "3.5cm", "8g", "Good", "Worn twice to parties")
    gem = Gemstone("Amber", "Gold Amber Ring", 1,"Rectangle", "Orange","n/a",  "2cm", "1cm", "0.5cm", "5g", "Rare quality")
    metal = Metal("Gold", "Gold Amber Ring", "gold", "14k", "copper", "3.5cm", "1cm", "4g")
    metal1 = Metal("Silver", "Gold Amber Ring", "silver", "n/a", "copper", "1cm", "1cm", "4g")
    item.set_gems(gem)
    item.set_metals(metal)
    item.set_metals(metal1)
    return item

bp = Blueprint('main', __name__)

@bp.route('/')
def show():
    item = get_item()
    return render_template('index/show.html', item=item)

@bp.route('/watchlist/<id>')
def watchlist(id):
    item = get_item()
    return render_template('watchlist/show.html', item=item)

@bp.route('/item_details/<id>')
def item_details(id):
    item = get_item()
    return render_template('item_details/show.html', item=item)

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