from flask import Blueprint

# Create a Blueprint named 'app_views'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import any endpoints you create
from . import index

