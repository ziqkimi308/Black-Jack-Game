"""
********************************************************************************
* Project Name:  BlackJack Game
* Description:   This project is blackjack game.\
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

import random
from art import logo
from replit import clear # type: ignore

def deal_card():
    card_set = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_set)

def calculate_score(x):
    if 11 in x and 10 in x and len(x) == 2:
        return 0
    if 11 in x and sum(x) > 21:
        x.remove(11)
        x.append(1)
    # else
    return sum(x)

def compare(you, comp):
    if you == comp:
        return "Draw.\n"
    elif comp == 0:
        return "You lose...Computer has a blackjack.\n"
    elif you == 0:
        return "You win! You have a blackjack!\n"
    elif you > 21:
        return "You lose...You went over 21.\n"
    elif comp > 21:
        return "You win! Computer went over 21.\n"
    elif you > comp:
        return "You win!\n"
    else:
        return "You lose...\n"

def play_game():
    # Assign first 2 cards
    user_card = []
    comp_card = []
    for i in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    # User turn
    user_turn = True
    while user_turn:
        user_score = calculate_score(user_card)
        comp_score = calculate_score(comp_card)
        print(f"Your cards: {user_card} | Score: {user_score}")
        print(f"Computer first card: {comp_card[0]}\n")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            user_turn = False
        else:
            draw_another = input("Enter 'y' to draw another card or 'n' to pass: ").lower()
            if draw_another == 'y':
                user_card.append(deal_card())
            else:
                user_turn = False

    # Computer turn
    while comp_score != 0 and comp_score < 17:
        comp_card.append(deal_card())
        comp_score = calculate_score(comp_card)

    # Conclude
    print(f"\nYour final hand: {user_card} | Final score: {user_score}")
    print(f"Computer final hand: {comp_card} | Final score: {comp_score}\n")
    print(compare(user_score, comp_score))

    # Repeat game?
    while input("Do you want to play Blackjack? Enter 'y' or 'n': ").lower() == 'y':
        clear()
        play_game()

# Call function
print(logo)
print("🃏 Welcome to the Blackjack! 🎉\n")
play_game()