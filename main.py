import random

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
	computer_count = 0
	player_hand = first_deal(deck)
	player_count = 0
	stand = False



	print(f"Your starting hand is {player_hand}")
	# print(computer_hand[0], player_hand)

	while stand == False:
		
		player_input = input("Hit or Stand? \n").lower()
		if player_input not in ['hit', 'stand']:
			print("Please choose 'Hit' or 'Stand'")
		elif player_input == 'hit':
			player_hand.append(random_card(deck))
			print(player_hand)
		else:
			stand = True
	print(card_totals(player_hand))
	
	
	
	
			
	# print(computer_hand)
	# computer_hand.append(deal_card)
	# print(computer_hand)
	

	

blackjack()