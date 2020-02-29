import copy

base = { "hp": 100, "d": 0, "a": 0 }
boss = { "hp": 109, "d": 8, "a": 2 }

weapons = { "w1": {"c": 8, "d": 4, "a":0}, "w2": {"c": 10, "d": 5, "a":0}, "w3": {"c": 25, "d": 6, "a":0}, "w4": {"c": 40, "d": 7, "a":0}, "w5": {"c": 74, "d": 8, "a":0} }
armor = { "a0": {"c": 0, "d": 0, "a":0}, "a1": {"c": 13, "d": 0, "a":1}, "a2": {"c": 31, "d": 0, "a":2}, "a3": {"c": 53, "d": 0, "a":3}, "a4": {"c": 75, "d": 0, "a":4}, "a5": {"c": 102, "d": 0, "a":5} }
rings = { "ra0": {"c": 0, "d": 0, "a":0}, "rd0": {"c": 0, "d": 0, "a":0}, "rd1": {"c": 25, "d": 1, "a":0}, "rd2": {"c": 50, "d": 2, "a":0}, "rd3": {"c": 100, "d": 3, "a":0}, "ra1": {"c": 20, "d": 0, "a":1}, "ra2": {"c": 40, "d": 0, "a":2}, "ra3": {"c": 80, "d": 0, "a":3} }

def runcombat(plar):
    bhp = boss["hp"]
    php = base["hp"]
    while bhp > 0:
        if php <= 0:
            return False
        bhp = bhp - (plar["d"] - boss["a"])
        #print("player hit boss for ",plar["d"] - boss["a"], " boss now on ", bhp)
        if bhp <= 0:
            return True
        php = php - (boss["d"] - plar["a"])
        #print("boss hit player for ", boss["d"] - plar["a"], "player now on", php)
        #input()
    return True


mincost = 99999
maxcost = -99999
for x in weapons.items():
    for y in armor.items():
        for z in rings.items():
            for zz in rings.items():
                if zz != z:
                    plyr = copy.deepcopy(base)
                    plyr["d"] = plyr["d"] + x[1]["d"] + z[1]["d"] + zz[1]["d"]
                    plyr["a"] = plyr["a"] + y[1]["a"] + z[1]["a"] + zz[1]["a"]
                    cost = x[1]["c"] + y[1]["c"] + z[1]["c"] + zz[1]["c"]
                    #print(plyr)
                    if runcombat(plyr):
                        if cost < mincost:
                            #print(cost)
                            #input()
                            mincost = cost
                    else:
                        if cost > maxcost:
                            maxcost = cost

print(mincost)
print(maxcost)


                    
