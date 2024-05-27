import mysql.connector

def create_db(conn, cursor):
  # Read the SQL file
  with open('create_db.sql', 'r') as sql_file:
      sql_script = sql_file.read()

# Execute the SQL script
  for statement in sql_script.split(';'):
      if statement.strip():
        cursor.execute(statement)
  
  conn.commit()