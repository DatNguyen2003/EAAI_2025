import mysql.connector

def insert_chameleon_game(result, keyword, order_list, conn, cursor):
    # Ensure order_list has exactly 6 elements, filling with empty strings if necessary
    while len(order_list) < 6:
        order_list.append("")

    # SQL query to insert the data
    insert_query = """
    INSERT INTO ChameleonGame (Result, Keyword, Order1, Order2, Order3, Order4, Order5, Order6)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Data to be inserted
    data = (result, keyword) + tuple(order_list[:6])

    try:
      # Execute the insert query
      cursor.execute(insert_query, data)
      conn.commit()
    except mysql.connector.Error as err:
      print(f"Error: {err}")
      conn.rollback()

