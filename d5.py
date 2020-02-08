totalnice = 0
totalnaughty = 0

def checksep(nl):
    for c in range(0, len(nl)-2):
        if nl[c] == nl[c+2]:
            return True
    return False

def checkdblpair(nl):
    for c in range(0, len(nl)-3):
        if nl[c:c+2] in nl[c+2:]:
            print(nl, nl[c:c+2], nl[c+2:])
            return True
    return False

with open("input5.txt") as fp:
    cnt = 0
    for line in fp:
        if checkdblpair(line):
            if checksep(line):
                totalnice += 1
            else:
                totalnaughty += 1
        else:
            totalnaughty += 1
        
print("Nice ", totalnice)
print("Naughty ", totalnaughty)