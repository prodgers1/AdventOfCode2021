import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(12)

paths = defaultdict(list)

for line in _input:
  start, end = line.split('-')
  paths[start].append(end)
  paths[end].append(start)

def part1Walk(currentNode, pathsChecked, currentPath, smallCavesVisited):
  if currentNode == "end":
    currentPath.append(currentNode)
    pathsChecked.append(deepcopy(currentPath))
    currentPath.pop()
    return
  
  if currentNode.islower() and currentNode != "end":
    smallCavesVisited.add(currentNode)

  nextNodes = paths[currentNode]
  currentPath.append(currentNode)

  for node in nextNodes:
    if node == "end":
      part1Walk(node, pathsChecked, currentPath, deepcopy(smallCavesVisited))

    elif node.islower() and node not in smallCavesVisited:
      part1Walk(node, pathsChecked, currentPath, deepcopy(smallCavesVisited))
    
    elif not node.islower():
      part1Walk(node, pathsChecked, currentPath, deepcopy(smallCavesVisited))

  currentPath.pop()
  return currentPath

def part2Walk(currentNode, pathsChecked, currentPath, smallCavesVisited, hasDupes):
  if currentNode == "end":
    currentPath.append(currentNode)
    pathsChecked.append(deepcopy(currentPath))
    currentPath.pop()
    return
  
  if currentNode.islower() and currentNode != "end":
    smallCavesVisited.add(currentNode)

  nextNodes = paths[currentNode]
  currentPath.append(currentNode)

  for node in nextNodes:
    if node == "end":
      part2Walk(node, pathsChecked, currentPath, deepcopy(smallCavesVisited), hasDupes)

    elif node.islower() and node not in smallCavesVisited:
      part2Walk(node, pathsChecked, currentPath, deepcopy(smallCavesVisited), hasDupes)
    
    elif node.islower() and not hasDupes and (node != "start" and node != "end"):
      part2Walk(node, pathsChecked, currentPath, deepcopy(smallCavesVisited), True)

    elif not node.islower():
      part2Walk(node, pathsChecked, currentPath, deepcopy(smallCavesVisited), hasDupes)

  currentPath.pop()
  return currentPath

pathsChecked = []
part1Walk("start", pathsChecked, [], set())
print(len(pathsChecked))

pathsChecked = []
part2Walk("start", pathsChecked, [], set(), False)
print(len(pathsChecked))