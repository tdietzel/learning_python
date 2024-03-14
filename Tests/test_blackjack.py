import sys
sys.path.append('..')
import blackjack #ignore

import unittest

class BlackJackTests(unittest.TestCase):

  def test_deck(self):
    game = blackjack.create_deck()
    self.assertEqual(len(game), 52)

  def test_dealHand(self):
    playerHand, houseHand = blackjack.black_jack()
    self.assertEqual(len(playerHand), 2)
    self.assertEqual(len(houseHand), 2)

  # def test_handValue(self):
  #   player_hand, house_hand, player_score, house_score = blackjack.black_jack()

  #   self.assertEqual(player_score)

if __name__ == '__main__':
  unittest.main()