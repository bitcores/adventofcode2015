import copy

# turn on = True
# turn off = False
# toggle = not value
lightgrid = {}

def setlights(s, e, m):
    for y in range(int(s[1]), int(e[1])+1):
        if not y in lightgrid:
            lightgrid[y] = {}
        for x in range(int(s[0]), int(e[0])+1):
            if m == 2:
                lightgrid[y][x] = lightgrid[y][x] + 2
            elif m == 1:
                lightgrid[y][x] = lightgrid[y][x] + 1
            elif m == 0:
                if not x in lightgrid[y]:
                    lightgrid[y][x] = 0
                else:
                    lightgrid[y][x] = lightgrid[y][x] - 1

                    if lightgrid[y][x] < 0:
                        lightgrid[y][x] = 0 
                        
def countrlights(x,y):
    oncount = 0
    for p in range(y-1, y+2):
        for r in range(x-1, x+2):
            if lightgrid[p][r] == 1:
                if p == y and r == x:
                    oncount = oncount
                else:
                    oncount += 1
    return oncount

                

setlights([-1,-1], [100,100], 0)

y = 0

with open("input18.txt") as fp:
    for line in fp:
        x = 0
        for z in line:
            if z == "#":
                lightgrid[y][x] = 1
            if z == ".":
                lightgrid[y][x] = 0
            x += 1

        y += 1

y = 0
x = 0
lightgrid[0][0] = 1
lightgrid[0][99] = 1
lightgrid[99][0] = 1
lightgrid[99][99] = 1

for i in range(0,100):
    workgrid = copy.deepcopy(lightgrid)
    for y in range(0,100):
        for x in range(0,100):
            if lightgrid[y][x] == 0 and countrlights(x,y) == 3:
                workgrid[y][x] = 1
                #print(y,x,"toggle1")
            elif lightgrid[y][x] == 1:
                if countrlights(x,y) == 2 or countrlights(x,y) == 3:
                    workgrid[y][x] = 1
                else:
                    workgrid[y][x] = 0
                #print(y,x,"toggle2")

    lightgrid = copy.deepcopy(workgrid)
    lightgrid[0][0] = 1
    lightgrid[0][99] = 1
    lightgrid[99][0] = 1
    lightgrid[99][99] = 1

#print(lightgrid)

onlights = 0
for y in range(0,100):
    for x in range(0,100):
        if lightgrid[y][x] == 1:
            onlights += 1

print(onlights)