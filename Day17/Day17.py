import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(17)

target = _input[0] #target area: x=277..318, y=-92..-53

target = target.split("target area: ")[1].split(",")

minX, maxX = target[0].split('=')[1].split('..')
minY, maxY = target[1].split('=')[1].split('..')

minX = int(minX)
maxX = int(maxX)
minY = int(minY)
maxY = int(maxY)

targetCoords = set()

for x in range(minX, maxX+1, 1):
  for y in range(minY, maxY+1, 1):
    targetCoords.add((x,y))
    

def step(x, y, xVelocity, yVelocity):
  x += xVelocity
  y += yVelocity

  if xVelocity > 0:
    xVelocity -= 1
  elif xVelocity < 0:
    xVelocity += 1
    
  yVelocity -= 1

  return x, y, xVelocity, yVelocity

start = (0,0)
hits = []
initalVelocities = set()

for xVelocity in range(1, 400, 1):
  for yVelocity in range(-150, 100, 1):
    xVel = xVelocity
    yVel = yVelocity
    highestY = 0

    (x, y) = start
    while x <= maxX and y >= minY:
      x, y, xVel, yVel = step(x, y, xVel, yVel)

      if y > highestY:
        highestY = y

      if (x,y) in targetCoords:
        #print(f"Hit at ({x},{y})!, Highest Y: {highestY}, Starting Velocity: ({xVelocity, yVelocity})")
        hits.append(((x,y), highestY))
        initalVelocities.add((xVelocity, yVelocity))
        break

print(max([x[1] for x in hits]))
print(len(initalVelocities))
