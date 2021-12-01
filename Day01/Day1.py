import sys
import math
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(1)

def part1():
  counter = 1
  for i in range(1, len(_input)):
    prev = _input[i-1]
    current = _input[i]

    if current > prev:
      counter += 1

  print(counter)

def part2():
  counter = 0
  prevSum = 99999999999999
  for i in range(len(_input)):

    if i+1 >= len(_input) or i+2 >= len(_input):
      break

    first = int(_input[i])
    second = int(_input[(i+1)])
    third = int(_input[(i+2)])

    if (first + second + third) > prevSum:
      counter += 1
    
    prevSum = first + second + third
  
  print(counter)

    

part1()
part2()