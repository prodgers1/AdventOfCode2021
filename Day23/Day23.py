import sys
import math
import heapq
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(23)

#part 1 14348
#part 2 40954

grid = []
gridStates = []

cost = {
  'A': 1,
  'B': 10,
  'C': 100,
  'D': 1000
}

homes = {
  'A' : 3,
  "B": 5,
  "C" : 7,
  "D": 9
}

for line in _input:
  temp = []
  for c in line:
    temp.append(c)
  grid.append(temp)

gridStates.append(grid)
#print(*grid, sep="\n")

walls = set()
fish = defaultdict(list)
hangoutSpots = set()

for row in range(len(grid)):
  for col in range(len(grid[row])):
    val = grid[row][col]
    if val == '#':
      walls.add((row, col))
    
    if row == 1 and val != '#' and col not in [3, 5, 7, 9]:
      hangoutSpots.add((row,col))
    
    if "A" in val or "B" in val or "C" in val or 'D' in val:
      #current pos, cost to get to destination column, isHome
      fish[val].append([(row,col), 0, (True if homes[val] - col == 0 and row == 3 else False)])

def calculateDistanceToHome(fish):
  DR = [-1, 0, 0] #change in row
  DC = [0, 1, -1] #change in col

  for k, v in fish.items():
    temp = []
    for f in v:
      (row, col), steps, isHome = f
      startR = row
      startC = col
      if isHome:
        temp.append([(row,col), 0, isHome])
        continue
      
      stepsToReachHome = 0
      stop = False
      while not stop:
        for i in range(3):
          dr = row + DR[i]
          dc = col + DC[i]

          if (dr,dc) in walls:
            continue

          #moving away from destination
          if (abs(dc - homes[k]) > abs(homes[k] - col)):
            continue
          
          row = dr
          col = dc
          stepsToReachHome += 1

          if col == homes[k]:
            temp.append([(startR, startC), stepsToReachHome * cost[k], isHome])
            stop = True
            break

          
    
    fish[k] = temp



print(fish)
print(walls)
print(hangoutSpots)

for grid in gridStates:
  print(*grid, sep="\n")

#use a heap. the "cost" of each node is its movement. So we will always try to move A's first, B's second, etc
# once we pop a node, if we can't move it, pop the next node, try to move it. If its found its home
# don't add it back to the heap.
# If it's not in its home or can't move, add it back to the heap once the state has changed?

calculateDistanceToHome(fish)

queue = []
for k,v  in fish.items():
  for f in v:
    (row, col), costToGetToDestinationColumn, isHome = f
    if isHome:
      continue
    heapq.heappush(queue, [costToGetToDestinationColumn, k, (row,col), isHome])

def canMove(row, col, id, grid):
  DR = [-1, 0, 0] #change in row
  DC = [0, 1, -1] #change in col
  destinationColumn = homes[id]

  stop = False
  while not stop:
    for i in range(3):
      dr = row + dr
      dc = col + dc

      # its not an open spot
      if grid[dr][dc] != '.':
        return False



  return True

while queue:
  newGrid = deepcopy(grid)
  costToGetToDestinationColumn, id, (row,col), isHome = heapq.heappop()

  #first try to get the fish in the hallways home,
  #if they can't try to move the fish to hallways

  for hallwaySpot in hangoutSpots:
    row,col = hallwaySpot


  canMove(row, col, id)

  gridStates.append(newGrid)
  grid = newGrid