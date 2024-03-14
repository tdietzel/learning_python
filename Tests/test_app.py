import sys
sys.path.append("..")
from app import RPSGame
import unittest
from unittest.mock import patch

class UnitTest(unittest.TestCase):

  def setUp(self):
    self.patcher = patch('builtins.input', return_value = 'rock')
    self.patcher.start()
    self.testGame = RPSGame()

  def tearDown(self):
    self.patcher.stop()

  def test_userChoice(self):
    # testGame = RPSGame()
    self.assertEqual(self.testGame.userInput, 'rock')

  def test_computerChoice(self):
    # testGame = RPSGame()
    self.assertTrue(self.testGame.computerChoice in [ 'rock', 'paper', 'scissors' ])
    
  def test_gameWinner(self):
    self.assertTrue(self.testGame.gameWinner in [ 'player', 'computer', 'draw' ])

if __name__ == "__main__":
  unittest.main()