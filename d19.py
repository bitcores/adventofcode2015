from random import shuffle

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

# found a solution on reddit
cnt = 0
emol = strtmol

while emol != "e":
    tmp = emol
    for a, b in repments:
        if b not in emol:
            continue
        
        emol = emol.replace(b, a, 1)
        cnt += 1

    if tmp == emol:
        emol = strtmol
        cnt = 0
        # this shuffle thing was what i was missing, changing the order replacements were
        # checked to find a replacement path through. but it seems to me that it wouldn't
        # be guaranteed to work and is more of a hack solution than some others
        shuffle(repments)

print(cnt)


