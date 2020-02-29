import operator
import math

pinp = 34000000
housecnt = 1
housdict = {}

while True:
    if not housecnt in housdict:
        housdict[housecnt] = 0
    p = 1

    while p <= math.sqrt(housecnt):
        if housecnt % p == 0:
            # for part 1 change multiplier to 10 and remove the <= 50 if statements
            if (housecnt / p == p):
                #print(p)
                housdict[housecnt] = housdict[housecnt] + p * 11
            else:
                #print(p, housecnt/p)
                if housecnt//p <= 50:
                    #print(p, housecnt/p)
                    #print(p)
                    housdict[housecnt] = housdict[housecnt] + p * 11
                if p <= 50 :
                    housdict[housecnt] = housdict[housecnt] + housecnt//p * 11
                    #print(p, housecnt//p)
        p += 1

    #print(housdict)
    #input()
    #print(housecnt, housdict[housecnt])
    if housdict[housecnt] >= pinp:
        print("house ", housecnt, " on ", housdict[housecnt])
        break
    housecnt += 1
