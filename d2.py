
totalpaper = 0
totalribbon = 0
with open("input2.txt") as fp:
    cnt = 0
    for line in fp:
        dime = line.split("x")
        dime[0] = int(dime[0])
        dime[1] = int(dime[1])
        dime[2] = int(dime[2])
        sides = []
        sides.append(int(dime[0])*int(dime[1]))
        sides.append(int(dime[1])*int(dime[2]))
        sides.append(int(dime[0])*int(dime[2]))
        sides.sort()
        totalpaper += sides[0]*3 + sides[1]*2 + sides[2]*2
        dime.sort()
        totalribbon += (int(dime[0])*2 + int(dime[1])*2) + int(dime[0])*int(dime[1])*int(dime[2])

print(totalpaper)
print(totalribbon)