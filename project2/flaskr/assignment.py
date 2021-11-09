import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from flaskr.db import get_db

bp = Blueprint('assignment', __name__, url_prefix="/")

@bp.route('/assignment', methods=['GET'])
def assignment():
  return render_template('assignment/home.html')
