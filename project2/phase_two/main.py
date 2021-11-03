import sqlite3

if __name__ == '__main__':

  ## Open files
  customer_file = open("Car_Rental_2/CUSTOMER.csv", "r")
  rate_file = open("Car_Rental_2/RATE.csv", "r")
  rental_file = open("Car_Rental_2/RENTAL.csv", "r")
  vehicle_file = open("Car_Rental_2/VEHICLE.csv", "r")

  def split_file(f):
    entities = []
    for line in f:
      line = line.strip("\n")
      entities.append(line.split(","))
    return entities

  ## Grab data from files
  customers = split_file(customer_file)
  rates = split_file(rate_file)
  rentals = split_file(rental_file)
  vehicles = split_file(vehicle_file)

  # Get rid of column identifier
  customers.pop(0)
  rates.pop(0)
  rentals.pop(0)
  vehicles.pop(0)

  customer_file.close()
  rate_file.close()
  rental_file.close()
  vehicle_file.close()

  ## Connect to database and create a cursor object to execute SQL statements
  connection = sqlite3.connect("rental.db")
  cursor = connection.cursor()

  ## Drop tables to avoid trying to create a table that already exists
  cursor.execute('''DROP TABLE IF EXISTS customers''')
  cursor.execute('''DROP TABLE IF EXISTS rates''')
  cursor.execute('''DROP TABLE IF EXISTS rentals''')
  cursor.execute('''DROP TABLE IF EXISTS vehicles''')

  ## Create tables
  cursor.execute(
    '''
    CREATE TABLE customers (
      CustID INTEGER PRIMARY KEY,
      Name TEXT NOT NULL,
      Phone TEXT NOT NULL
    )
    '''
  )
  cursor.execute(
    '''
    CREATE TABLE rates (
      Type INTEGER,
      Category INTEGER NOT NULL,
      Weekly REAL NOT NULL,
      Daily REAL NOT NULL,
      PRIMARY KEY (Type, Category)
    )
    '''
  )
  cursor.execute(
    '''
    CREATE TABLE rentals (
      CustID INTEGER,
      VehicleID TEXT,
      StartDate TEXT,
      OrderDate TEXT,
      RentalType INTEGER,
      Qty INTEGER,
      ReturnDate TEXT,
      TotalAmount REAL,
      PaymentDate TEXT,
      PRIMARY KEY(CustID, VehicleID, StartDate)
    )
    '''
  )
  cursor.execute(
    '''
    CREATE TABLE vehicles (
      VehicleID TEXT PRIMARY KEY,
      Description TEXT,
      Year TEXT,
      Type INTEGER,
      Category INTEGER
    )
    '''
  )

  ## INSERT statements for customers data
  for entity in customers:
    ## Convert first element from string to int
    entity[0] = int(entity[0])
    ## Convert list of attributes to a string, stripping off brackets
    entity = str(entity).strip('[]')
    ## Format our INSERT string
    insert_string = f'INSERT INTO customers VALUES ( {entity} )'
    ## Add to execution
    cursor.execute(insert_string)
    
  ## INSERT statements for rates data
  for entity in rates:
    ## Convert elements from string to int/float
    entity[0] = int(entity[0])
    entity[1] = int(entity[1])
    entity[2] = float(entity[2])
    entity[3] = float(entity[3])
    ## Convert list of attributes to a string, stripping off brackets
    entity = str(entity).strip('[]')
    ## Format our INSERT string
    insert_string = f'INSERT INTO rates VALUES ( {entity} )'
    ## Add to execution
    cursor.execute(insert_string)

  ## INSERT statements for rentals data
  for entity in rentals:
    ## Convert elements from string to int/float
    entity[0] = int(entity[0])
    entity[4] = int(entity[4])
    entity[5] = int(entity[5])
    entity[7] = float(entity[7])
    ## Convert list of attributes to a string, stripping off brackets
    entity = str(entity).strip('[]')
    ## Format our INSERT string
    insert_string = f'INSERT INTO rentals VALUES ( {entity} )'
    ## Add to execution
    cursor.execute(insert_string)

  ## INSERT statements for vehicles data
  for entity in vehicles:
    ## Convert elements from string to int/float
    entity[3] = int(entity[3])
    entity[4] = int(entity[4])
    ## Convert list of attributes to a string, stripping off brackets
    entity = str(entity).strip('[]')
    ## Format our INSERT string
    insert_string = f'INSERT INTO vehicles VALUES ( {entity} )'
    ## Add to execution
    cursor.execute(insert_string)
    

  
  connection.commit()
  connection.close()

