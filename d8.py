import json

totalcode = 0
totalmem = 0

with open("input8.txt") as fp:
    for line in fp:
        line = line.strip()
        #tr = line[1:-1]
        tr = bytes(line,"utf-8").encode("unicode_escape")
        #tr = json.dumps(line)

        l = len(line)
        m = len(tr)
        #print(line)
        print(tr)
        totalcode += l
        totalmem += m

print(totalcode, totalmem)
print(totalcode - totalmem)
