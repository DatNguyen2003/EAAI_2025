import mysql.connector

def get_keywords_with_highest_values(conn, cursor):
    # Execute SQL query to retrieve keywords with highest values
    query = """
        SELECT key_word
        FROM attributes_keys_sorted_column_sums_transpose
        WHERE count = (SELECT MAX(count) FROM attributes_keys_sorted_column_sums_transpose);
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return [row[0] for row in result]