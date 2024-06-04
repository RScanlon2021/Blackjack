import random
import time

def first_deal(deck):
	return random.sample(deck, 2)

def random_card(deck):
	return random.choice(deck)

def card_totals(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def new_game_option():
	new_game = False
	while new_game == False:
		play_new_game = input("Would you like to play another hand? 'Y' or 'N'? \n").lower()
		if play_new_game not in ['y', 'n']:
			print("Please choose 'Y' or 'N'.\n")
		elif play_new_game == 'y':
			new_game = True
			blackjack()
		elif play_new_game == 'n':
			print("Thank you for playing at Caesar's Palace!")
			return
		
def winner(player_hand, computer_hand):
	if card_totals(player_hand) > card_totals(computer_hand) and card_totals(player_hand) <= 21:
		print("You Win!!\n")
	elif card_totals(player_hand) == card_totals(computer_hand):
		print("Draw\n")
	elif card_totals(player_hand) <= 21 and card_totals(computer_hand) > 21:
		print("You Win!!\n")
	else:
		print("You Lose!\n")

def blackjack():
	deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	computer_hand = first_deal(deck)
	player_hand = first_deal(deck)
	stand = False

	print(f"Your starting hands are - Dealer:[X, {computer_hand[1]}], You:{player_hand} \n")
	# Handles player cards
	while stand == False:
		player_input = input("\nHit or Stand?\n").lower()
		if player_input not in ['hit', 'stand']:
			print("Please choose 'Hit' or 'Stand'")
		elif player_input == 'hit':
			time.sleep(.5)
			player_hand.append(random_card(deck))
			print(player_hand)
			if card_totals(player_hand) > 21:
				if 11 in player_hand: # Handles ace handling
					player_hand[player_hand.index(11)] = 1
				else:
					print("You Lose!")
					new_game_option()
					return
		else:
			stand = True
	
	print(f"Your total is {card_totals(player_hand)}\n")
	print(computer_hand)
	# Handles Computer cards and ace handling
	while True:
		time.sleep(1)
		if 11 in computer_hand and card_totals(computer_hand) > 21:
			computer_hand[computer_hand.index(11)] = 1
			print(computer_hand)
		elif 11 in computer_hand and card_totals(computer_hand) >= 17 and card_totals(computer_hand) < card_totals(player_hand):
			computer_hand[computer_hand.index(11)] = 1
			print(computer_hand)
		elif card_totals(computer_hand) < 17:
			computer_hand.append(random_card(deck))
			print(computer_hand)
		else:
			break
		
	print(f"\nThe computer has {card_totals(computer_hand)}\n")
	print(f"You have {card_totals(player_hand)}\n")
	# Handles winner logic
	winner(player_hand, computer_hand)
	new_game_option()
	
blackjack()