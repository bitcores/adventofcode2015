import copy
from itertools import permutations

allset = set()
persons = {}

with open("input13.txt") as fp:
    cnt = 0
    for line in fp:
        roudis = line.split(" ")
        if not roudis[0] in persons:
            persons[roudis[0]] = {}
        m = int(roudis[3])
        if roudis[2] == "lose":
            m = m*-1
        nper = roudis[10].strip()[:-1]
        persons[roudis[0]][nper] = m
        allset.add(roudis[0])

print(persons)

allpos = list(permutations(allset))
# for part b change to 0
maxhappy = -99999

for x in range(len(allpos)):
    happy = 0
    link = ""

    for y in range(len(allpos[x])-1):
        happy += persons[allpos[x][y]][allpos[x][y+1]]
        happy += persons[allpos[x][y+1]][allpos[x][y]]
        link = link + allpos[x][y] + "->" + allpos[x][y+1] + ", " + str(persons[allpos[x][y]][allpos[x][y+1]]) + "."
    
    happy += persons[allpos[x][0]][allpos[x][len(allpos[x])-1]]
    happy += persons[allpos[x][len(allpos[x])-1]][allpos[x][0]]

    print(link)
    print(happy)
    if happy > maxhappy:
        maxhappy = happy

print(maxhappy)