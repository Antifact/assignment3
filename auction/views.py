from flask import Blueprint, render_template, request, session

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index/show.html')

@bp.route('/watchlist')
def watchlist():
    return render_template('watchlist/show.html')

@bp.route('/item_details')
def item_details():
    return render_template('item_details/show.html')

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