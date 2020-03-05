#row and column location is in user input
r = 3010
c = 3019

lp = 1
for p in range(0,r+c-1):
    lp = lp + p
#print(lp+c-1)

iterations = lp+c-1
print(iterations)

lastval = 20151125
for z in range(0,iterations-1):
    lastval = (lastval * 252533)%33554393

print(lastval)