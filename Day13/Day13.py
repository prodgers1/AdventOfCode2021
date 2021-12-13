import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(13)

dots = set()
folds = []

maxX = 0
maxY = 0

for line in _input:
  if ',' in line:
    x, y = line.split(',')
    x = int(x)
    y = int(y)

    if x > maxX:
      maxX = x
    
    if y > maxY:
      maxY = y

    dots.add((x,y))
  
  elif "fold" in line:
    _, _, l=  line.split()
    folds.append(l)

#print(dots, folds)
#print(maxX, maxY)

paper = [['.' for x in range(maxX+1)] for y in range(maxY+1)]

for dot in dots:
  x, y = dot
  paper[y][x] = '#'



for fold in folds:
  line, lineNum = fold.split("=")
  lineNum = int(lineNum)

  if line == 'y':
    topGrid = [[paper[y][x] for x in range(len(paper[0]))] for y in range(len(paper)) if y < int(lineNum)]
    bottomGrid = [[paper[y][x] for x in range(len(paper[0]))] for y in range(len(paper)) if y > int(lineNum)]
    #start from bottom left, work up
    i = 0
    topI = len(topGrid) - 1
    while topI >= 0 and i < len(bottomGrid[0]):
      for col in range(len(bottomGrid[0])):
        if bottomGrid[i][col] == '#':
          topGrid[topI][col] = '#'
      
      i += 1
      topI -= 1

    paper = topGrid
    

  else:
    leftGrid = [['.' for x in range(lineNum)] for y in range(len(paper))]
    rightGrid = [['.' for x in range(lineNum, len(paper[0]) - 1)] for y in range(len(paper))]
    
    for row in range(len(leftGrid)):
      for col in range(len(leftGrid[0])):
        leftGrid[row][col] = paper[row][col]
    
    for row in range(len(rightGrid)):
      for col in range(len(rightGrid[0])):
        rightGrid[row][col] = paper[row][col+lineNum + 1]

    #start from top right, work left
    i = 0
    leftI = len(leftGrid[0]) - 1
    while leftI >= 0 and i < len(rightGrid[0]):
      for row in range(len(rightGrid)):
        if rightGrid[row][i] == '#':
          leftGrid[row][leftI] = '#'

      i += 1
      leftI -= 1
    

    paper = leftGrid
  #add this break to get part 1, answer is 847
  #break
  

for line in paper:
  print(' '.join(line)) 


ans = 0
for row in range(len(paper)):
  for col in range(len(paper[0])):
    if paper[row][col] == '#':
      ans += 1

print(ans)