from os import sep
import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(25)



trench = list()

eastFacing = set()
southFacing = set()

for line in _input:
  temp = []
  for c in line:
    temp.append(c)
  trench.append(temp)

R = len(trench)
C = len(trench[0])

for row in range(R):
  for col in range(C):
    if trench[row][col] == '>':
      eastFacing.add((row,col))
    
    elif trench[row][col] == 'v':
      southFacing.add((row,col))

def show(east, south):
  grid = list()
  for row in range(R):
    temp = []
    for col in range(C):
      if (row, col) in east:
        temp.append('>')
      elif (row, col) in south:
        temp.append('v')
      else:
        temp.append('.')
    grid.append(temp)
  
  for line in grid:
    print(''.join(line))
  


done = False
steps = 0
while not done:
  steps += 1
  done = True
  newEast = set()
  newSouth = set()

  for cucumber in eastFacing:
    row, col = cucumber
    nextCol = col

    if col + 1 >= C:
      nextCol = 0
    else:
      nextCol = col + 1
    
    if (row, nextCol) in eastFacing or (row, nextCol) in southFacing:
      newEast.add((row, col))
      continue
    
    done = False
    newEast.add((row, nextCol))

  eastFacing = newEast

  for cucumber in southFacing:
    row, col = cucumber
    nextRow = row

    if row + 1 >= R:
      nextRow = 0
    else:
      nextRow = row + 1

    #something is in the way
    if (nextRow, col) in eastFacing or (nextRow, col) in southFacing:
      newSouth.add((row, col))
      continue
    
    done = False
    newSouth.add((nextRow, col))
  
  southFacing = newSouth

  #show(eastFacing, southFacing)
    
print(steps)