import mysql.connector

def run_sql_atts(sql_file_name, attributes_id, conn, cursor):
    # Read the SQL file
    with open(sql_file_name, 'r') as sql_file:
        sql_script = sql_file.read()

    # Replace placeholder with user input
    sql_script = sql_script.replace('1,2,3', attributes_id)

    # Execute the SQL script
    for statement in sql_script.split(';'):
        if statement.strip():
            cursor.execute(statement)

    conn.commit()