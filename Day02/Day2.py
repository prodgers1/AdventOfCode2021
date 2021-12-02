import sys
import math
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(2)


def part1():
  x = 0
  y = 0
  for line in _input:
    direction, units = line.split(' ')
    units = int(units)
    if direction == 'forward':
      x += units
    elif direction == 'down':
      y += units
    elif direction == "up":
      y -= units
    
  print(x * y)

def part2():
  x = 0
  y = 0
  aim = 0
  for line in _input:
    direction, units = line.split(' ')
    units = int(units)
    
    if direction == 'forward':
      x += units
      y += aim * units
    elif direction == 'down':
      aim += units
    elif direction == "up":
      aim -= units
    
  print(x * y)

part1()
part2()