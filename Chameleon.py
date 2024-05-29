import random
import mysql.connector
import subprocess


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

def bot_guess_word(players):
    attributes = [player.clue_word for player in players]
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
