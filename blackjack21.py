import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    permission = input("Do you want to play blackjack? (y/n): ")
    if permission.lower() != "y":
        break
    
    # Initialize player and computer cards
    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    
    # Player's turn
    print(f"\nYour cards: {player_cards}, Score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    while sum(player_cards) <= 21:
        choice = input("Do you want another card? (y/n): ")
        if choice.lower() == "y":
            player_cards.append(random.choice(cards))
            print(f"Your cards: {player_cards}, Score: {sum(player_cards)}")
        else:
            break
    
    player_score = sum(player_cards)
    
    # Computer's turn
    while sum(computer_cards) < 21:
        computer_cards.append(random.choice(cards))
    
    computer_score = sum(computer_cards)
    
    # Show final scores
    print(f"\nYour final cards: {player_cards}, Score: {player_score}")
    print(f"Computer's cards: {computer_cards}, Score: {computer_score}")
    
    # Determine winner
    if player_score > 21:
        print("Busted - you lose!")
    elif computer_score > 21:
        print("Computer busted - you won!")
    elif player_score > computer_score:
        print("You won!")
    elif player_score == 21:
        print("You won!")
    elif computer_score == 21:
        print("computer won!!!!")
    elif player_score == computer_score:
        print("tie")
    elif player_score < 21:
        print("You busted - you lose!")
    elif computer_score < 21:
        print("you won")
    else:
        print("You lose!")

    