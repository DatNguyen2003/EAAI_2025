import random
import mysql.connector
import subprocess

from create_final_attributes_keys import create_final_attributes_keys
from fetch_highest_value import fetch_highest_value
from fill_naive_bayes import fill_naive_bayes
from fill_word2vec import fill_word2vec
from get_all_attribute_given_keyword import get_non_zero_attributes
from get_attribute_ids import get_attribute_ids
from get_keywords_with_highest_values import get_keywords_with_highest_values
from highest_spread_attribute import get_attribute_with_highest_value
from run_sql import run_sql
from run_sql_atts import run_sql_atts


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

def gather_clues(players, attributes_input, conn, cursor):
    for player in players:
        if not player.is_chameleon:
            player.clue_word = attributes_input.pop()
            print(f"{player.name}, enter a clue for the secret word:",player.clue_word)
        else:
            # Fill the navie_bayes, word2vec table
            keywords = ['Chicken', 'Pizza', 'Burger', 'Salad', 'Pasta', 'Sushi', 'Steak', 'Tacos', 'Soup', 'Sandwich', 'Fries', 'Hotdog', 'Curry', 'Rice', 'Fish', 'Cake']
            attributes = [player.clue_word for player in players if not player.is_chameleon]
            attributes_id = get_attribute_ids(conn, cursor, attributes)
            run_sql_atts('sorted_rows.sql', attributes_id, conn, cursor)
            keywords = get_keywords_with_highest_values(conn, cursor)
            create_final_attributes_keys(conn, cursor, keywords)
            run_sql('fill_pro_spread.sql',conn, cursor)
            fill_naive_bayes(keywords, attributes, conn, cursor)
            fill_word2vec(keywords, attributes, conn, cursor)
            player.clue_word = chameleon_guess_attribute(attributes, conn, cursor)
            print(f"{player.name}, enter a clue for the secret word:",player.clue_word,"(this is the Chameleon)")

            if player.clue_word in attributes_input:
                attributes_input.remove(player.clue_word)



def chameleon_guess_attribute(attributes, conn, cursor):
    keyword = chameleon_guess_keyword("naive_bayes", conn, cursor)
    non_zero_attributes = get_non_zero_attributes(keyword, conn, cursor)
    set2 = set(attributes)
    final_list_attributes = [attribute for attribute in non_zero_attributes if attribute not in set2]
    highest_value_attribute = get_attribute_with_highest_value(final_list_attributes, conn, cursor)
    return highest_value_attribute


def chameleon_guess_keyword(table_name, conn, cursor):
    return fetch_highest_value(table_name, conn, cursor)

def identify_chameleon(players):
    for player in players:
        print(f"{player.name}'s clue: {player.clue_word}")
    
    votes = {}
    for player in players:
        vote = input(f"{player.name}, who do you think is the Chameleon? ")
        votes[vote] = votes.get(vote, 0) + 1
    
    suspect = max(votes, key=votes.get)
    return suspect
