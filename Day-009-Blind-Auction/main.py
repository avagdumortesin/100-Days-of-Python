"""
Instructions:
The goal is to build a blind auction program.

Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.

# This will add 20 new lines to the output
print("\n" * 20)

Functionality
- Each person writes their name and bid.
- The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
- Each person's name and bid are saved to a dictionary.
- Once all participants have placed their bid, the program works out who has the highest bid and prints it.
"""
"""
Demo from AppBrewery:
https://appbrewery.github.io/python-day9-demo/
"""

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
