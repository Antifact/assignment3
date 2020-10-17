from flask import Blueprint
from flask import render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')

@bp.route('/item_details')
def item_details():
    return render_template('item_details.html')

@bp.route('/list_item')
def list_item():
    return render_template('list_item.html')