import random
import os
from art import logo
# To clear the console after the game is over
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# the function which gives the cards 
def deal_cards():
    """Returns a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
# A function calculate the score
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)
# A function to compare scores of the computer and the user 
def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif user_score > 21 and computer_score > 21:
        return "You went over. You Lose! :("
    elif user_score == 21:
        return "You win with a Blackjack! :o"
    elif computer_score == 21:
        return "Computer has a Blackjack. You lose! :("
    elif user_score > 21:
        return "You went over. You lose! :("
    elif computer_score > 21: 
        return "Computer went over. You win! :)"
    elif user_score > computer_score:
        return "You win! :)"
    else:
        return "You lose! :("
# Function to start the game 
def start_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}") 
        print(f"    Computer's first card: {computer_cards[0]}")
        if user_score == 21 or computer_score == 21 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card - Type'n' to pass:\t")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True
    while computer_score != 21 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    print(f"    Your final hand: {user_cards}, Final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, Final score: {computer_score}")
    print(compare_scores(user_score, computer_score))
while input("Do you want to start a round of Blackjack? Type 'y' to start or 'n' to quit: ").lower() == 'y':
    clear()
    start_game()
print("Goodbye!")
