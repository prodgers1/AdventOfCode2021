def main():
    filehandle = open("./Day24/Day24Input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())

    assert [9,9,9,9,9,9,9,9,9,9,9,9,9,9] == [9] * 14

    codeVars, exploderIndex = parse(lines)
    print(runALU(codeVars, exploderIndex, [9]*14, False))
    print(runALU(codeVars, exploderIndex, [1]*14, True))

def parse(lines):
    variablesMap = []
    exploderIndex = []
    ind = 0
    for i in range(0,len(lines),18):
        if 'inp' in lines[i]:
            zDivider = int(lines[i+4].split(' ')[-1])
            xAdder = int(lines[i+5].split(' ')[-1])
            yAdder = int(lines[i+15].split(' ')[-1])
            chunkMap = {'zDivider': zDivider, 'xAdder': xAdder, 'yAdder': yAdder}
            variablesMap.append(chunkMap)
            if zDivider == 1:
                exploderIndex.append(ind)
            ind += 1
    return variablesMap, exploderIndex

def runALU(codeVars, exploderIndex, number, part2):
    zValMAp = {-1:0}
    i = 0
    z = 0
    while True:
        
        if i >= 14:
            if z == 0:
                num = ''.join(map(str,number))
                return num
            i = rollbackNum(i, number, exploderIndex, part2)
            if i == -1:
                    break
            z = zValMAp[i]

        if i in exploderIndex:
            z = runCode(number[i], z, **codeVars[i])
            zValMAp[i] = z
            i += 1
        else:
            tumblerVal, z = reduce(i,z,codeVars)
            if tumblerVal != -1:
                number[i] = tumblerVal
                zValMAp[i] = z
                i += 1
            else:
                i = rollbackNum(i, number, exploderIndex, part2)
                if i == -1:
                    break

                z = zValMAp[i-1]
        

def rollbackNum(i, number, exploderIndex, part2):
    if part2:
        return rollbackNumUp(i, number, exploderIndex)
    else:
        return rollbackNumDown(i, number, exploderIndex)

def rollbackNumDown(i, number, exploderIndex):
    while i not in exploderIndex:
        i -= 1

    if number[i] == 1:
        if i == 0:
            return -1
        number[i] = 9
        return rollbackNumDown(i-1, number, exploderIndex)
    else:
        number[i] -= 1
        return i

def rollbackNumUp(i, number, exploderIndex):
    while i not in exploderIndex:
        i -= 1

    if number[i] == 9:
        if i == 0:
            return -1
        number[i] = 1
        return rollbackNumUp(i-1, number, exploderIndex)
    else:
        number[i] += 1
        return i

def reduce(i, z, codeVars):

    for j in range(1,10):
        newZ = runCode(j,z,**codeVars[i])
        if newZ == z//26:
            return j, newZ
    
    return -1, 1e9

def runCode(inp, inpz, zDivider, xAdder, yAdder):
    w,x,y,z = inp,0,0,inpz

    x *= 0
    x += z
    x = x % 26
    z = z//zDivider
    x += xAdder
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
    y += yAdder
    y *= x
    z += y

    return z

main()