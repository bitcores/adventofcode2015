from itertools import combinations_with_replacement

ingred = {}
ingredset = set()

with open("input15.txt") as fp:
    cnt = 0
    for line in fp:
        roudis = line.split(" ")
        if not roudis[0] in ingred:
            ingred[roudis[0]] = {}
        ingred[roudis[0]]["cap"] = int(roudis[2][:-1])
        ingred[roudis[0]]["dur"] = int(roudis[4][:-1])
        ingred[roudis[0]]["fla"] = int(roudis[6][:-1])
        ingred[roudis[0]]["tex"] = int(roudis[8][:-1])
        ingred[roudis[0]]["cal"] = int(roudis[10].strip())
        ingredset.add(roudis[0])

print(ingred)

comb = list(combinations_with_replacement(ingredset, 100))

hiscore = 0

for x in range(len(comb)):
    nutri = {}
    nutri["cap"] = 0
    nutri["dur"] = 0
    nutri["fla"] = 0
    nutri["tex"] = 0
    cals = 0
    score = 1
    for y in range(len(comb[x])):
        # add all the values together
        #print(comb[x][y])
        nutri["cap"] = nutri["cap"] + ingred[comb[x][y]]["cap"]
        nutri["dur"] = nutri["dur"] + ingred[comb[x][y]]["dur"]
        nutri["fla"] = nutri["fla"] + ingred[comb[x][y]]["fla"]
        nutri["tex"] = nutri["tex"] + ingred[comb[x][y]]["tex"]
        cals = cals + ingred[comb[x][y]]["cal"]
    
    if cals == 500:
        for p in nutri:
            if nutri[p] <= 0:
                score = 0
                break
            else:
                score = score * nutri[p]
    
    if score > hiscore:
        hiscore = score

print(hiscore)