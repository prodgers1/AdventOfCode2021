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
  #directions, up right down left
  DR = [-1, 0, 1, 0] #change in row
  DC = [0, 1, 0, -1] #change in col
  for row in range(len(heatmap)):
    for col in range(len(heatmap[0])):
      toCheck = heatmap[row][col]
      potential = []
      
      for d in range(4):
        dr = row + DR[d]
        dc = col + DC[d]

        if 0 <= dr < len(heatmap) and 0 <= dc < len(heatmap[0]):
          potential.append(heatmap[dr][dc])

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
  #directions, up right down left
  DR = [-1, 0, 1, 0] #change in row
  DC = [0, 1, 0, -1] #change in col
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
          
          #loop over all the directions, up right down left
          for d in range(4):
            dr = row + DR[d]
            dc = col + DC[d]

            if 0 <= dr < len(heatmap) and 0 <= dc < len(heatmap[0]) and heatmap[dr][dc] != 9 and (dr, dc) not in checked:
              potential.append((dr, dc))
          
        
        basins.append(basin)

  sortedBasins = sorted(basins, key=len, reverse=True)
  
  ans = 1
  for basin in sortedBasins[:3]:
    ans *= len(basin)
  
  print(ans)


part1()
part2()


