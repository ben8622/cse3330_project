 # What is Phase 2?
 Phase two is where we actually create our database on a given set of standards provided by the professor. This will allow us to focus more on the GUI application in phase 3 rather than worrying about the creation of queries.
 ## Files:
 - `/main.py` is the python file that builds or tables, extracts data from the provided datasets, inserts said data, and runs all the queries from Task 3.
 - `/rental.db` is the SQLite database file generated from `main.py`
 - `/Car_Rental_2` holds all of our datasets in `.csv` format

## How to run:
_**IMPORTANT:** this is assuming you already know how to run a python file from your machine_
1. `cd` into the `phase_two` directory where these files are located
2. execute `python main.py` 

After running you should see the output of each query ran and what question it corresponded to in Task 3 such as:
```
...
Query 10:
('G. Clarkson', '2019-11-01', '2019-11-15', 1200.0)
('J. Brown', '2020-01-01', '2020-01-29', 2400.0)
...
```
