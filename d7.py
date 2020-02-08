import copy
import numpy as np

initi = []
operat = []
signals = {}

def doop(sig, x, y=-1):
    global signals
    if sig == "NOT":
        return np.uint16(~signals[x])
    if sig == "LSHIFT":
        return np.uint16(signals[x] << int(y))
    if sig == "RSHIFT":
        return np.uint16(signals[x] >> int(y))
    if sig == "AND":
        if x.isdigit():
            c = int(x)
        else:
            c = signals[x]
        return np.uint16(c & signals[y])
    if sig == "OR":
        if x.isdigit():
            c = int(x)
        else:
            c = signals[x]
        return np.uint16(c | signals[y])
    print("Error ", sig)



with open("input7.txt") as fp:
    for line in fp:
        if line.count(" ") == 2:
            initi.append(line.strip())
        else:
            operat.append(line.strip())
        
for i in range(len(initi)):
    sll = initi[i].split(" -> ")
    if sll[0].isdigit():
        signals[sll[1]] = int(sll[0])
    else:
        operat.append(initi[i])

signals['b'] = 46065

operlist = copy.deepcopy(operat)
while not "a" in signals:
    rem = []
    for o in range(len(operlist)):
        lr = operlist[o].split(" -> ")
        op = lr[0].split(" ")

        if len(op) == 2:
            if op[1] not in signals:
                rem.append(operlist[o])
            else:
                signals[lr[1]] = doop(op[0], op[1])
        elif len(op) == 3:
            if op[0] not in signals and not op[0].isdigit():
                rem.append(operlist[o])
            elif (op[1] == "AND" or op[1] == "OR") and op[2] not in signals:
                rem.append(operlist[o])
            else:
                signals[lr[1]] = doop(op[1], op[0], op[2])
        else:
            if op[0] not in signals:
                rem.append(operlist[o])
            else:
                signals[lr[1]] = signals[lr[0]]
    #print(len(rem))
    #print(signals)
    #input()
    operlist = copy.deepcopy(rem)

print(signals)