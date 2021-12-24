import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(22)


def parse():
  commands = list()
  for line in _input:
    splitLine = line.split(',')
    command, xLine = splitLine[0].split()

    xStart, xEnd = xLine.split('=')[1].split("..")
    yStart, yEnd = splitLine[1].split('=')[1].split("..")
    zStart, zEnd = splitLine[2].split('=')[1].split('..')

    commands.append((command, (int(xStart), int(xEnd)), (int(yStart), int(yEnd)), (int(zStart), int(zEnd))))

  return commands

def part1(commands):
  cubes = set()
  #comment out the huge lines 
  for command in commands:
    on = command[0] == 'on'

    (xStart, xEnd) = command[1]
    (yStart, yEnd) = command[2]
    (zStart, zEnd) = command[3]
    
    for x in range(int(xStart), int(xEnd) + 1):
      for y in range(int(yStart), int(yEnd) + 1):
        for z in range(int(zStart), int(zEnd) + 1):
          if (x,y,z) in cubes and not on:
            cubes.remove((x,y,z))
          elif on:
            cubes.add((x,y,z))
      


  print(len(cubes))

def part2(commands):
  onCount = 0
  cubes = []
  for command in commands:
    on = command[0] == 'on'

    (xStart, xEnd) = command[1]
    (yStart, yEnd) = command[2]
    (zStart, zEnd) = command[3]
    xEnd += 1
    yEnd += 1
    zEnd += 1

    
    

  print(onCount)
  return

def newPart2():
  data = [] #this will be our list of cubes
  for line in _input:
    items = line.split(' ')
    if items[0] == 'on':
      value = 1
    else:
      value = 0
    ranges = [x[2:] for x in items[1].split(',')]
    x_start,x_end = [int(x) for x in ranges[0].split("..")]
    y_start,y_end = [int(x) for x in ranges[1].split("..")]
    z_start,z_end = [int(x) for x in ranges[2].split("..")]
    #it's easier to do inclusive start indices and exclusive end indices,
    #at least for me.  You could do it either way.
    x_end+=1
    y_end+=1
    z_end+=1
    #a cube is a 7-tuple (actually a list so we can modify it), as follows:
    cube = [x_start,x_end,y_start,y_end,z_start,z_end,value]
    #we'll put all the new cubes into this list
    new_items = []
    for i in range(len(data)):
      #loop through all the existing cubes and check whether they intersect.
      #I originally made this an index-loop because i was going to `del`
      #the indices from the list, but then I decided it was simpler to just make
      #a new one each loop
      item = data[i]
      
      #in order to intersect, we must overlap in x, y and z
      x_overlap = x_end > item[0] and x_start < item[1]
      y_overlap = y_end > item[2] and y_start < item[3]
      z_overlap = z_end > item[4] and z_start < item[5]
      if x_overlap and y_overlap and z_overlap:
        
        #now we check for each of the possible 'left-over' slices,
        #left, right, up, down, front back
        if item[0] < x_start:
          #if the left edge of this cube is to the left of the new one, 
          #then it's going to have a left-over slice on the left side.
          #this left-over slice is everything to the left of the new cube
          #so its x_end value will be the *x_start* of the new cube
          new_item = [item[0],x_start,item[2],item[3],item[4],item[5],item[6]]
          #we've already accounted for everything to the left of here, so remove it
          #from the cube to avoid double counting
          item[0] = x_start
          #add the slice to our new list
          new_items.append(new_item)
        #repeat for the five other directions, all the exact same idea
        if item[1] > x_end:
          new_item = [x_end,item[1],item[2],item[3],item[4],item[5],item[6]]
          item[1] = x_end
          new_items.append(new_item)
        if item[2] < y_start:
          new_item = [item[0],item[1],item[2],y_start,item[4],item[5],item[6]]
          item[2] = y_start
          new_items.append(new_item)        
        if item[3] > y_end:
          new_item = [item[0],item[1],y_end,item[3],item[4],item[5],item[6]]
          item[3] = y_end
          new_items.append(new_item) 
        if item[4] < z_start:
          new_item = [item[0],item[1],item[2],item[3],item[4],z_start,item[6]]
          item[4] = z_start
          new_items.append(new_item)        
        if item[5] > z_end:
          new_item = [item[0],item[1],item[2],item[3],z_end,item[5],item[6]]
          item[5] = z_end
          new_items.append(new_item)
      else:
        #if we didn't intersect at all, just keep the cube
        new_items.append(item)
    
    #add our new one
    new_items.append(cube)
    #update the list for the next pass
    data = new_items
 
  #sum up the total number of cells that are on
  total = 0
  for i in range(len(data)): #I don't know why this is index-based
    item = data[i]
    if item[6]==1: #only count cells that are on!
      #add the total area of the cube
      total+=(item[1]-item[0])*(item[3]-item[2])*(item[5]-item[4])
 
  print(total)

commands = parse()
#part1(commands)
newPart2()