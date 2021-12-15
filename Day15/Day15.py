import sys
import math
import heapq
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(15)

def part1():
  grid = []
  for line in _input:
    temp = []
    for c in line:
      temp.append(int(c))
    
    grid.append(temp)

  #directions,   down right left up
  DR = [1, 0, 0, -1,] #change in row
  DC = [0, 1, -1, 0] #change in col

  start = (0, 0)
  queue = [(0, start, [])]
  seen = set()

  while queue:
    cost, (row,col), path = heapq.heappop(queue)
    
    if (row,col) in seen:
      continue
    
    path = path + [(row,col)]
    seen.add((row,col))

    if row == len(grid)-1 and col == len(grid[0])-1:
      #print(cost, path)
      print(cost)
      break

    for d in range(4):
      dr = row + DR[d]
      dc = col + DC[d]
      
      if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]):
        newCost = cost + grid[dr][dc]
        heapq.heappush(queue, (newCost, (dr, dc), path))

def part2():
  grid = []
  for line in _input:
    temp = []
    for c in line:
      temp.append(int(c))
    
    grid.append(temp)

  length_Grid = len(grid)
  length_Col = len(grid[0])

  for row in range(length_Grid * 4):
    offset = 1 
    temp = []
    for col in range(length_Col * 4):
      copyVal = grid[row][col]
      
      if copyVal == 9:
        grid[row].append(1)
      else:
        grid[row].append(copyVal + 1)

    copyRow = grid[row]
    for c in copyRow:
      c = int(c)
      if c + offset > 9:
        temp.append(1)
      else:
        temp.append(c + offset)

    grid.append(temp)

  #directions,   down right left up
  DR = [1, 0, 0, -1,] #change in row
  DC = [0, 1, -1, 0] #change in col

  start = (0, 0)
  queue = [(0, start, [])]
  seen = set()

  while queue:
    cost, (row,col), path = heapq.heappop(queue)
    
    if (row,col) in seen:
      continue
    
    path = path + [(row,col)]
    seen.add((row,col))

    if row == len(grid)-1 and col == len(grid[0])-1:
      #print(cost, path)
      print(cost)
      break

    for d in range(4):
      dr = row + DR[d]
      dc = col + DC[d]
      
      if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]):
        newCost = cost + grid[dr][dc]
        heapq.heappush(queue, (newCost, (dr, dc), path))

part1()
part2()