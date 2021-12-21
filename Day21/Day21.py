import sys
import math
from copy import deepcopy
from collections import defaultdict
from functools import lru_cache
from itertools import product
import time
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(21)

class Player:
  def __init__(self, id, startingPos):
    self.Id = id
    self.Position = int(startingPos)
    self.Score = 0
    self.Wins = 0
    self.Universes = 0
  
  def Move(self, steps):
    for step in range(1, steps+1):
      if self.Position + 1 > 10:
        self.Position = 1
      else:
        self.Position += 1

    self.Score += self.Position
  
  def DidWin(self):
    return self.Score >= 1000
  
  def DidWinPart2(self):
    return self.Score >= 21
  
  def Win(self):
    self.Wins += 1

def setup():
  players = list()
  for line in _input:
    splitline = line.split()
    players.append(Player(splitline[1], splitline[4]))
  return players



def rollDie(die):
  temp = die
  die = (die % 100) + 1
  return temp, die


dieRolled = 0
def play(players):
  global dieRolled
  die = 1
  
  while True:
    for player in players:
      
      roll1, die = rollDie(die)
      roll2, die = rollDie(die)
      roll3, die = rollDie(die)

      dieRolled += 3

      toMove = roll1 + roll2 + roll3
      player.Move(toMove)

      win = player.DidWin()

      if win:
        return player.Id

@lru_cache(None)
def playGame(player1Pos, player2Pos, player1Score, player2Score):

  if player1Score >= 21:
    return [1,0]

  if player2Score >= 21:
    return [0,1]

  wins = [0,0]
  
  for x in [1,2,3]:
    for y in [1,2,3]:
      for z in [1,2,3]:
        roll = x + y + z
        newPos = (player1Pos + roll) % 10
        if newPos == 0:
          newPos = 10

        newScore = player1Score + newPos

        #in the first iteration, its now player 2's turn.
        #essentially always flip who's turn it is, passing in the new position and score
        # for the player who just took their turn
        player2Wins, player1Wins = playGame(player2Pos, newPos, player2Score, newScore)
        # after this game is played, it was player 2's turn, so his wins are going to be in the 0th index
        # and player 1 (which was the second player in this next turn) is in the first index
        wins[0] += player1Wins
        wins[1] += player2Wins
  
  return wins[0], wins[1]

def part2(players):
  start = time.time()
  wins = playGame(players[0].Position, players[1].Position, 0, 0)
  end = time.time()
  print(end-start, wins, max(wins))
  

players = setup()
winnerId = play(players)
loser = [player for player in players if player.Id != winnerId][0]
print(loser.Score * dieRolled)

players = setup()
part2(players)





