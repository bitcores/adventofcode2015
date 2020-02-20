import json
import re

#dinp = '{"a":2,"b":4}'
f = open("input12.txt", "r")
dinp = f.read()
f.close()

def reit(itin):
    global ctotal
    global rejsn

    for y in itin:      
        if isinstance(y, dict):
            nored = True

            for i, t in y.items():
                if t == "red":
                    del y
                    nored = False
                    break

            if nored:
                print(y)
                input()
                for i, t in y.items():
                    
                    if (isinstance(t, dict) or isinstance(t, list)):
                        reit(t)
                    else:
                        if isinstance(t, int):
                            ctotal += int(t)


jsnned = json.loads(dinp)
rejsn = ""
ctotal = 0
reit(jsnned)

pos = 0
bpos = 0
spos = 0
ebpos = 0
nbpos = 0
ninp = ""

while pos < len(dinp):
    pos = dinp.find("red", pos)
    if pos == -1:
        break
    #print(pos)
    nbpos = dinp.find("}", pos)
    nspos = dinp.find("]", pos)
    
    #print(bpos, spos)
    if nbpos < nspos:
        bpos = dinp[:nbpos].rfind("{")
        nnpos = dinp[:nbpos].rfind("}")
        if nnpos > bpos:
            bpos = dinp[:bpos].rfind("{")

        ninp += dinp[bpos:nbpos+1]
        #print(dinp[bpos:nbpos+1])
        pos = nbpos
        #input()

    pos += +1

#print(dinp)
#print(ninp)

tmp = re.findall(r'-?\d+', dinp)
numbers = list(map(int, tmp))

total = 0
for x in range(len(numbers)):
    total += numbers[x]

tmp2 = re.findall(r'-?\d+', ninp)
numbers2 = list(map(int, tmp2))

total2 = 0
for x in range(len(numbers2)):
    total2 += numbers2[x]

tmp3 = re.findall(r'-?\d+', rejsn)
numbers3 = list(map(int, tmp3))

total3 = 0
for x in range(len(numbers3)):
    total3 += numbers3[x]

print(total)
print(total2)
print(total - total2)
print(total3)
print(ctotal)