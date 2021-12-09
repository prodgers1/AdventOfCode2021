import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(9)

heatmap = []

for line in _input:
  temp = []
  for c in line:
    temp.append(int(c))
  heatmap.append(temp)


def part1():
  ans = []
  for row in range(len(heatmap)):
    for col in range(len(heatmap[0])):
      toCheck = heatmap[row][col]
      potential = []

      #up
      if row - 1 >= 0:
        potential.append(heatmap[row-1][col])
      #left
      if col - 1 >= 0:
        potential.append(heatmap[row][col - 1])
      #right
      if col + 1 < len(heatmap[0]):
        potential.append(heatmap[row][col + 1])
      #down
      if row + 1 < len(heatmap):
        potential.append(heatmap[row+1][col])
      
      good = True
      for num in potential:
        if toCheck >= num:
          good = False
          break
      
      if not good:
        continue
      
      ans.append(toCheck + 1)

  #print(ans)
  print(sum(ans))

def part2():
  ans = []
  checked = set()
  basins = []
  for row in range(len(heatmap)):
    for col in range(len(heatmap[0])):
      current = heatmap[row][col]
      if current == 9:
        checked.add((row,col))
        continue
      if (row,col) not in checked:
        potential = []
        potential.append((row,col))

        basin = []
        while len(potential) > 0:
          row, col = potential.pop()
          
          if (row,col) in checked:
            continue

          checked.add((row,col))
          basin.append(heatmap[row][col])
          
          #up
          if row - 1 >= 0 and heatmap[row-1][col] != 9 and (row - 1, col) not in checked:
            potential.append((row-1, col))
          #left
          if col - 1 >= 0 and heatmap[row][col - 1] != 9 and (row, col - 1) not in checked:
            potential.append((row, col - 1))
          #right
          if col + 1 < len(heatmap[0]) and heatmap[row][col + 1] != 9 and (row, col + 1) not in checked:
            potential.append((row, col + 1))
          #down
          if row + 1 < len(heatmap) and heatmap[row+1][col] != 9 and (row + 1, col) not in checked:
            potential.append((row + 1, col))
        
        basins.append(basin)

  sortedBasins = sorted(basins, key=len, reverse=True)
  
  ans = 1
  for basin in sortedBasins[:3]:
    ans *= len(basin)
  
  print(ans)


part1()
part2()


