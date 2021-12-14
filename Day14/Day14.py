import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(14)

polymers = defaultdict(str)

for line in _input[2:]:
  polymer, result = line.strip().split(' -> ')
  polymers[polymer] = result

def part1():
  template = _input[0]
  for step in range(10):
    counts = defaultdict(int)
    newTemplate = ""
    for current, next in zip(template, template[1:]):
      if newTemplate == "":
        newTemplate += current
        counts[current] += 1
      toFind = current + next

      if toFind in polymers:
        counts[polymers[toFind]] += 1
        counts[next] += 1
        newTemplate += (polymers[toFind] + next)

    #print(newTemplate + "\n")
    template = newTemplate
    #print(template, step, counts)

  maxValue = max([x for x in counts.values()])
  minValue = min([x for x in counts.values()])
  #print(maxValue, minValue)
  print(maxValue - minValue)

def part2():
  template = _input[0]
  pairs = defaultdict(int)

  for current, next in zip(template, template[1:]):
    pairs[current+next] = 1

  lastChar = template[-1]

  for step in range(40):
    new = defaultdict(int)
    #We know that the rule AB -> C produces both AC and BC according to the rules. The RHS gets put between the pair on the left
    # and that forms another pair with the RHS as the starting character
    #If we loop through and calculate the pairs that each rule produces, we never have to calculate the string
    for pair, value in pairs.items():
      if pair in polymers:
        first = pair[0]+polymers[pair]
        new[first] += value

        second = polymers[pair] + pair[1]
        new[second] += value
    
    pairs = new
    #print(template, step, counts)

  freq = defaultdict(int)
  for pair, value in pairs.items():
    freq[pair[0]] += value
  
  freq[lastChar] += 1

  maxValue = max([x for x in freq.values()])
  minValue = min([x for x in freq.values()])

  print(maxValue - minValue)

part1()
part2()