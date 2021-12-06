import sys
import math
from copy import deepcopy
sys.path.append('./')
from adventInput import GetInput
import time

_input = GetInput(6)

fishes = [int(x) for x in _input[0].split(',')]

def bruteForce(fishes):

  startTime = time.time()
  day = 1
  end = 256
  while day <= end:
    toAdd = []
    for i in range(len(fishes)):
       if fishes[i] == 0:
         toAdd.append(8)
         fishes[i] = 6
       else:
         fishes[i] -= 1
    
    fishes.extend(toAdd)
    #out of memory at day 148, 444 seconds elapsed
    #Day 148: Number of fish: 144554335. Duration: 444.9987280368805 seconds
    print(f"Day {day}: Number of fish: {len(fishes)}. Duration: {time.time() - startTime} seconds")
    day += 1
  
  print(f"DONE!!!!! Number of fish: {len(fishes)}. Duration: {time.time() - startTime} seconds")

def spawnFish(end, fishes):
  day = 1
  daysRemaining = {}

  for i in range(10):
    daysRemaining[i] = 0

  for fish in fishes:
    daysRemaining[fish] += 1
    
  while day <= end:
    days = deepcopy(daysRemaining)
    for key, value in days.items():
      if key == 0:
        daysRemaining[8] += value
        daysRemaining[6] += value
        daysRemaining[0] -= value

      else:
        daysRemaining[key] -= value
        daysRemaining[key-1] += value

    day += 1
    
  total = 0
  for key, value in daysRemaining.items():
    total += value
  print(total)

bruteForce(fishes)
#spawnFish(80, fishes)
#spawnFish(256, fishes)
