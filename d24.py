from itertools import combinations

plist = []

with open("input24.txt") as fp:
    for line in fp:
        x = 0
        line = line.strip()
        plist.append(int(line))

#per compartment weight
#divide by 4 for part 2
pcw = sum(plist,0) // 3

#find the least number of packages that'll reach pcw (probably less than 10 packages)
sol = ()
for x in range(1,10):
    combs = list(combinations(plist, x))
    for y in combs:
        if sum(y,0) == pcw:
            sol = y
            break
    if len(sol) > 0:
        break

#i"m not handling lowest EQ of same number package groups because i don't have any
print(sol)
qe = 1
for z in sol:
    qe = qe * z
print(qe)

