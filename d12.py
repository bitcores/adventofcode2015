import json
import re

#dinp = '{"a":2,"b":4}'
f = open("input12.txt", "r")
dinp = f.read()
f.close()

def reit(itin):
    global ctotal
    global rejsn
    #print(itin)
    #input()

    if isinstance(itin, list):
        for y in itin:  
            if isinstance(y, list) or isinstance(y, dict):
                reit(y)
            
            if isinstance(y, int):
                #print(t)
                #input()
                ctotal += int(y)

    if isinstance(itin, dict):
        nored = True
        for i, t in itin.items():
            if t == "red":
                nored = False
                return

        if nored:
            for i, t in itin.items():
                if isinstance(t, int):
                    #print(t)
                    #input()
                    ctotal += int(t)
                if (isinstance(t, dict) or isinstance(t, list)):
                    reit(t)


jsnned = json.loads(dinp)
rejsn = ""
ctotal = 0
reit(jsnned)

tmp = re.findall(r'-?\d+', dinp)
numbers = list(map(int, tmp))

total = 0
for x in range(len(numbers)):
    total += numbers[x]

print(total)
print("json ", ctotal)