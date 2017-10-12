from flask import Blueprint
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
from api.v1.views.authentication import *  # noqa
