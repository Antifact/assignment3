from .models import Item
from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')
