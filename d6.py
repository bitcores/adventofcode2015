
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
                        
                

setlights([0,0], [999,999], 0)

with open("input6.txt") as fp:
    for line in fp:
        inst = line.split(" ")
        if len(inst) == 5:
            s = inst[2].split(",")
            e = inst[4].split(",")
            if inst[1] == "on":
                #print("turn on")
                m = 1
            else:
                #print("turn off")
                m = 0
        else:
            #print("toggle")
            s = inst[1].split(",")
            e = inst[3].split(",")
            m = 2
        #print(s, e)
        setlights(s, e, m)

lightsum = 0
for y in range(0, 1000):
    lightsum += sum(value for value in lightgrid[y].values())

#print(lightgrid[2])
#print(sum(value for value in lightgrid[2].values()))
print(lightsum)