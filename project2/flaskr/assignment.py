import functools
import json
from flaskr.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from flaskr.db import get_db

bp = Blueprint('assignment', __name__, url_prefix="/")

@bp.route('/assignment', methods=['GET'])
def assignment():
  return render_template('assignment/index.html')

@bp.route('/assignment/example_query_1', methods=['GET'])
def example_query_1():
  db = get_db()
  cur = db.cursor()
  rows = cur.execute(
    '''
    SELECT VehicleID as VIN, Description, Year,
      CASE
          WHEN Type = 1 THEN 'Compact'
          WHEN Type = 2 THEN 'Medium'
          WHEN Type = 3 THEN 'Large'
          WHEN Type = 4 THEN 'SUV'
          WHEN Type = 5 THEN 'Truck'
          WHEN Type = 6 THEN 'VAN'
      END, 
      CASE
          WHEN Category = 0 THEN 'Basic'
          WHEN Category = 1 THEN 'Luxury'
      END 
    FROM vehicles
    '''
  ).fetchall()
  data = []
  for row in rows:
    data.append([x for x in row]) # or simply data.append(list(row))
  return json.dumps(data)

@bp.route('/assignment/example_query_2', methods=['GET'])
def example_query_2():
  db = get_db()
  cur = db.cursor()
  rows = cur.execute(
    '''
    SELECT *
    FROM customers
    '''
  ).fetchall()
  data = []
  for row in rows:
    data.append([x for x in row]) # or simply data.append(list(row))
  return json.dumps(data)
