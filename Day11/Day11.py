import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(11)

octopuses = []

for line in _input:
  temp = []
  for octopus in line:
    temp.append(int(octopus))
  
  octopuses.append(temp)

ROW_LENGTH = len(octopuses)
COL_LENGTH = len(octopuses[0])

def part1(octopuses):
  totalFlashes = 0
  for i in range(100):
    flashed = []
    for row in range(ROW_LENGTH):
      for col in range(COL_LENGTH):
        octopuses[row][col] += 1

        if octopuses[row][col] > 9:
          totalFlashes += 1
          flashed.append((row,col))
    
    done = deepcopy(flashed)
    while flashed:
      row, col = flashed.pop()

      for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
          if dx == 0 and dy == 0:
            continue
          dr = row + dx
          dc = col + dy

          if 0 <= dr < ROW_LENGTH and 0 <= dc < COL_LENGTH:
            octopuses[dr][dc] += 1

            if octopuses[dr][dc] > 9 and (dr, dc) not in done:
              totalFlashes += 1
              flashed.append((dr, dc))
              done.append((dr, dc))

    for row,col in done:
      octopuses[row][col] = 0

  print(totalFlashes)

def part2(octopuses):
  i = 0
  while True:
    flashed = []
    for row in range(ROW_LENGTH):
      for col in range(COL_LENGTH):
        octopuses[row][col] += 1

        if octopuses[row][col] > 9:
          flashed.append((row,col))
    

    done = deepcopy(flashed)
    while flashed:
      row, col = flashed.pop()

      for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
          if dx == 0 and dy == 0:
            continue
          dr = row + dx
          dc = col + dy

          if 0 <= dr < ROW_LENGTH and 0 <= dc < COL_LENGTH:
            octopuses[dr][dc] += 1

            if octopuses[dr][dc] > 9 and (dr, dc) not in done:
              flashed.append((dr, dc))
              done.append((dr, dc))
    
    if len(done) == ROW_LENGTH * COL_LENGTH:
      print(i + 1)
      break

    for row,col in done:
      octopuses[row][col] = 0
    
    i += 1

part1(deepcopy(octopuses))
part2(deepcopy(octopuses))