import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(20)

imageEnhancer = [c for c in _input[0]]
inputImage = []

for line in _input[2:]:
  temp = []
  for c in line:
    temp.append(c)
  inputImage.append(temp)

DR = [-1, 0, 1]
DC = [-1, 0, 1]

def findLights(R, C, image):
  light = set()
  for row in range(R):
    for col in range(C):
      if image[row][col] == '#':
        light.add((row,col))
  
  return light

def enhance(image, flicker):
  R = len(image)
  C = len(image[0])

  light = findLights(R,C, image)
  newLight = set()
  newImage = []
  
  for row in range(-1, R+1):
    temp = []
    for col in range(-1, C+1):
      pixelBinary = ''
      for dr in DR:
        for dc in DC:
          newR = row + dr
          newC = col + dc
          
          if (newR < 0 or newR >= R) or (newC >= C or newC < 0):
            pixelBinary += ('0' if flicker % 2 == 0 else '1')
          else:
            if (newR, newC) in light:
              pixelBinary += '1'
            else:
              pixelBinary += '0'
        
      binary = int(pixelBinary, 2)

      imageEnhancerPixel = imageEnhancer[binary]
      temp.append(imageEnhancerPixel)

      if imageEnhancerPixel == '#':
        newLight.add((row,col))
    
    newImage.append(temp)
  return newImage, newLight

image = deepcopy(inputImage)
for i in range(2):
  newImage, newLight = enhance(image, i)
  image = newImage

print(len(newLight))

image = deepcopy(inputImage)
for i in range(50):
  newImage, newLight = enhance(image, i)
  image = newImage

print(len(newLight))