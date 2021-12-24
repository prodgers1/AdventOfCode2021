import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(24)

#ANSWER:
#part 1: 93997999296912
#part 2: 81111379141811
#

#find when the z value is dropping by a large chunk, then look for the pattern in the number

#start = 93997999296912
start = 99999999999999
deduct = 1
minSoFar = 9999999999999
while True:
  variables = defaultdict(int)
  
  if '0' in str(start):
    start -= deduct
    continue
  print(f"Checking: {start}")

  currentIndex = 0
  invalid = False

  for line in _input:
    if "inp" in line:
      command, a = line.split()
      startStr = str(start)
      nextNum = startStr[currentIndex]
      #nextNum = start
      currentIndex += 1

      variables[a] = int(nextNum)
      

    elif "add" in line:
      command, a, b = line.split()
      if a.isdigit():
        val1 = int(a)
      else:
        val1 = int(variables[a])
      
      if b.lstrip('-').isdigit():
        val2 = int(b)
      else:
        val2 = int(variables[b])
      variables[a] = val1 + val2
    
    elif "mul" in line:
      command, a, b = line.split()
      if a.isdigit():
        val1 = int(a)
      else:
        val1 = int(variables[a])
      
      if b.lstrip('-').isdigit():
        val2 = int(b)
      else:
        val2 = int(variables[b])
      variables[a] = val1 * val2
    elif "div" in line:
      command, a, b = line.split()
      if a.isdigit():
        val1 = int(a)
      else:
        val1 = int(variables[a])
      
      if b.lstrip('-').isdigit():
        val2 = int(b)
      else:
        val2 = int(variables[b])

      if val2 == 0:
        invalid = True
        break
        

      variables[a] = val1 // val2
    
    elif "mod" in line:
      command, a, b = line.split()

      if a.isdigit():
        val1 = int(a)
      else:
        val1 = int(variables[a])
      
      if b.lstrip('-').isdigit():
        val2 = int(b)
      else:
        val2 = int(variables[b])

      if val1 < 0 or val2 <= 0:
        invalid = True
        break
      
      variables[a] = val1 % val2
    
    elif "eql" in line:
      command, a, b = line.split()
      if a.isdigit():
        val1 = int(a)
      else:
        val1 = int(variables[a])
      
      if b.lstrip('-').isdigit():
        val2 = int(b)
      else:
        val2 = int(variables[b])

      if val1 == val2:
        variables[a] = 1
      else:
        variables[a] = 0
  
  #print(variables['z'])

  if variables['z'] < minSoFar:
    minSoFar = variables['z']

  if len(str(variables['z'])) < 4:
    asddf = 3

  if variables['y'] == 0 and variables['x'] == 0:
    print(start)

  if variables['z'] == 0:
    print(f"FOUND! {start}")
    break
  
  start -= deduct
  

