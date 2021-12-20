import sys
import math
import json
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(19)

scanners = {}
totalMap = defaultdict(list)

scannerNum = None

for line in _input:
  if "scanner" in line:
    scannerNum = line.split(" ")[2]
    scanners[scannerNum] = []
  elif line == "":
    scannerNum = None

  elif scannerNum != None and (line[0].isdigit() or line[0] == '-'):
    x, y, z = line.split(',')
    scanners[scannerNum].append((int(x),int(y),int(z)))

def createBeaconMap(scannerNum):
  beaconMap = {}
  beacons = scanners[scannerNum]
  #every beacon gets a turn to be (0,0). We want to calculate the distance of every beacon from that point
  # because there will exist a mapping between scanners that have the same distances between beacons
  for i in range(len(beacons)):
    x, y, z = beacons[i]
    beaconMap[(x,y,z)] = []
    for j in range(len(beacons)):
      if i == j:
        continue
      dx, dy, dz = beacons[j]

      beaconMap[(x,y,z)].append((dx-x, dy-y, dz-z))

  return beaconMap



def compareBeaconMaps(beaconMap1, beaconMap2):
  score = {}
  for key, value in beaconMap1.items():
    for key2, value2 in beaconMap2.items():
      
      match = 0   
      temp= []
      for i in value:
        x1, y1, z1 = i
        l = sorted([abs(x1), abs(y1), abs(z1)])
        for j in value2:
          x2, y2, z2 = j
          l1 = sorted([abs(x2), abs(y2), abs(z2)])
          if l == l1:
            match += 1
            temp.append(((x1,y1,z1), (x2,y2,z2)))
      
      if match > 1:
        score[((key), (key2))] = temp
      
    
  return score

def getOrientation(score):
  for k, v in score.items():
    x1, y1, z1 = v[0][0]
    x2, y2, z2 = v[0][1]
    orientation = []

    if x1 == x2:
      orientation.append(1)
    else:
      orientation.append(-1)
    
    if y1 == y2:
      orientation.append(1)
    else:
      orientation.append(-1)

    if z1 == z2:
      orientation.append(1)
    else:
      orientation.append(-1)


    return orientation

def findOffset(beacons, orientation):
  x1, y1, z1 = beacons[0]
  x2, y2, z2 = beacons[1]
  
  x2 = (x2 * orientation[0])
  y2 = (y2 * orientation[1]) 
  z2 = (z2 * orientation[2])

  dx = (x1 - x2)
  dy = (y1 - y2)
  dz = (z1 - z2)
  
  return (dx, dy, dz)

def translatePoints(point, offsets, orientation):
  x, y, z = point
  dx, dy, dz = 0, 0, 0

  #dx = x - offsets[0]
  #dy = y - offsets[1]
  #dz = z - offsets[2]

  if orientation[0] < 0:
    dx = x - offsets[0]
  else:
    dx = x + offsets[0]
    dx *= -1
    dx = -dx * orientation[0]
    
  
  if orientation[1] < 0:
    dy = y - offsets[1]
    
  else:
    dy = y + offsets[1]
    dy *= -1 
    dy = -dy * orientation[1]
    
  
  if orientation[2] < 0:
    dz = z - offsets[2] 
  else:
    dz = dz + offsets[2]
    dz *= -1
    dz = -dz * orientation[2]
  
  return (dx * orientation[0], dy * orientation[1], dz * orientation[2])

ans = []

maps = {}

for scannerNum, _ in scanners.items():
  beaconMap = createBeaconMap(scannerNum)
  maps[scannerNum] = beaconMap

#for some reason scanner 0 and 4 don't map together when they should.

for scannerNum, beacons in scanners.items():
  #firstScannerBeaconMap = createBeaconMap(scannerNum)
  firstScannerBeaconMap = maps[scannerNum]
  print(f"Scanner {scannerNum} / {len(scanners)}")
  score = 0
  for scannerNum2, beacons2 in scanners.items():
    if scannerNum == scannerNum2 or scannerNum2 == 0:
      continue
    #secondScannerBeaconMap = createBeaconMap(scannerNum2)
    secondScannerBeaconMap = maps[scannerNum2]
    matchingBeacons = compareBeaconMaps(firstScannerBeaconMap, secondScannerBeaconMap)
    score += len(matchingBeacons)
    #for b in beacons:
    # print(b)
    #print("------")
    
    #this isnt right, but idk what to do
    if score >= 12 and matchingBeacons:
      orientation = getOrientation(matchingBeacons)
      for k, v in matchingBeacons.items():
        offsets = findOffset(k, orientation)
        break
        #offset then orientate
      for i in range(len(beacons2)):
        point = beacons2[i]
        newX, newY, newZ = translatePoints(point, offsets, orientation)
        #print((newX, newY, newZ))
        if (newX, newY, newZ) not in ans:
          ans.append((newX, newY, newZ))
        #print((newX, newY, newZ))
      
      #break
        
for a in ans:
  print(a)
print(len(ans))
    

