import copy

def iname(co, n):
    name = chr(65+co) + str(n)
    return name

pos = [0,0]
pos2 = [0,0]
reclist = {}

# ^ north y+1
# v south y-1
# < west x-1
# > east x+1

f = open("input3.txt", "r")
dinp = f.read()
f.close()

reclist[iname(pos[0],pos[1])] = 2

for e in range(0, len(dinp), 2):
    if dinp[e] == "^":
        pos[1] = pos[1]+1
    if dinp[e] == "v":
        pos[1] = pos[1]-1
    if dinp[e] == "<":
        pos[0] = pos[0]-1
    if dinp[e] == ">":
        pos[0] = pos[0]+1

    if dinp[e+1] == "^":
        pos2[1] = pos2[1]+1
    if dinp[e+1] == "v":
        pos2[1] = pos2[1]-1
    if dinp[e+1] == "<":
        pos2[0] = pos2[0]-1
    if dinp[e+1] == ">":
        pos2[0] = pos2[0]+1
    
    if iname(pos[0],pos[1]) in reclist:
        reclist[iname(pos[0],pos[1])] = reclist[iname(pos[0],pos[1])]+1
    else:
        reclist[iname(pos[0],pos[1])] = 1
    
    if iname(pos2[0],pos2[1]) in reclist:
        reclist[iname(pos2[0],pos2[1])] = reclist[iname(pos2[0],pos2[1])]+1
    else:
        reclist[iname(pos2[0],pos2[1])] = 1

print(len(reclist))
