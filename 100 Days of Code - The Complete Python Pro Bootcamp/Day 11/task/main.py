import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_checker(user_card1, user_card2, user_total, computer_total):
    if user_total or computer_total == 21:
        if user_total == 21:
            print("User Wins!")
            is_playing = False
        else:
            print("Computer Wins!")
            is_playing = False

    elif user_total > 21:
        if user_card1 == 11:
            user_card1 = 1
            user_total = user_card1 + user_card2
            if user_total > 21:
                print("Computer Wins!")
                is_playing = False
        elif user_card2 == 11:
            user_card2 = 1
            user_total = user_card1 + user_card2
            if user_total > 21:
                print("Computer Wins!")
                is_playing = False
        else:
            print("Computer Wins!")
            is_playing = False


def blackjack():
    user_card1 = random.choice(cards)
    user_card2 = random.choice(cards)
    user_total = user_card1 + user_card2
    print(f"You cards: [{user_card1}, {user_card2}], current score: {user_total}")
    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    print(f"Computer's first card: {computer_card1}.")
    computer_total = computer_card2 + computer_card1
    card_checker(user_card1, user_card2, user_total, computer_total)
    another_card = input("Type y to get another card, type n to pass.")
    if another_card == "y":
        user_total += random.choice(cards)
        card_checker(user_card1, user_card2, user_total, computer_total)
    else:
        while computer_total < 17:
            computer_total += random.choice(cards)
        if computer_total > 21:
            print("User Wins!")
        else:
            if user_total > computer_total:
                print("User Wins!")
            elif computer_total > user_total:
                print("Computer Wins!")
            else:
                print("Draw")

is_playing = True
play = input("Do you want to play a game of BlackJack? Type y or n: ")
if play == "y":
    print(art.logo)
    while is_playing:
        blackjack()