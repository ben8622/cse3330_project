import sqlite3

if __name__ == '__main__':

  ##############
  ### TASK 2 ###
  ##############

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
      Category INTEGER,
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
      OrderDate TEXT NOT NULL,
      RentalType INTEGER NOT NULL,
      Qty INTEGER NOT NULL,
      ReturnDate TEXT NOT NULL,
      TotalAmount REAL NOT NULL,
      PaymentDate TEXT,
      PRIMARY KEY(CustID, VehicleID, StartDate)
    )
    '''
  )
  cursor.execute(
    '''
    CREATE TABLE vehicles (
      VehicleID TEXT PRIMARY KEY,
      Description TEXT NOT NULL,
      Year TEXT NOT NULL,
      Type INTEGER NOT NULL,
      Category INTEGER NOT NULL
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
    ## Check to see if value is 'NULL'
    if "'NULL'" in entity:
      entity = entity.replace("'NULL'", "NULL")
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

  ## Count the rows in each table
  cursor.execute('SELECT COUNT(*) FROM customers')
  print("# of customers: " + str(cursor.fetchall()[0][0]))

  cursor.execute('SELECT COUNT(*) FROM rates')
  print("# of rates: " + str(cursor.fetchall()[0][0]))

  cursor.execute('SELECT COUNT(*) FROM rentals')
  print("# of rentals: " + str(cursor.fetchall()[0][0]))

  cursor.execute('SELECT COUNT(*) FROM vehicles')
  print("# of vehicles: " + str(cursor.fetchall()[0][0]))
  
  
  ##############
  ### TASK 3 ###
  ##############

  # 1
  cursor.execute(
    '''
    INSERT INTO customers (Name, Phone)
    VALUES ('L. Marconi', '(111) 222-3333' )
    '''
  )
  
  # 2
  cursor.execute(
    '''
    UPDATE customers
    Set Phone = '(837) 721-8965'
    WHERE Name = 'L. Marconi'
    '''
  )

  # 3
  cursor.execute(
    '''
    UPDATE rates
    Set Daily = Daily * 1.05
    WHERE Category = 1
    '''
  )

  # 4a
  cursor.execute(
    '''
    INSERT INTO vehicles
    VALUES ( '5FNRL6H58KB133711' , 'Honda Odyssey' , '2019', 6, 1)
    '''
  )
  # 4b
  cursor.execute(
    '''
    INSERT INTO RATES
    VALUES 
    (5,1,900,150), 
    (6,1,800,135)
    '''
  )

  connection.commit()

  # 5
  cursor.execute(
    '''
    SELECT v.VehicleID as VIN, v.Description, v.Year, StartDate, ReturnDate, TOTAL(ROUND(JULIANDAY(ReturnDate) - JULIANDAY(StartDate))) as DaysRented
    FROM vehicles AS v
    JOIN rentals AS r ON v.VehicleId = r.VehicleID
    WHERE (v.Type = 1 OR v.Category = 1) AND (r.StartDate NOT BETWEEN "2019-06-01" AND "2019-06-20") AND (r.ReturnDate NOT BETWEEN "2019-06-01" AND "2019-06-20") 
    GROUP BY VIN; 
    '''
  )
  print("Query 5: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  # 6
  cursor.execute(
    '''
    SELECT Name, SUM(TotalAmount)
    FROM customers
	  JOIN rentals ON rentals.CustID = customers.CustId
    WHERE customers.CustID = 221 AND rentals.PaymentDate IS NULL
    '''
  )
  print("Query 6: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

    # 7 
  cursor.execute(
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
  print("Query 7: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  # 8
  cursor.execute(
    '''
    SELECT SUM(TotalAmount)
    FROM rentals
    WHERE rentals.PaymentDate IS NOT NULL
    '''
  )
  print("Query 8: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  # TODO: finish 9a with extra stuff
  cursor.execute(
    '''
    SELECT 
      StartDate, 
      v.vehicleID, 
      v.Description, 
      v.Year,
      CASE
              WHEN v.Type = 1 THEN 'Compact'
              WHEN v.Type = 2 THEN 'Medium'
              WHEN v.Type = 3 THEN 'Large'
              WHEN v.Type = 4 THEN 'SUV'
              WHEN v.Type = 5 THEN 'Truck'
              WHEN v.Type = 6 THEN 'VAN'
        END as Type,  
      CASE
              WHEN v.Category = 0 THEN 'Basic'
              WHEN v.Category = 1 THEN 'Luxury'
      END as Category, 
      r.TotalAmount,
      CASE
        WHEN r.RentalType = 1 THEN ROUND(r.TotalAmount / rates.Daily)
        WHEN r.RentalType = 7 THEN ROUND(r.TotalAmount / rates.Weekly)
      END as UnitPrice,
      CASE
        WHEN r.RentalType = 7 THEN 'Weekly'
        WHEN r.RentalType = 1 THEN 'Daily'
      END AS RentalType,
      CASE
        WHEN r.PaymentDate IS NOT NULL THEN 'Paid'
        WHEN r.PaymentDate IS NULL THEN 'Not Paid'
      END AS IsPaid
    FROM customers c
    JOIN rentals r ON r.CustID = c.CustID 
    JOIN vehicles v ON v.vehicleID = r.vehicleID
    JOIN rates ON rates.Category = v.Category AND rates.Type = v.Type
    WHERE c.Name = "J. Brown"
    ORDER BY StartDate
    '''
  )
  print("Query 9a: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  # 9b
  cursor.execute(
    '''
    SELECT  TOTAL(TotalAmount) as 'Total Owed'
    FROM rentals
    JOIN customers on rentals.CustID = customers.CustID
    WHERE rentals.PaymentDate IS NULL AND Name = "J. Brown";
    '''
  )
  print("Query 9b: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  # 10
  cursor.execute(
    '''
    SELECT Name, StartDate, ReturnDate, TotalAmount
    FROM customers 
    JOIN rentals ON rentals.CustID = customers.CustID
    WHERE VehicleID = '19VDE1F3XEE414842' AND PaymentDate IS NULL AND RentalType = 7
    '''
  )
  print("Query 10: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  # 11
  cursor.execute(
    '''
    SELECT *
    FROM customers
    WHERE NOT EXISTS (
      SELECT *
      FROM rentals
      WHERE customers.CustID = rentals.CustId
    )
    '''
  )
  print("Query 11: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)

  # 12
  cursor.execute(
    '''
    SELECT Name, Description, StartDate, ReturnDate, TotalAmount
    FROM customers
    JOIN rentals ON rentals.CustID = customers.CustID
    JOIN vehicles ON rentals.VehicleID = vehicles.VehicleID
    WHERE StartDate = PaymentDate
    ORDER BY Name;
    '''
  )
  print("Query 12: ")
  rows = cursor.fetchall()
  for row in rows:
    print(row)


  connection.close()

