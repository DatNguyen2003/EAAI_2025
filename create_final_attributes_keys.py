import mysql.connector

def create_final_attributes_keys(conn, cursor, keywords):
  # Drop the table if it exists
  drop_table_query = "DROP TABLE IF EXISTS final_attributes_keys;"
  cursor.execute(drop_table_query)

  # Generate the SQL query to create the new table
  create_table_query = f"""
    CREATE TABLE final_attributes_keys (
      attribute_id INT PRIMARY KEY AUTO_INCREMENT,
      attribute_name VARCHAR(255),
      Chicken FLOAT DEFAULT 0,
      Pizza FLOAT DEFAULT 0,
      Burger FLOAT DEFAULT 0,
      Salad FLOAT DEFAULT 0,
      Pasta FLOAT DEFAULT 0,
      Sushi FLOAT DEFAULT 0,
      Steak FLOAT DEFAULT 0,
      Tacos FLOAT DEFAULT 0,
      Soup FLOAT DEFAULT 0,
      Sandwich FLOAT DEFAULT 0,
      Fries FLOAT DEFAULT 0,
      Hotdog FLOAT DEFAULT 0,
      Curry FLOAT DEFAULT 0,
      Rice FLOAT DEFAULT 0,
      Fish FLOAT DEFAULT 0,
      Cake FLOAT DEFAULT 0
    );
  """

  # Execute the SQL query to create the new table
  cursor.execute(create_table_query)

  # Get the list of attribute names from the original table
  cursor.execute("SELECT attribute_name FROM attributes_keys")
  attribute_names = [row[0] for row in cursor.fetchall()]

  # Generate the SQL query to copy data from the original table to the final table
  copy_data_query = f"""
    INSERT INTO final_attributes_keys (attribute_name, Chicken, Pizza, Burger, Salad, Pasta, Sushi, Steak, Tacos, Soup, Sandwich, Fries, Hotdog, Curry, Rice, Fish, Cake)
      SELECT 
        attribute_name, 
        CASE WHEN 'Chicken' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Chicken ELSE 0 END,
        CASE WHEN 'Pizza' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Pizza ELSE 0 END,
        CASE WHEN 'Burger' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Burger ELSE 0 END,
        CASE WHEN 'Salad' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Salad ELSE 0 END,
        CASE WHEN 'Pasta' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Pasta ELSE 0 END,
        CASE WHEN 'Sushi' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Sushi ELSE 0 END,
        CASE WHEN 'Steak' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Steak ELSE 0 END,
        CASE WHEN 'Tacos' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Tacos ELSE 0 END,
        CASE WHEN 'Soup' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Soup ELSE 0 END,
        CASE WHEN 'Sandwich' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Sandwich ELSE 0 END,
        CASE WHEN 'Fries' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Fries ELSE 0 END,
        CASE WHEN 'Hotdog' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Hotdog ELSE 0 END,
        CASE WHEN 'Curry' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Curry ELSE 0 END,
        CASE WHEN 'Rice' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Rice ELSE 0 END,
        CASE WHEN 'Fish' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Fish ELSE 0 END,
        CASE WHEN 'Cake' IN ({', '.join(["'" + kw + "'" for kw in keywords])}) THEN Cake ELSE 0 END
      FROM attributes_keys;
  """

   # Execute the SQL query to copy data
  cursor.execute(copy_data_query)

  # Commit the transaction
  conn.commit()
