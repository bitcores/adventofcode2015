from collections import defaultdict

dictsue = {}
sueset = set()

mfcsam = {}
mfcsam["children:"] = 3
mfcsam["cats:"] = 7
mfcsam["samoyeds:"] = 2
mfcsam["pomeranians:"] = 3
mfcsam["akitas:"] = 0
mfcsam["vizslas:"] = 0
mfcsam["goldfish:"] = 5
mfcsam["trees:"] = 3
mfcsam["cars:"] = 2
mfcsam["perfumes:"] = 1

with open("input16.txt") as fp:
    cnt = 0
    for line in fp:
        roudis = line.split(" ")
        if not roudis[1] in dictsue:
            dictsue[roudis[1]] = defaultdict(lambda: 0)
        dictsue[roudis[1]][roudis[2]] = int(roudis[3][:-1])
        dictsue[roudis[1]][roudis[4]] = int(roudis[5][:-1])
        dictsue[roudis[1]][roudis[6]] = int(roudis[7].strip())

        sueset.add(roudis[0])

#print(dictsue["500:"])

for x in dictsue:
    matches = 0
    for y in dictsue[x]:
        if y == "cats:" or y == "trees:":
            if dictsue[x][y] > mfcsam[y]:
                matches += 1
        elif y == "pomeranians:" or y == "goldfish:":
            if dictsue[x][y] < mfcsam[y]:
                matches += 1
        elif dictsue[x][y] == mfcsam[y]:
            matches += 1
    
    if matches >= 3:
        print(x)