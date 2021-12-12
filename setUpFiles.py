import os

for i in range(1, 26):
  day = i
  if i < 10:
    day = f"0{i}"
  dir_path = os.path.dirname(os.path.realpath(__file__)) + f"\\Day{day}"
  
  if os.path.isdir(dir_path):
    continue
  
  os.mkdir(dir_path)

  with open(f'{dir_path}\\Day{day}.py', 'w') as fp:
    fp.write(f"""import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput({i})
""")
    pass
  
  with open(f'{dir_path}\\Day{day}Input.txt', 'w') as fp:
    pass