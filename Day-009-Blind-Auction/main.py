from art import logo
import os
import subprocess

def clear():
    subprocess.run(
        ["cls"] if os.name == "nt" else ["clear"],
        shell=(os.name == "nt"),
    )
    # print("\n" * 100)
    return

def find_winner(bidding_dict):
    winner = max(bidding_dict, key=bidding_dict.get)
    print(f"The winner is {winner} with a bid of ${silent_auction[winner]}")

def run_auction():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    silent_auction[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        clear()
        find_winner(silent_auction)
        return False
    else:
        clear()
        return True

print(logo)
silent_auction = {}

while True:
    run_auction()
