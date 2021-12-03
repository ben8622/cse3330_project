import functools
import json
from datetime import datetime
from flaskr.db import get_db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('assignment', __name__, url_prefix="/")

def select_query(query):
  db = get_db()
  cur = db.cursor()
  rows = cur.execute(query).fetchall()

  data = []
  for row in rows:
    data.append([x for x in row])
  
  return json.dumps(data)

def _select_query(query):
  db = get_db()
  cur = db.cursor()
  rows = cur.execute(query).fetchall()

  data = []
  for row in rows:
    data.append([x for x in row])
  
  return data

def get_vehicle_type_and_category(vehicle_id):
  t = _select_query(f"""
     SELECT Type, Category
     FROM vehicles
     WHERE VehicleID = '{vehicle_id}'
     """)
  return (t[0][0], t[0][1])

@bp.route('/assignment', methods=['GET'])
def assignment():
  return render_template('assignment/index.html')

@bp.route('/assignment/example_query_1', methods=['GET'])
def example_query_1():
  return select_query(
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
  )

@bp.route('/assignment/example_query_2', methods=['GET'])
def example_query_2():
  return select_query(
    '''
    SELECT *
    FROM customers
    '''
  )

@bp.route('/assignment/example_query_3', methods=['GET'])
def example_query_3():
  return select_query(
    '''
    SELECT COUNT(*)
    FROM rentals
    '''
  )

@bp.route('/assignment/requirement1', methods=['POST'])
def requirement1():
  customers = _select_query(
    """
    SELECT *
    FROM customers
    ORDER BY CustId
    """
  )
  last_id = customers[-1][0]

  cust_id = last_id + 1
  name = request.form["name"]
  phone = request.form["phone"]
  insert_string = f"INSERT INTO customers VALUES ({cust_id},'{name}','{phone}')"

  db = get_db()
  cursor = db.cursor()
  cursor.execute(insert_string).fetchall()
  db.commit()

  cursor.close()
  db.close()

  return json.dumps("")

@bp.route('/assignment/requirement2', methods=['POST'])
def requirement2():
  vehicle_id = request.form["vehicleId"]
  description = request.form["description"]
  year = request.form["year"]
  type = request.form["type"]
  category = request.form["category"]
  insert_string = f"INSERT INTO vehicles VALUES ('{vehicle_id}','{description}','{year}', {type}, {category})"

  db = get_db()
  cursor = db.cursor()
  cursor.execute(insert_string).fetchall()
  db.commit()

  cursor.close()
  db.close()

  return json.dumps("")

@bp.route('/assignment/requirement3', methods=['POST'])
def requirement3():

  vehicle_id = request.form["vehicleId"]
  customer_id = request.form["customerId"]
  start_date = request.form["startDate"]
  return_date = request.form["returnDate"]
  rental_type = request.form["rentalType"]
  pay_now = request.form["payNow"]

  ## Grab todays date (when it was ordered) and payment date if today
  order_date = datetime.today().strftime('%Y-%m-%d') 
  payment_date = f"'{datetime.today().strftime('%Y-%m-%d')}'" if  pay_now == '1' else "NULL"

  # Calculate quantity
  days_renting = (datetime.fromisoformat(return_date) - datetime.fromisoformat(start_date)).days
  quantity = round(days_renting / int(rental_type))

  # Grab the vehicles rate
  vehicle_type, vehicle_category = get_vehicle_type_and_category(vehicle_id)
  rental_type_string = "Daily" if rental_type == "1" else "Weekly"
  rate = _select_query(
    f"""
    SELECT {rental_type_string}
    FROM rates
    WHERE Type = {vehicle_type} AND Category = {vehicle_category}
    """
  )[0][0]

  total_amount = rate * quantity

  insert_string = f"""
    INSERT INTO rentals VALUES 
    (
      {customer_id},
      '{vehicle_id}',
      '{start_date}',
      '{order_date}',
      {rental_type},
      {quantity},
      '{return_date}',
      {total_amount},
      {payment_date}
    )
    """
  
  print(insert_string)

  db = get_db()
  cursor = db.cursor()
  cursor.execute(insert_string).fetchall()
  db.commit()

  cursor.close()
  db.close()

  return json.dumps("")

@bp.route('/assignment/requirement4', methods=['POST'])
def requirement4():

  # db = get_db()
  # cursor = db.cursor()
  # cursor.execute(insert_string).fetchall()
  # db.commit()

  # cursor.close()
  # db.close()

  return json.dumps("")

@bp.route('/assignment/requirement5a', methods=['POST'])
def requirement5a():
  customer_id = request.form["customerId"]
  name = request.form["name"]

  ## Construct the WHERE clause
  where_clause = ""
  if(customer_id != "" and name != ""):
    where_clause = f"WHERE CustomerId = {customer_id} AND CustomerName LIKE '%{name}%'"
  elif(customer_id != ""):
    where_clause = f"WHERE CustomerId = {customer_id}"
  elif(name != ""):
    where_clause = f"WHERE CustomerName LIKE '%{name}%'"
  
  select_str = """
    SELECT CustomerId, CustomerName, SUM(RentalBalance)
    FROM vRentalInfo
    """
  select_str = select_str + where_clause + "GROUP BY CustomerId"

  return select_query(select_str)

@bp.route('/assignment/requirement5b', methods=['POST'])
def requirement5b():
  vin = request.form['vin']
  desc = request.form['description']

  ## Construct the WHERE clause
  where_clause = ""
  if(vin != "" and desc != ""):
    where_clause = f"WHERE VIN = {Vin} AND Description LIKE '%{desc}%'"
  elif(vin != ""):
    where_clause = f"WHERE CustomerId = {vin}"
  elif(desc != ""):
    where_clause = f"WHERE Description LIKE '%{desc}%'"

  select_str = """
    SELECT VIN, 
      vehicles.Description,
      SUM(rentals.TotalAmount)/SUM(rentaltype*qty) As DailyAvg,
      SUM(rentaltype*qty) as Days,
      SUM(rentals.TotalAmount) as Total
    FROM vRentalInfo
    JOIN vehicles ON vehicles.VehicleId = vRentalInfo.VIN
    LEFT JOIN rentals On vRentalInfo.VIN = rentals.VehicleId AND vRentalInfo.ReturnDate = rentals.ReturnDate
  """

  select_str = select_str + where_clause + "GROUP BY vehicles.VehicleID"

  return select_query(select_str)


  # db = get_db()
  # cursor = db.cursor()
  # cursor.execute(insert_string).fetchall()
  # db.commit()

  # cursor.close()
  # db.close()

  return json.dumps("")


########### SELECT HELPERS #############
@bp.route('/assignment/available_vehicles', methods=['GET'])
def available_vehicles():
  return select_query(
    """
    SELECT *
    FROM vehicles
    ORDER BY Description, Category, Type
    """
  )

@bp.route('/assignment/customers', methods=['GET'])
def customers():
  return select_query(
    """
    SELECT *
    FROM customers
    """
  )

@bp.route('/assignment/createview', methods=['GET'])
def createview():
  db = get_db()
  cursor = db.cursor()
  cursor.execute("DROP VIEW IF EXISTS vRentalInfo")
  cursor.execute("""
    Create view vRentalInfo AS
    SELECT OrderDate, 
        StartDate, 
        ReturnDate,
        RentalType*Qty as TotalDays,
        VEHICLEs.VehicleID as VIN,
        Description as Vehicle,
        CASE Type
            WHEN 1 THEN 'Compact'
            WHEN 2 THEN 'Medium'
            WHEN 3 THEN 'Large'
            WHEN 4 THEN 'SUV'
            WHEN 5 THEN 'Truck'
            WHEN 6 THEN 'VAN'
        END aS Type,
        Category as Category,
        CUSTOMERs.CustID as CustomerID,
        Name as CustomerName,
        TotalAmount as OrderAmount,
        CASE 
            WHEN RENTALs.PaymentDate Is NULL THEN TotalAmount
            ELSE 0
        END as RentalBalance
    FROM VEHICLEs
    JOIN RENTALs ON VEHICLEs.VehicleID = RENTALs.VehicleID
    JOIN CUSTOMERs ON RENTALs.CustID = CUSTOMERs.CustID
    ORDER BY StartDate ASC;
  """)
  db.commit()

  cursor.close()
  db.close()

  return json.dumps("")