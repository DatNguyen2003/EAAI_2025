import random
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import mysql.connector
from sqlalchemy import func


class Player:
    def __init__(self, name, is_chameleon=False):
        self.name = name
        self.is_chameleon = is_chameleon
        self.clue_word = ""

def roll_dice():
    return random.randint(1, 4), random.randint(1, 4)

def get_secret_word(topic_card, code_card, dice_roll):
    row, col = dice_roll
    try:
        return topic_card[code_card[row-1][col-1]]
    except IndexError:
        return None

def assign_roles(players):
    chameleon_index = random.randint(0, len(players) - 1)
    for i, player in enumerate(players):
        player.is_chameleon = (i == chameleon_index)
        player.is_bot = (i == chameleon_index)

def gather_clues(players):
    for player in players:
        if not player.is_chameleon:
            player.clue_word = input(f"{player.name}, enter a clue for the secret word: ")
        else:
            # player.clue_word = input(f"{player.name}, enter any clue (you are the Chameleon): ")
            player.clue_word = bot_guess_clue()

def bot_guess_clue():
    return "I don't know"

def bot_guess_word():
    return "I don't know"

def identify_chameleon(players):
    for player in players:
        print(f"{player.name}'s clue: {player.clue_word}")
    
    votes = {}
    for player in players:
        vote = input(f"{player.name}, who do you think is the Chameleon? ")
        votes[vote] = votes.get(vote, 0) + 1
    
    suspect = max(votes, key=votes.get)
    return suspect

database_url = 'mysql+mysqlconnector://root:2003@localhost/chameleon'
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
metadata.reflect(bind=engine)

table_name = 'key'
table = metadata.tables.get(table_name)

def add_data_sqlalchemy(database_url, table_name, data):
    table = metadata.tables.get(table_name)
    
    try:
        # Check if the row exists
        existing_row = session.query(table).filter_by(id=data['id']).first()
        if existing_row:
            # Update existing row
            session.query(table).filter_by(id=data['id']).update(data)
        else:
            # Insert new row
            insert_stmt = table.insert().values(data)
            session.execute(insert_stmt)
        
        session.commit()
        print("Data inserted/updated successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()

def main():

    topic_card = {
        1: "Chicken", 2: "Pizza", 3: "Burger", 4: "Salad",
        5: "Pasta", 6: "Sushi", 7: "Steak", 8: "Tacos",
        9: "Soup", 10: "Sandwich", 11: "Fries", 12: "Hotdog",
        13: "Curry", 14: "Rice", 15: "Fish", 16: "Cake"
    }



    for key, value in topic_card.items():
        data = {
            'id': f"{key}",
            'key_word_name': value
        }
        session = Session()
        add_data_sqlalchemy(database_url, 'key', data)

    code_card = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    players = [Player("Dat"),Player("Tri"),Player("Bu"),Player("Lam"),Player("KD"),Player("TA")]
    
    assign_roles(players)
    dice_roll = roll_dice()
    serect_word_id = dice_roll[0] + dice_roll[1]*3
    print(serect_word_id)
    
    secret_word = get_secret_word(topic_card, code_card, dice_roll)
    if secret_word is None:
        print("Invalid dice roll, please try again.")
        return

    print(f"The secret word is at {dice_roll}.")
    print(secret_word)
    
    gather_clues(players)
    suspect = identify_chameleon(players)
    
    for player in players:
        if player.name == suspect:
            if player.is_chameleon:
                guess = input("The chameleon was corretly guessed! The Chameleon now has a last chance. Now, guess the secret word: ")
                if guess.lower() == secret_word.lower():
                    print("The Chameleon has escaped!")
                else:
                    print("The Chameleon was caught!")
            else:
                print(f"{suspect} was wrongly accused! The Chameleon escapes.")
    
    print(f"The secret word was: {secret_word}")

    last_id = session.query(func.max(table.c.id)).scalar()
    for player in players:
        if(player.is_chameleon == False):
            last_id += 1
            data = {
                'id': last_id,
                'attributes': player.clue_word,
                'key_id': serect_word_id
            }
            print(data)
            session = Session()
            add_data_sqlalchemy(database_url,'key_attributes', data)

if __name__ == "__main__":
    main()




