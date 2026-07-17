"""
Instructions:
Chose your difficulty
- Normal 😎: Use all Hints below to complete the project.
- Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
- Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
- Expert 🤯: Only use Hint 1 to complete the project.

Our Blackjack Game House Rules
- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.
"""
"""
Demo from AppBrewery:
https://appbrewery.github.io/python-day11-demo/
"""

import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    player_cards = []
    dealer_cards = []
    for card in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    return player_cards, dealer_cards

def calculate_score(dealt_cards):
    if sum(dealt_cards) == 21 and len(dealt_cards) == 2:
        return 0
    if 11 in dealt_cards and sum(dealt_cards) > 21:
        dealt_cards.remove(11)
        dealt_cards.append(1)
    busted = sum(dealt_cards) > 21
    return sum(dealt_cards), busted

def hit_me(dealt_cards):
    dealt_cards.append(random.choice(cards))
    return dealt_cards

def determine_winner(player_score, dealer_score):
    print(f"Your cards: {p_cards}, current score: {p_score}")
    print(f"Dealer's cards: {d_cards}, current score: {d_score}")
    if player_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "You lose; the dealer has Blackjack."
    elif player_score == 0:
        return "You have Blackjack; you win!"
    elif player_score > 21:
        return "You busted. You lose!"
    elif dealer_score > 21:
        return "Dealer busted. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

while True:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "n":
        print("Well, shucks. See you next time!")
        break
    else:
        print(art.logo)
        game_over = False
        p_cards, d_cards = deal_cards()
        p_score, p_busted = calculate_score(p_cards)
        print(f"Your cards: {p_cards}, current score: {p_score}")
        print(f"Dealer's first card: {d_cards[0]}")
        d_score, d_busted = calculate_score(d_cards)
        while not p_busted and not d_busted and not game_over:
            hit_choice = input("Would you like me to hit you? Type 'y' to get another card or 'n' to stand:").lower()
            if hit_choice == "y":
                p_score, p_busted = calculate_score(hit_me(p_cards))
                print(f"Your cards: {p_cards}, current score: {p_score}")
            elif d_score < 17:
                d_score, d_busted = calculate_score(hit_me(d_cards))
                print(f"Dealer's cards: {d_cards}, current score: {d_score}")
            else:
                determine_winner(p_score, d_score)
                game_over = True
        if p_busted or d_busted:
            determine_winner(p_score, d_score)

