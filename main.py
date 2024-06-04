import random
import time

def first_deal(deck):
	return random.sample(deck, 2)


def random_card(deck):
	return random.choice(deck)

def card_totals(hand):
	total = 0
	for card in hand:
		total += card
	return total



def blackjack():
	deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	computer_hand = first_deal(deck)
	player_hand = first_deal(deck)
	stand = False

	print(f"Your starting hands are - Dealer:[X, {computer_hand[1]}], You:{player_hand} \n")

	while stand == False:
		player_input = input("Hit or Stand? \n").lower()
		if player_input not in ['hit', 'stand']:
			print("Please choose 'Hit' or 'Stand'")
		elif player_input == 'hit':
			# time.sleep(1)
			player_hand.append(random_card(deck))
			print(player_hand)
			if card_totals(player_hand) > 21:
				print("You Lose!")
				return
		else:
			stand = True
	
	print(card_totals(player_hand))
	print(computer_hand)
	
	
	while card_totals(computer_hand) < 17:
		# time.sleep(1)
		computer_hand.append(random_card(deck))
		print(computer_hand)


	print(f"\nThe computer has {card_totals(computer_hand)}\n")
	print(f"You have {card_totals(player_hand)}\n")
	
	if card_totals(player_hand) > card_totals(computer_hand) and card_totals(player_hand) <= 21:
		print("You Win!!")
	elif card_totals(player_hand) == card_totals(computer_hand):
		print("Draw")
	elif card_totals(player_hand) <= 21 and card_totals(computer_hand) > 21:
		print("You Win!!")
	else:
		print("You Lose!")
	
	
blackjack()