import mysql.connector

def run_sql(sql_file_name ,conn, cursor):
  # Read the SQL file
  with open(sql_file_name, 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
  for statement in sql_script.split(';'):
    if statement.strip():
      cursor.execute(statement)
  
  conn.commit()