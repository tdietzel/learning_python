import random

def create_deck():
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
  random.shuffle(deck)
  return deck

def deal_hand(hand, house):
  if house:
    for card in hand:
      print('House cards', f"{card['rank']} of {card['suit']}")
  else:
    for card in hand:
      print('Your cards', f"{card['rank']} of {card['suit']}")
  return hand

def card_value(card):
  rank = card['rank']
  if rank in [ 'J', 'Q', 'K']:
    return 10
  elif rank == 'A':
    return 11
  else:
    return int(rank)

def count_Score(hand):
  score = 0
  for card in hand:
    score += card_value(card)
  return score

def black_jack():
  deck = create_deck()

  print("~---~---~---~----~---~---~---~----~")
  player_hand = [deck.pop(), deck.pop()]
  house_hand = [deck.pop(), deck.pop()]
  deal_hand(player_hand, house = False)
  deal_hand(house_hand, house = True)
  player_score = count_Score(player_hand)
  house_score = count_Score(house_hand)

  print("~---~---~---~----~---~---~---~----~")
  print(f"Your total: {player_score} | House total: {house_score}")
  print("___________________________________")
  game_choice = input("Do you want to 'hit' or 'stand'? ").lower
  
  if game_choice == 'hit':
    player_hand.append(deck.pop())
    player_hand = count_Score(player_hand)
    house_hand = count_Score(house_hand)
    print(f"Your total: {player_score} | House total: {house_score}")
  elif game_choice == 'stand':
    if player_hand < house_hand and house_hand < 21:
      print('You lost')
    elif player_hand > house_hand and player_hand < 21:
      print('You win')
    elif player_hand == 21:
      print('Blackjack! You win')
    elif house_hand == 21:
      print('House got Blackjack! You lose')
    else:
      print("error")
  return player_hand, house_hand, player_score, house_score, game_choice

black_jack()