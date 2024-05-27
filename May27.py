import mysql.connector
import subprocess

from create_db import create_db
from modify_keys_attributes import insert_or_update_attribute
from open_sql_workbench import open_sql_workbench

# Database configuration for initial connection
initial_config = {
    'user': 'root',  # replace with your MySQL username
    'password': '2003',  # replace with your MySQL password
    'host': 'localhost'
}

# Connect to the MySQL server
conn = mysql.connector.connect(**initial_config)
cursor = conn.cursor()

create_db(conn, cursor)

# Connect to the newly created database
conn.database = 'chameleon_db'

insert_or_update_attribute('Example Attribute', 'Chicken', conn, cursor)
insert_or_update_attribute('Example Attribute', 'Pizza', conn, cursor)

# Read the SQL file
with open('create_pro_spread.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
for statement in sql_script.split(';'):
    if statement.strip():
        cursor.execute(statement)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

open_sql_workbench()
