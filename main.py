from random import choice, randint
import csv
import json


# Append new words in 'learning now' file
def next_step():
    pass


# Choice language for words, to show you
def en_or_ru():
    coin = randint(0, 1)
    if coin:
        return 'eng'
    else:
        return 'rus'


def choice_user(names):
    pass


def new_user():
    pass


while True:
    try:
        with open('names.json', 'r', encoding='utf-8-sig') as users_file:
            users = json.load(users_file)
    except:
        # new_user()
        print('Имя пользователя не найдено')
break
