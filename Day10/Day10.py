import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(10)

corrupted = []
incomplete = []
valid = []

def part1():
  part1Lookup = {}
  part1Lookup[')'] = 3
  part1Lookup[']'] = 57
  part1Lookup['}'] = 1197
  part1Lookup['>'] = 25137

  for line in _input:
    stack = []
    isCorrupted = False
    for char in line:

      if char == '(':
        stack.append(')')
      elif char == '[':
        stack.append(']')
      elif char == '{':
        stack.append('}') 
      elif char == '<':
        stack.append('>')
      else:
        top = stack.pop()
        if top != char:
          corrupted.append(char)
          isCorrupted = True
    
    if len(stack) == 0:
      valid.append(line)
    elif not isCorrupted:
      incomplete.append(line)

  total = 0
  for char in corrupted:
    total += part1Lookup[char]

  print(total)

def part2():
  lookup = {}
  lookup[')'] = 1
  lookup[']'] = 2
  lookup['}'] = 3
  lookup['>'] = 4

  scores = []
  for line in _input:
    stack = []
    isCorrupted = False
    for char in line:

      if char == '(':
        stack.append(')')
      elif char == '[':
        stack.append(']')
      elif char == '{':
        stack.append('}') 
      elif char == '<':
        stack.append('>')
      else:
        top = stack.pop()
        if top != char:
          corrupted.append(char)
          isCorrupted = True
    
    if len(stack) == 0:
      valid.append(line)
    elif not isCorrupted:
      incomplete.append(line)

      total = 0
      stack = reversed(stack)

      for char in stack:
        total = (total * 5) + lookup[char]

      scores.append(total)
  
  scores = sorted(scores)

  print(scores[len(scores) // 2])


part1()
part2()