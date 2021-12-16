import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(16)

hexString = _input[0]

lookup = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111'
}
binary = ""
for char in hexString:
  binary += lookup[char]

def parseLiteralPacket(binary, currentPos):
  total = ""
  while currentPos < len(binary):
    subPacket = binary[currentPos:currentPos+5]

    #its not the end
    if int(subPacket[0]) == 1:
      total += subPacket[1:]
      currentPos += 5
    else:
      total += subPacket[1:]
      currentPos += 5
      break
  return total, currentPos

def parseOperatorPacket(binary, currentPos, type):
  global versionTotal
  numbers = []
  lengthTypeId = int(binary[currentPos])
  currentPos += 1

  if lengthTypeId == 0:
    totalBitsOfSubPackets = binary[currentPos:currentPos+15]
    currentPos = currentPos + 15
    current = 0
    

    while current < int(totalBitsOfSubPackets, 2):
      subVersion, subType, currentPos = getPacketTypeAndVersion(binary, currentPos)
      versionTotal += subVersion
      current += 6
      if subType == 4:
        posBefore = currentPos
        total, currentPos = parseLiteralPacket(binary, currentPos)
        current += (currentPos - posBefore)

        numbers.append(int(total, 2))
      
      else:
        posBefore = currentPos
        currentPos, val = parseOperatorPacket(binary, currentPos, subType)
        numbers.append(val)
        current += (currentPos - posBefore)

  else:
    numberOfSubPackets = int(binary[currentPos:currentPos+11], 2)
    currentPos += 11

    for i in range(numberOfSubPackets):
      subVersion, subType, currentPos = getPacketTypeAndVersion(binary, currentPos)
      versionTotal += subVersion

      if subType == 4:
        total, currentPos = parseLiteralPacket(binary, currentPos)
        numbers.append(int(total, 2))
      
      else:
        currentPos, val = parseOperatorPacket(binary, currentPos, subType)
        numbers.append(val)
  
  val = operate(type, numbers)

  return currentPos, val

def operate(type, numbers):
  if type == 0:
    return sum(numbers)
  elif type == 1:
    res = 1
    for n in numbers:
      res *= n
    return res
  elif type == 2:
    return min(numbers)
  elif type == 3:
    return max(numbers)
  elif type == 5:
    return 1 if numbers[0] > numbers[1]  else 0
  elif type == 6:
    return 1 if numbers[0] < numbers[1] else 0
  elif type == 7:
    return 1 if numbers[0] == numbers[1] else 0

def getPacketTypeAndVersion(binary, currentPos):
  return int(binary[currentPos:currentPos+3], 2), int(binary[currentPos+3: currentPos + 6], 2), currentPos + 6

currentPos = 0
versionTotal = 0
totalValue = []

version, type, currentPos = getPacketTypeAndVersion(binary, currentPos)
versionTotal = version

if type == 4:
  total, currentPos = parseLiteralPacket(binary, currentPos)

else:
  currentPos, val = parseOperatorPacket(binary, currentPos, type)

print(versionTotal)
print(val)
  




  




