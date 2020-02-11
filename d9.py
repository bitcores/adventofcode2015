import copy
from itertools import permutations

allset = set()
loca = {}

with open("input9.txt") as fp:
    cnt = 0
    for line in fp:
        roudis = line.split(" = ")
        rou = roudis[0].split(" to ")
        if not rou[0] in loca:
            loca[rou[0]] = {}
        if not rou[1] in loca:
            loca[rou[1]] = {}
        loca[rou[0]][rou[1]] = int(roudis[1])
        loca[rou[1]][rou[0]] = int(roudis[1])
        allset.add(rou[0])
        allset.add(rou[1])

alldest = list(permutations(allset))
mindist = 0
minpath = ""

for x in range(len(alldest)):
    dist = 0
    path = ""
    for y in range(len(alldest[x])-1):
        dist += loca[alldest[x][y]][alldest[x][y+1]]
        path = path + alldest[x][y] + " -> " + alldest[x][y+1] + ", " + str(dist) + ". "
    if dist > mindist: 
        mindist = dist
        minpath = path

print(mindist)
print(minpath)

