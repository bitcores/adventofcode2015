from itertools import combinations

litres = 150
containers = []

with open("input17.txt") as fp:
    cnt = 0
    for line in fp:
        containers.append(int(line.strip()))

print(containers)

hmany = 0
hmlist = []
mincon = 99999
nmin = 0
nlist = []

for x in range(len(containers)):
    allcomb = list(combinations(containers, x+1))

    for y in range(len(allcomb)):
        totalcap = 0
        for z in range(len(allcomb[y])):
            totalcap += allcomb[y][z]
        if totalcap == litres:
            hmany += 1
            hmlist.append(allcomb[y])

for p in range(len(hmlist)):
    if len(hmlist[p]) < mincon:
        mincon = len(hmlist[p])

for q in range(len(hmlist)):
    if len(hmlist[q]) == mincon:
        nmin += 1
        nlist.append(hmlist[q])

#print(hmlist)
print(hmany)
print(nlist)
print(mincon)
print(nmin)