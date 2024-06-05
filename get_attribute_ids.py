import mysql.connector

def get_attribute_ids(conn, cursor, attributes):
    # Generate the SQL query to get the IDs of the given attributes
    query = f"""
        SELECT attribute_id 
        FROM attributes_keys 
        WHERE attribute_name IN ({', '.join(['%s'] * len(attributes))})
    """

    # Execute the query with the provided attributes
    cursor.execute(query, attributes)

    # Fetch the results
    attribute_ids = [str(row[0]) for row in cursor.fetchall()]

    # Format the result as a comma-separated string
    return ','.join(attribute_ids)
