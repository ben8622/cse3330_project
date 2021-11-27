import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    cursor = db.cursor()

    # Initializes the Schema
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
    customer_file = current_app.open_resource('data/CUSTOMER.csv')
    rate_file = current_app.open_resource('data/RATE.csv')
    rental_file = current_app.open_resource('data/RENTAL.csv')
    vehicle_file = current_app.open_resource('data/VEHICLE.csv')

    def split_file(f):
        # f.read().decode('utf-8') returns an array of chars
        file_info = f.read().decode('utf-8')
        # we combine all the chars into a single string, splitting on '\n' for each entitity
        file_info = str(file_info).split('\n')
        entities = []
        # then iterate through, stripping '\r', and splitting each entity into it's attributes
        for line in file_info:
            line = line.strip("\r")
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
        if len(entity) < 9:
            continue
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
        if len(entity) < 5:
            continue
        ## Convert elements from string to int/float
        entity[1] = entity[1].strip('"')
        entity[3] = int(entity[3])
        entity[4] = int(entity[4])
        ## Convert list of attributes to a string, stripping off brackets
        entity = str(entity).strip('[]')
        ## Format our INSERT string
        insert_string = f'INSERT INTO vehicles VALUES ( {entity} )'
        ## Add to execution
        cursor.execute(insert_string)

    db.commit()

    

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)