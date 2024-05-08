from flask import Blueprint
from views.main_views import *

bp = Blueprint('main_bp', __name__, template_folder='templates')
bp.add_url_rule('/', 'homepage', homepage)
bp.add_url_rule('/login', 'login', login)
bp.add_url_rule('/auth', 'auth', auth)
bp.add_url_rule('/logout', 'logout', logout)
