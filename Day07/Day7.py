import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(7)
_input = [int(x) for x in _input[0].split(',')]

totalGasToMoveTo = defaultdict(int)

for i in range(max(_input)):
  total = 0
  for j, val2 in enumerate(_input):    
    gasToMove = abs(i - val2)
    total += (gasToMove * (gasToMove + 1)) // 2
    #total += gasToMove
  
  totalGasToMoveTo[i] = total 

print(min([val for x, val in totalGasToMoveTo.items()]))