import mysql.connector

def fetch_highest_value(table_name, conn, cursor):
    try:
        # Build the query to select the keyword with the highest probability
        query = f"SELECT keyword FROM {table_name} ORDER BY probability DESC LIMIT 1"
        
        # Execute the query
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            # Return the keyword
            return row[0]
        else:
            # If no rows are found, return None
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

