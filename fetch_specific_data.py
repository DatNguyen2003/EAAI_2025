import mysql.connector

def fetch_specific_data(attribute_name, keyword, conn, cursor):
    # Ensure keyword is valid and in the table schema
    valid_keywords = ['Chicken', 'Pizza', 'Burger', 'Salad', 'Pasta', 'Sushi', 'Steak', 'Tacos', 'Soup', 'Sandwich', 'Fries', 'Hotdog', 'Curry', 'Rice', 'Fish', 'Cake']
    if keyword and keyword not in valid_keywords:
        raise ValueError(f"Invalid keyword '{keyword}'. Must be one of {valid_keywords}")

    try:
        # Build the query to select the specific keyword column
        query = f"SELECT {keyword} FROM attributes_keys_probability WHERE attribute_name = %s"
        
        # Execute the query with the attribute_name parameter
        cursor.execute(query, (attribute_name,))
        row = cursor.fetchone()

        if row:
            if(row[0]==0): return 0.01
            return float(row[0]) if row[0] is not None else 1
        else:
            return 1

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 0.0
