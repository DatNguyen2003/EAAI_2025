import mysql.connector

def insert_or_update_attribute(attribute_name, keyword, conn, cursor):        
    # Ensure keyword is valid and in the table schema
    valid_keywords = ['Chicken', 'Pizza', 'Burger', 'Salad', 'Pasta', 'Sushi', 'Steak', 'Tacos', 'Soup', 'Sandwich', 'Fries', 'Hotdog', 'Curry', 'Rice', 'Fish', 'Cake']
    if keyword not in valid_keywords:
        raise ValueError(f"Invalid keyword '{keyword}'. Must be one of {valid_keywords}")

    try:
        # Check if the attribute already exists
        select_query = "SELECT * FROM keys_attributes WHERE attribute_name = %s"
        cursor.execute(select_query, (attribute_name,))
        row = cursor.fetchone()

        if row:
            # Attribute exists, increment the keyword count
            update_query = f"UPDATE keys_attributes SET {keyword} = {keyword} + 1 WHERE attribute_name = %s"
            cursor.execute(update_query, (attribute_name,))
        else:
            # Attribute does not exist, insert a new row
            insert_query = f"""
            INSERT INTO keys_attributes 
            (attribute_name, {', '.join(valid_keywords)}) 
            VALUES 
            (%s, {', '.join(['%s' if k != keyword else '%s' for k in valid_keywords])})
            """
            values = [attribute_name] + [1 if k == keyword else 0 for k in valid_keywords]
            cursor.execute(insert_query, tuple(values))

        # Commit the transaction
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
