import sys
import math
from copy import deepcopy
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(3)

def part1():
  gamma = ""
  epsilon = ""

  for i in range(len(_input[0])):
    oneBits = 0
    zeroBits = 0
    for line in _input:
      if line[i] == '1':
        oneBits += 1
      else:
        zeroBits += 1
    
    if oneBits > zeroBits:
      gamma += '1'
    else:
      gamma += '0'

  for i, val in enumerate(gamma):
    if val == "1":
      epsilon += "0"
    else:
      epsilon += "1"

  print(int(gamma, 2) * int(epsilon, 2))

def part2(_input):
  def getRating(ratings, isOxygen):
    length = len(ratings[0])
    retVal = 0
    prefix = ""
    for i in range(length):
      oneBits = 0
      zeroBits = 0
      for line in ratings:
        if line[i] == '1':
          oneBits += 1
        else:
          zeroBits += 1
      
      if isOxygen:
        if oneBits >= zeroBits:
          prefix += '1'
        else:
          prefix += '0'
      else:
        if oneBits < zeroBits:
          prefix += '1'
        else:
          prefix += '0'
      
      temp = []
      for i in range(len(ratings)):
        if ratings[i].startswith(prefix):
          temp.append(ratings[i])
      
      ratings = temp

      if len(ratings) == 1:
        retVal = ratings[0]
    return retVal
  
  oxygen = getRating(deepcopy(_input), True)
  co2 = getRating(deepcopy(_input), False)

  print(int(oxygen, 2) * int(co2, 2))
    
part1()
part2(_input)