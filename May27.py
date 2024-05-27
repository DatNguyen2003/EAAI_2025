import mysql.connector
import subprocess

# Database configuration for initial connection
initial_config = {
    'user': 'root',  # replace with your MySQL username
    'password': '2003',  # replace with your MySQL password
    'host': 'localhost'
}

# Connect to the MySQL server
conn = mysql.connector.connect(**initial_config)
cursor = conn.cursor()

# Read the SQL file
with open('chameleon_db_create.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
for statement in sql_script.split(';'):
    if statement.strip():
        cursor.execute(statement)

# Commit the changes
conn.commit()

# Connect to the newly created database
conn.database = 'chameleon_db'

# Read the SQL file
with open('chameleon_db_insert.sql', 'r') as sql_file:
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

# Replace 'path_to_mysql_workbench' with the actual path to MySQL Workbench executable
mysql_workbench_path = r'C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe'

# Launch MySQL Workbench
subprocess.run([mysql_workbench_path])
