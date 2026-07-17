"""
Instructions:
The goal is to build a game that asks the user to guess who has more followers on Instagram.

Original Higher Lower Game
https://www.higherlowergame.com/
"""
"""
Demo from AppBrewery:
https://appbrewery.github.io/python-day14-demo/
"""

import random
from art import logo, vs
from game_data import data
import os
import subprocess

def select_account():
    return random.choice(data)

def assign_account(account_1, account_2):
    if account_1 == {} and account_2 == {}:
        return select_account(), select_account()
    elif account_2 == {}:
        account_2 = select_account()
        while account_2 == account_1:
            account_2 = select_account()
        return account_1, account_2
    return account_1, account_2


def compare_accounts(account_1, account_2):
    if account_1['follower_count'] > account_2['follower_count']:
        return "a"
    else:
        return "b"

def play_game():
    first_account = second_account = {}
    continue_playing = True
    score = 0

    while continue_playing:
        first_account, second_account = assign_account(first_account, second_account)
        # print(type(first_account))
        # print(type(second_account))
        # print(first_account)
        # print(second_account)
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {first_account['name']}, a {first_account['description']}, from {first_account['country']}.")
        print(vs)
        print(f"Against B: {second_account['name']}, a {second_account['description']}, from {second_account['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        answer = compare_accounts(first_account, second_account)
        if guess == answer:
            score += 1
            if guess == "b":
                first_account = second_account
                second_account = {}
            else:
                second_account = {}
            clear_screen()
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            continue_playing = False


def clear_screen():
    subprocess.run(
        ["cls"] if os.name == "nt" else ["clear"],
    shell=(os.name == "nt")
    )

play_game()

