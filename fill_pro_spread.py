import mysql.connector

# Fill the probability and spread table in the database
def fill_pro_spread(conn, cursor):
  # Read the SQL file
  with open('fill_pro_spread.sql', 'r') as sql_file:
      sql_script = sql_file.read()

# Execute the SQL script
  for statement in sql_script.split(';'):
      if statement.strip():
        cursor.execute(statement)
  
  conn.commit()