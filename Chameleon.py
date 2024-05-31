import random
import mysql.connector
import subprocess

from fetch_highest_value import fetch_highest_value
from fill_naive_bayes import fill_naive_bayes
from fill_word2vec import fill_word2vec
from get_all_attribute_given_keyword import get_non_zero_attributes
from highest_spread_attribute import get_attribute_with_highest_value


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

def gather_clues(players, conn, cursor):
    for player in players:
        if not player.is_chameleon:
            player.clue_word = input(f"{player.name}, enter a clue for the secret word: ")
        else:
            # Fill the navie_bayes, word2vec table
            keywords = ['Chicken', 'Pizza', 'Burger', 'Salad', 'Pasta', 'Sushi', 'Steak', 'Tacos', 'Soup', 'Sandwich', 'Fries', 'Hotdog', 'Curry', 'Rice', 'Fish', 'Cake']
            attributes = [player.clue_word for player in players]
            fill_naive_bayes(keywords, attributes, conn, cursor)
            fill_word2vec(keywords, attributes, conn, cursor)
            player.clue_word = chameleon_guess_attribute(conn, cursor)
            print(f"{player.name}, enter a clue for the secret word:",player.clue_word,"(this is the Chameleon)")

def chameleon_guess_attribute(conn, cursor):
    keyword = chameleon_guess_keyword("naive_bayes", conn, cursor)
    attributes = get_non_zero_attributes(keyword, conn, cursor)
    highest_value_attribute = get_attribute_with_highest_value(attributes, conn, cursor)
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
