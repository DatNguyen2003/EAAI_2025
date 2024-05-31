import mysql.connector

def get_attribute_with_highest_value(attributes, conn, cursor):
    try:
        # Prepare the query to find the attribute with the highest key_word_covering value
        format_strings = ','.join(['%s'] * len(attributes))
        query = f"""
        SELECT attribute_name, key_word_covering
        FROM attributes_spreading
        WHERE attribute_name IN ({format_strings})
        ORDER BY key_word_covering DESC
        LIMIT 1
        """
        
        # Execute the query with the list of attributes
        cursor.execute(query, attributes)
        row = cursor.fetchone()

        if row:
            # Return the attribute name with the highest key_word_covering value
            return row[0]
        else:
            # If no matching row is found, return None
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Example usage
if __name__ == "__main__":
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    
    # Create a cursor
    cursor = conn.cursor()

    # Example list of attributes
    attributes = ['attribute1', 'attribute2', 'attribute3']  # Replace with actual attribute names

    # Get the attribute with the highest key_word_covering value
    highest_value_attribute = get_attribute_with_highest_value(attributes, conn, cursor)
    
    if highest_value_attribute:
        print("Attribute with the highest key_word_covering value:", highest_value_attribute)
    else:
        print("No matching attributes found.")

    # Close the cursor and connection
    cursor.close()
    conn.close()
