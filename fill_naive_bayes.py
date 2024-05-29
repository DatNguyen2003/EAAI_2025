import mysql.connector

from fetch_specific_data import fetch_specific_data

def fill_naive_bayes(keywords, attributes, conn, cursor):    
    try:
        # SQL Insert query with ON DUPLICATE KEY UPDATE
        insert_query = """
        INSERT INTO naive_bayes (keyword, probability)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE probability = VALUES(probability)
        """

        # Insert each keyword with the given probability

        for keyword in keywords:
          probability_value = 0.5
          for attribute in attributes:
            probability_value *= fetch_specific_data(attribute, keyword, conn, cursor)
          print(probability_value)
          cursor.execute(insert_query, (keyword, probability_value))

        # Commit the transaction
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

