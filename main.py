from random import choice, randint
import csv

# Append new words in 'learning now' file
def next_step():
    None

# Choice language for words, to show you
def en_or_ru():
    coin = randint(0, 1)
    if coin:
        return 'eng'
    else:
        return 'rus'

def choice_user(names):
    None

def new_user():
    None


while True:
    try:
        with open('names.json', 'r', encoding='utf-8-sig') as users_file:
            users = json.load(users_file)
    except:
        # new_user()
        None

    break
    
