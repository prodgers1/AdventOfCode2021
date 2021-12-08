import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(8)

def part1():
  total = 0
  for line in _input:
    patterns, output = line.split("|")

    patterns = patterns.strip().split(" ")
    output = output.strip().split(" ")

    for digit in output:
      if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
        total += 1
    
  print(total)

def isThree(knownNumbers, pattern):
  isThree = True
  for char in knownNumbers[1]:
    if char not in pattern:
      isThree = False
      break
  
  return isThree

#must contain at least 3 of the 4 digits of 4
def isFive(knownNumbers, pattern):
  count = 0
  isFive = False
  for char in knownNumbers[4]:
    if char in pattern:
      count += 1
    if count == 3:
      isFive = True
      break
  
  return isFive

def isNine(knownNumbers, pattern):
  isNine = True 
  for char in knownNumbers[4]:
    if char not in pattern:
      isNine = False
  
  return isNine

def isZero(knownNumbers, pattern):
  isZero = True
  for char in knownNumbers[1]:
    if char not in pattern:
      isZero = False
  
  return isZero


def part2():
  totalSum = []
  for line in _input:
    patterns, output = line.split("|")

    patterns = patterns.strip().split(" ")
    output = output.strip().split(" ")

    sortedPatterns = sorted(patterns, key=len)
    
    knownNumbers = defaultdict()

    for pattern in sortedPatterns:
      if len(pattern) == 2:
        knownNumbers[1] = [x for x in pattern]
      elif len(pattern) == 3:
        knownNumbers[7] = [x for x in pattern]
        
      elif len(pattern) == 4:
        knownNumbers[4] = [x for x in pattern]
      
      elif len(pattern) == 5: #2 3 or 5
        isNumberThree = isThree(knownNumbers, pattern)
        if isNumberThree:
          knownNumbers[3] = [x for x in pattern]
          continue
        
        isNumberFive = isFive(knownNumbers, pattern)
        if isNumberFive:
          knownNumbers[5] = [x for x in pattern]
          continue
        if not isNumberFive and not isNumberThree:
          knownNumbers[2] = [x for x in pattern]

      if len(pattern) == 6: #6 9 or 0
        isNumberNine = isNine(knownNumbers, pattern)
        if isNumberNine:
          knownNumbers[9] = [x for x in pattern]
          continue
        
        isNumberZero = isZero(knownNumbers, pattern)
        if isNumberZero:
          knownNumbers[0] = [x for x in pattern]
          continue
        
        if not isNumberZero and not isNumberNine:
          knownNumbers[6] = [x for x in pattern]
      
      if len(pattern) == 7:
        knownNumbers[8] = [x for x in pattern]
    
    ans = ""
    for number in output:
      for key, value in knownNumbers.items():
        potentialNumber = ''.join(value)

        if sorted(potentialNumber) == sorted(number):
          ans += str(key)
    
    totalSum.append(ans)
  
  print(sum([int(x) for x in totalSum]))
      
      
part1()
part2()
  