f = open("input1.txt", "r")
dinp = f.read()
f.close()

up = dinp.count("(")
down = dinp.count(")")

floor = up - down

print("floor number",floor)

f = 0
for e in range(0, len(dinp)):
    if dinp[e] == "(":
        f = f + 1
    if dinp[e] == ")":
        f = f - 1
    
    if f == -1:
        print("Position", e+1)
        break
