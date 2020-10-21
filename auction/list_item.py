from flask import Blueprint, render_template

bp = Blueprint('item', __name__, url_prefix='/list_item')

@bp.route('/<id>') 
def show(id):
    return render_template('list_item/show.html')