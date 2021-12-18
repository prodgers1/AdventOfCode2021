import sys
import math
import ast
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(18)

def findLeft(snailfish, currentIndex):

  for i in range(currentIndex, 0, -1):
    char = snailfish[i]

    if char.isdigit():
      return int(char), i
  
  return None, -1

def findRight(snailfish, currentIndex):
  for i in range(currentIndex, len(snailfish)):
    char = snailfish[i]

    if char.isdigit():
      return int(char), i
  
  return None, -1


def explode(snailfish, index):
  leftVal = int(snailfish[index + 1])
  rightVal = int(snailfish[index + 3])

  leftNum, indexOfLeftNum = findLeft(snailfish, index)

  if indexOfLeftNum != -1:
    snailfish[indexOfLeftNum] = str((leftNum + leftVal))
  
  #start after the right number in the current pair
  rightNum, indexOfRightNum = findRight(snailfish, index+4)

  if indexOfRightNum != -1:
    snailfish[indexOfRightNum] = str((rightVal + rightNum))

  return snailfish[:index] + ['0'] + snailfish[index+5:]

def split(snailfish, index):
  valAtIndex = int(snailfish[index])

  newLeft = math.floor(valAtIndex / 2)
  newRight = math.ceil(valAtIndex / 2)

  snailfish = snailfish[:index] + ["["] + [str(newLeft)] + [","] + [str(newRight)] + [']'] + snailfish[index+1:]

  return snailfish

def reduce(snailfish):
  changed = True
  while changed:
    changed = False
    depth = 0

    for i, char in enumerate(snailfish):
      if char == ']':
        depth -= 1
      elif char == '[':
        depth += 1
      
        #5 because im including the outermost scope as well
        if depth == 5:
          snailfish = explode(snailfish, i)
          #print(''.join([str(x) for x in snailfish]))
          changed = True
          break

    if changed:
      continue
    
    for i, char in enumerate(snailfish):
      if char.isdigit() and int(char) > 9:
        snailfish = split(snailfish, i)
        #print(''.join([str(x) for x in snailfish]))
        changed = True
        break

  return snailfish

def add(current, snailfishToAdd):

  result = []
  result.extend('[')
  result.extend(current)
  result.extend(',')
  result.extend(snailfishToAdd)
  result.extend(']')

  snailfish = reduce(result)
  return snailfish

def magnitude(snailfish):
  while len(snailfish) > 1:
    for i, val in enumerate(snailfish):
      if val.isdigit() and snailfish[i + 2].isdigit():
        lhs = int(val) * 3
        rhs = int(snailfish[i+2]) * 2

        new = lhs + rhs

        startOfPair = i - 1
        endOfPair = i + 4

        snailfish = snailfish[:startOfPair] + [str(new)] + snailfish[endOfPair:]
        break
  
  return int(snailfish[0])

def part1(snailfish):
  current = None
  for i, snailfish in enumerate(snailfish):
    if current == None:
      current = snailfish
      continue
    
    current = add(current, snailfish)
  
  print(magnitude(current))
  
def part2(snailfish):
  maxMagnitude = 0
  for i, s1 in enumerate(snailfish):
    for j, s2 in enumerate(snailfish):
      if i != j:
        reduced = add(s1, s2)
        reducedMagnitude = magnitude(reduced)
        maxMagnitude = max(maxMagnitude, reducedMagnitude)
  
  print(maxMagnitude)

snailfish = []

for line in _input:
  snailfish.append([x for x in line.strip()])

part1(deepcopy(snailfish))
part2(deepcopy(snailfish))
