import operator

allset = set()
deer = {}
race = {}
lrace = {}

runtime = 2503

with open("input14.txt") as fp:
    cnt = 0
    for line in fp:
        roudis = line.split(" ")
        if not roudis[0] in deer:
            deer[roudis[0]] = {}
        if not roudis[0] in race:
            race[roudis[0]] = {}
            lrace[roudis[0]] = 0
        race[roudis[0]]["rst"] = 0
        race[roudis[0]]["pts"] = 0
        m = int(roudis[3])
        deer[roudis[0]]["sp"] = m
        t = int(roudis[6])
        deer[roudis[0]]["tm"] = t
        r = int(roudis[13])
        deer[roudis[0]]["rs"] = r
        race[roudis[0]]["mvt"] = t
        allset.add(roudis[0])


for i in range(0, runtime):
    for d in race:
        if race[d]["rst"] > 0:
            race[d]["rst"] = race[d]["rst"] - 1
            if race[d]["rst"] == 0:
                race[d]["mvt"] = deer[d]["tm"]     
        elif race[d]["mvt"] > 0:
            lrace[d] = lrace[d] + deer[d]["sp"]
            race[d]["mvt"] = race[d]["mvt"] - 1
            if race[d]["mvt"] == 0:
                race[d]["rst"] = deer[d]["rs"]
    # sort race by dist and increment pts of first

    leaders = []
    leadval = max(lrace.items(), key=operator.itemgetter(1))[1]
    for e in lrace:
        if lrace[e] == leadval:
            leaders.append(e)

    for ed in leaders:
        race[ed]["pts"] = race[ed]["pts"] + 1
        
print(lrace)
print(race)
       
        
        