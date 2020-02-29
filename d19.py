import sys
sys.setrecursionlimit(15000)
unimols = set()
repments = []
strtmol = ""

with open("input19.txt") as fp:
    for line in fp:
        x = 0
        line = line.strip()
        if line.find("=>") > 0:
            rep = line.split(" => ")
            repments.append((rep[0], rep[1]))
        elif len(line) != 0:
            strtmol = line

#print(repments)
#print(strtmol)

for x in range(len(repments)):
    pos = 0
    while pos < len(strtmol):
        pos = strtmol.find(repments[x][0], pos)
        if pos == -1:
            break
        newmol = strtmol[:pos] + repments[x][1] + strtmol[pos+len(repments[x][0]):]
        unimols.add(newmol)
        pos = pos + 1

#print(unimols)
print(len(unimols))
