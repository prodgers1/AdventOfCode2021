import sys
import math
from copy import deepcopy
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(5)

def part1():
  coords = {}
  for line in _input:
    x1y1, x2y2 = line.split('->')

    x1, y1 = x1y1.strip().split(',')
    x2, y2 = x2y2.strip().split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    if x1 == x2:
      minY = min(y1, y2)
      maxY = max(y1, y2)
      for i in range(minY, maxY+1):
        if (x1, i) in coords:
          coords[(x1, i)] += 1
        else :
          coords[(x1, i)] = 1
          
    elif y1 == y2:
      minX = min(x1, x2)
      maxX = max(x1, x2)
      for i in range(minX, maxX+1):
        if (i, y1) in coords:
          coords[(i, y1)] += 1
        else :
          coords[(i, y1)] = 1
      
  print(sum([1 for (x,y) in coords if coords[(x,y)] >= 2]))

def part2():
  coords = {}
  #horizontal and vertical
  for line in _input:
    x1y1, x2y2 = line.split('->')

    x1, y1 = x1y1.strip().split(',')
    x2, y2 = x2y2.strip().split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    if x1 == x2:
      minY = min(y1, y2)
      maxY = max(y1, y2)
      for i in range(minY, maxY+1):
        if (x1, i) in coords:
          coords[(x1, i)] += 1
        else :
          coords[(x1, i)] = 1

    elif y1 == y2:
      minX = min(x1, x2)
      maxX = max(x1, x2)
      for i in range(minX, maxX+1):
        if (i, y1) in coords:
          coords[(i, y1)] += 1
        else :
          coords[(i, y1)] = 1
    
    #diagonal
    else:
      start = (x1, y1)
      end = (x2, y2)
      dx, dy = (1 if x1 < x2 else -1 ), (1 if y1 < y2 else -1)
      
      while start != end:
        if start in coords:
          coords[start] += 1
        else:
          coords[start] = 1
        
        start = (start[0] + dx, start[1] + dy)

      if start in coords:
        coords[start] += 1
      else:
        coords[start] = 1

  print(sum([1 for (x,y) in coords if coords[(x,y)] >= 2]))

part1()
part2()
