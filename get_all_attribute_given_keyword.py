import mysql.connector

def get_non_zero_attributes(keyword, conn, cursor):
    # Ensure keyword is valid and in the table schema
    valid_keywords = [
        'Chicken', 'Pizza', 'Burger', 'Salad', 'Pasta', 'Sushi', 'Steak',
        'Tacos', 'Soup', 'Sandwich', 'Fries', 'Hotdog', 'Curry', 'Rice',
        'Fish', 'Cake'
    ]
    
    if keyword not in valid_keywords:
        raise ValueError(f"Invalid keyword '{keyword}'. Must be one of {valid_keywords}")

    try:
        # Build the query to select attribute names with non-zero values for the given keyword
        query = f"SELECT attribute_name FROM attributes_keys WHERE {keyword} <> 0"
        
        # Execute the query
        cursor.execute(query)
        rows = cursor.fetchall()

        # Extract attribute names from the result
        non_zero_attributes = [row[0] for row in rows]

        return non_zero_attributes

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []


