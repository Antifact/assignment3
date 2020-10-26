from flask import Blueprint, render_template
from .models import Item, Gemstone, Metal

bp = Blueprint('item', __name__, url_prefix='/item_details')

