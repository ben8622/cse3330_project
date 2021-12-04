DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS rates;
DROP TABLE IF EXISTS rentals;
DROP TABLE IF EXISTS vehicles;

CREATE TABLE customers (
  CustID INTEGER PRIMARY KEY,
  Name TEXT NOT NULL,
  Phone TEXT NOT NULL
);
CREATE TABLE rates (
  Type INTEGER,
  Category INTEGER,
  Weekly REAL NOT NULL,
  Daily REAL NOT NULL,
  PRIMARY KEY (Type, Category)
);
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
);
CREATE TABLE vehicles (
  VehicleID TEXT PRIMARY KEY,
  Description TEXT NOT NULL,
  Year TEXT NOT NULL,
  Type INTEGER NOT NULL,
  Category INTEGER NOT NULL
);

ALTER TABLE rentals 
ADD column Returned INT NULL;