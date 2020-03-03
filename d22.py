import copy
from itertools import product

base = { "hp": 50, "mp": 500, "a": 0, "s": 0, "st": 0, "r": 0, "rt": 0 }
boss = { "hp": 55, "d": 8, "a": 0, "p": 0, "pt": 0 }

spells = { "mm": {"m": 53, "d": 4, "h": 0, "t": 0, "e": 0, "a": 0, "mg": 0}, "dr": {"m": 73, "d": 2, "h": 2, "t": 0, "e": 0, "a": 0, "mg": 0}, "sh": {"m": 113, "d": 0, "h": 0, "t": 6, "e": 0, "a": 7, "mg": 0}, "poi": {"m": 173, "d": 0, "h": 0, "t": 6, "e": 3, "a": 0, "mg": 0}, "re": {"m": 229, "d": 0, "h": 0, "t": 5, "e": 0, "a": 0, "mg": 101}}
minmpcost = 53

mincost = 99999
#maxcost = -99999

def runcombat(castlist):
    bhp = copy.deepcopy(boss)
    php = copy.deepcopy(base)
    c = 0
    mptotal = 0
    tictoc = True
    while bhp["hp"] > 0:  
        if tictoc:
            #hardmode
            php["hp"] = php["hp"] - 1
            if php["hp"] <= 0:
                return -1
            #end hardmode
            
        #apply status effects
        if bhp["p"] == 1:
            bhp["hp"] = bhp["hp"] - 3
            bhp["pt"] = bhp["pt"] - 1
            if bhp["pt"] <= 0:
                bhp["p"] = 0
        if php["r"] == 1:
            php["mp"] = php["mp"] + 101
            php["rt"] = php["rt"] - 1
            if php["rt"] <= 0:
                php["r"] = 0
        if php["s"] == 1:
            php["st"] = php["st"] - 1
            if php["st"] <= 0:
                php["s"] = 0
                php["a"] = 0

        #check death status before turn start (player shouldnt die before turn start)
        if bhp["hp"] <= 0:
            return mptotal
                  
        if tictoc:
            #players turn
            if php["mp"] < minmpcost:
                return -1
            #spell selection and cast          
            cvalid = False
            while not cvalid:
                ccast = castlist[c]
                if spells[ccast]["m"] > php["mp"]:
                    c+=1
                elif ccast == "sh" and php["s"] == 1:
                    c+=1
                elif ccast == "re" and php["r"] == 1:
                    c+=1
                elif ccast == "poi" and bhp["p"] == 1:
                    c+=1
                else:
                    cvalid = True
                if c >= len(castlist):
                    return -1

            if ccast == "mm":
                bhp["hp"] = bhp["hp"] - spells[ccast]["d"]
                #print("player cast mm, boss now on ", bhp["hp"])
            if ccast == "dr":
                bhp["hp"] = bhp["hp"] - spells[ccast]["d"]
                php["hp"] = php["hp"] + spells[ccast]["h"]
                #print("player cast dr boss now on ", bhp["hp"], " player now on ", php["hp"])
            if ccast == "sh":
                php["s"] = 1
                php["st"] = 6
                php["a"] = 7
                #print("player cast shield")
            if ccast == "poi":
                bhp["p"] = 1
                bhp["pt"] = 6
                #print("player cast poison")
            if ccast == "re":
                php["r"] = 1
                php["rt"] = 5
                #print("player cast recharge")
            
            php["mp"] = php["mp"] - spells[ccast]["m"]
            #print("player mp is now ", php["mp"])
            mptotal += spells[ccast]["m"]
            #input()
            
            if bhp["hp"] <= 0:
                return mptotal
            
            c += 1
            if c >= len(castlist):
                return -1
        else:
            #bosses turn
            php["hp"] = php["hp"] - (bhp["d"] - php["a"])
            #print("boss hit player for ", bhp["d"] - php["a"], " player now on", php["hp"])
            #input()
            if php["hp"] <= 0:
                return -1
        tictoc = not tictoc
        
    return -1



spelllist = list(product(spells, repeat=10))
#print(spelllist)

for x in spelllist:
    #print(x)
    #input()
    mpret = runcombat(x)
    if mpret > -1:
        if mpret < mincost:
            mincost = mpret

print(mincost)
#print(maxcost)


