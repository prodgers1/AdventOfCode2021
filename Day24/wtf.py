def firstChunk(w,x,y,z):
  x *= 0
  x += z
  x = x % 26
  z = z // 1
  x += 10
  if x == w:
    x = 1
  else:
    x = 0
  if x == 0:
    x = 1
  else:
    x = 0
  y *= 0
  y += 25
  y *= x
  y += 1
  z *= y
  y *= 0
  y += w
  y += 2
  y *= x
  z += y
  return w,x,y,z

def secondChunk(w,x,y,z):
  x *= 0
  x += z
  x = x % 26
  z = z // 1
  x += 14
  if x == w:
    x = 1
  else:
    x = 0
  if x == 0:
    x = 1
  else:
    x = 0
  
  y *= 0
  y += 25
  y *= x
  y += 1
  z *= y
  y *= 0
  y += w
  y += 13
  y *= x
  z += y
  return w,x,y,z


def thirdChunk(w,x,y,z):
  x *= 0
  x += z
  x = x % 26
  z = z // 1
  x += 14
  if x == w:
    x = 1
  else:
    x = 0
  if x == 0:
    x = 1
  else:
    x = 0
  y *= 0
  y += 25
  y *= x
  y += 1
  z *= y
  y *= 0
  y += w
  y += 13
  y *= x
  z += y

  return w,x,y,z


def fourthChunk(w,x,y,z):
  x *= 0
  x += z
  x = x % 26
  z = z // 26
  x = x + (-13)
  if x == w:
    x = 1
  else:
    x = 0
  
  if x == 0:
    x = 1
  else:
    x = 0
  y *= 0
  y += 25
  y *= x
  y += 1
  z *= y
  y *= 0
  y += w
  y += 9
  y *= x
  z += y

  return w,x,y,z


for i in range(1, 10):
  w,x,y,z = firstChunk(i,0,0,0)
  print(w,x,y,z)
  for j in range(1,10):
    w,x,y,z = secondChunk(j,x,y,z)
    print(w,x,y,z)
    for k in range(1,10):
      w,x,y,z = thirdChunk(i,x,y,z)
      print(k,x,y,z)
      for l in range(1,10):
        w,x,y,z = fourthChunk(l,x,y,z)
        print(w,x,y,z)
