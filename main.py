import mysql.connector
import subprocess

from create_final_attributes_keys import create_final_attributes_keys
from fetch_specific_data import fetch_specific_data
from fill_naive_bayes import fill_naive_bayes
from fill_word2vec import fill_word2vec
from get_attribute_ids import get_attribute_ids
from get_keywords_with_highest_values import get_keywords_with_highest_values
from modify_keys_attributes import insert_or_update_attribute
from Chameleon import Player, assign_roles, chameleon_guess_keyword, gather_clues, get_secret_word, identify_chameleon, roll_dice
from run_sql import run_sql
from run_sql_atts import run_sql_atts

def main():
    # Database configuration for initial connection
    initial_config = {
        'user': 'root',  # replace with your MySQL username
        'password': '2003',  # replace with your MySQL password
        'host': 'localhost'
    }

  # Replace 'path_to_mysql_workbench' with the actual path to MySQL Workbench executable
    mysql_workbench_path = r'C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe'

    # Connect to the MySQL server
    conn = mysql.connector.connect(**initial_config)
    cursor = conn.cursor()

    # Create chameleon_db 
    run_sql('create_db.sql' ,conn, cursor)


    # Connect to the newly created database
    conn.database = 'chameleon_db'
    
    topic_card = {
        1: "Chicken", 2: "Pizza", 3: "Burger", 4: "Salad",
        5: "Pasta", 6: "Sushi", 7: "Steak", 8: "Tacos",
        9: "Soup", 10: "Sandwich", 11: "Fries", 12: "Hotdog",
        13: "Curry", 14: "Rice", 15: "Fish", 16: "Cake"
    }

    code_card = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    players = [Player("Dat"), Player("Tri"), Player("Bu"), Player("Lam"), Player("KD"), Player("TA")]
    
    assign_roles(players)
    dice_roll = roll_dice()
    secret_word_id = code_card[dice_roll[1] - 1][dice_roll[0] - 1]  # Correct calculation for 1-based index
    print(f"Dice Roll: {dice_roll}")
    print(f"Secret Word ID: {secret_word_id}")

    secret_word = get_secret_word(topic_card, code_card, dice_roll)
    if secret_word is None:
        print("Invalid dice roll, please try again.")
        return

    print(f"The secret word is at {dice_roll}.")
    print(f"Secret Word: {secret_word}")

    attributes_input_str = input("Enter list of attributes:")
    attributes_input = attributes_input_str.split()
    gather_clues(players, attributes_input, conn, cursor)

    # Collect attributes from players (excluding the chameleon)
    data = []
    for player in players:
        if not player.is_chameleon:
            attribute = player.clue_word
            entry = [attribute] + [0] * 16  # Create an entry with all 0s except the first element
            entry[secret_word_id] = 1  # Set the position corresponding to the secret word ID to 1
            data.append(tuple(entry))  # Convert list to tuple

    # Insert or update attributes in the database
    for entry in data:
        insert_or_update_attribute(entry[0], secret_word, conn, cursor)  # Assuming insert_or_update_attribute handles the entry

    # Create the final_attributes_keys_table in the database
    attributes = [player.clue_word for player in players if not player.is_chameleon]
    attributes_id = get_attribute_ids(conn, cursor, attributes)
    run_sql_atts('sorted_rows.sql', attributes_id, conn, cursor)
    keywords = get_keywords_with_highest_values(conn, cursor)
    create_final_attributes_keys(conn, cursor, keywords)

    # Fill the probability and spread table in the database
    run_sql('fill_pro_spread.sql',conn, cursor)

    # # Fill the navie_bayes, word2vec table
    keywords = ['Chicken', 'Pizza', 'Burger', 'Salad', 'Pasta', 'Sushi', 'Steak', 'Tacos', 'Soup', 'Sandwich', 'Fries', 'Hotdog', 'Curry', 'Rice', 'Fish', 'Cake']
    fill_naive_bayes(keywords, attributes, conn, cursor)
    fill_word2vec(keywords, attributes, conn, cursor)

    # suspect = identify_chameleon(players)
    for player in players:
        if player.is_chameleon:
            suspect = player.name
            break

    for player in players:
        if player.name == suspect:
            if player.is_chameleon:
                print("The Chameleon was correctly guessed! The Chameleon now has a last chance. Now, guess the secret word: ")
                guess = chameleon_guess_keyword("naive_bayes", conn, cursor)
                # guess = chameleon_guess_keyword("word2vec", conn, cursor)
                print("The Chameleon has guess:",  guess)
                if guess.lower() == secret_word.lower():
                    print("The Chameleon has escaped!")
                else:
                    print("The Chameleon was caught!")
            else:
                print(f"{suspect} was wrongly accused! The Chameleon escapes.")

    print(f"The secret word was: {secret_word}")


    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Open SQL Workbench
    subprocess.run([mysql_workbench_path])

if __name__ == "__main__":
    main()