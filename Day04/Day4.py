import sys
import math
from copy import deepcopy
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(4)

numbers = [int(x) for x in _input[0].split(',')]

class Cell:
  def __init__(self, value):
    self.Value = value
    self.Picked = False

class Board:

  def __init__(self):
    self.Board = []
    self.SumOfNonSelectedValues = 0
    self.Solved = False
  
  def UpdateSum(self):
    for line in self.Board:
      for cell in line:
        if not cell.Picked:
          self.SumOfNonSelectedValues += cell.Value
  
  def SearchForValueAndPick(self, valueToFind):
    for line in self.Board:
      for cell in line:
        if cell.Value == valueToFind:
          cell.Picked = True
          self.SumOfNonSelectedValues -= cell.Value
  
  def EvaluateGame(self):
    if self.Solved:
      return True

    solved = False
    for row in self.Board:
      solved = solved or self.CheckLine(row)
      
    if solved:
      return True

    for col in range(5):
      column = []
      for row in range(5):
        column.append(self.Board[row][col])
      solved = solved or self.CheckLine(column)
    return solved
    
  

  def CheckLine(self, line):
    for cell in line:
      if not cell.Picked:
        return False
    
    return True


def CreateBoards():
  boards = []
  board = Board()
  for line in _input[2:]:
    line = line.strip()
    if line == "":
      board.UpdateSum()
      boards.append(board)
      board = Board()
    temp = []
    for _, val in enumerate(line.split()):
      val = val.strip()
      temp.append(Cell(int(val)))
    if temp:
      board.Board.append(temp)
  
  board.UpdateSum()
  boards.append(board)
  return boards


def FindWinner(boards, part1):
  for number in numbers:
    number = int(number)
    for board in boards:
      board.SearchForValueAndPick(number)
      solved = board.EvaluateGame()

      if part1 and solved:
        return number * board.SumOfNonSelectedValues

      elif not part1 and solved and not board.Solved:

        board.Solved = True
        unsolvedBoards = [board for board in boards if not board.Solved]

        if len(unsolvedBoards) == 0:
          #print(board.SumOfNonSelectedValues)
          return number * board.SumOfNonSelectedValues

boards = CreateBoards()

part1Ans = FindWinner(deepcopy(boards), True)
part2Ans = FindWinner(deepcopy(boards), False)

print(f'Part 1: {part1Ans}')
print(f'Part 2: {part2Ans}')

