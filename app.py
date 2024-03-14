import random

class RPSGame():
  def __init__(self):
    self.userInput = input("Make your choice: ").lower()
    print(self.userInput) #remove
    computerChoice = random.randint(1, 3)
    if computerChoice == 1:
      self.computerChoice = 'rock'
      print('computer chose rock') #remove
    elif computerChoice == 2:
      self.computerChoice = 'paper'
      print('computer chose paper') #remove
    elif computerChoice == 3:
      self.computerChoice = 'scissors'
      print('computer chose scissors') #remove
    if computerChoice == 1 and self.userInput == 'rock' or computerChoice == 2 and self.userInput == 'paper' or computerChoice == 3 and self.userInput == 'scissors':
      self.gameWinner = 'draw'
      print('DRAW') #remove
    elif computerChoice == 1 and self.userInput == 'scissors' or computerChoice == 2 and self.userInput == 'rock' or computerChoice == 3 and self.userInput == 'paper':
      self.gameWinner = 'computer'
      print('COMPUTER WINS') #remove
    elif self.userInput == 'rock' and computerChoice == 3 or self.userInput == 'paper' and computerChoice == 1 or self.userInput == 'scissors' and computerChoice == 2:
      self.gameWinner = 'user'
      print('USER WINS') #remove