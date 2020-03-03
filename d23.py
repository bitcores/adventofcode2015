
#set "a" to 1 for part 2
r = {"a": 0, "b": 0}
cmdlist = []

with open("input23.txt") as fp:
    for line in fp:
        x = 0
        line = line.strip()
        cmdlist.append(line)

pos = 0

while pos < len(cmdlist):
    cmdl = cmdlist[pos].split(", ")
    cmd = cmdl[0].split(" ")

    if cmd[0] == "inc":
        r[cmd[1]] += 1
        pos+=1
    elif cmd[0] == "tpl":
        r[cmd[1]] = r[cmd[1]] * 3
        pos+=1
    elif cmd[0] == "hlf":
        r[cmd[1]] = r[cmd[1]] / 2
        pos+=1
    elif cmd[0] == "jmp":
        step = int(cmd[1][1:])
        if cmd[1][0] == "-":
            step = step * -1
        pos+=step
    elif cmd[0] == "jie":
        if r[cmd[1]] % 2 == 0:
            step = int(cmdl[1][1:])
            if cmdl[1][0] == "-":
                step = step * -1
            pos+=step
        else:
            pos+=1
    elif cmd[0] == "jio":
        if r[cmd[1]] == 1:
            step = int(cmdl[1][1:])
            if cmdl[1][0] == "-":
                step = step * -1
            pos+=step
        else:
            pos+=1

print(r)