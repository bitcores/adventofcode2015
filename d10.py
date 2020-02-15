import time

st = time.time()

stri = "1321131112"
#stri = "1"

for r in range(0,40):
    x = 0
    n = ""
    while x < len(stri):
        if len(stri) == 1:
            n = "1" + stri
        elif x < len(stri) - 1:
            c = 1
            if stri[x] != stri[x+1]:
                    n = n + "1" + stri[x]
            else:
                while stri[x] == stri[x+1]:
                    c += 1
                    x += 1
                    if x == len(stri)-1:
                        break
                n = n + str(c) + stri[x]
        else:
            n = n + "1" + stri[x]
        
        x += 1

    stri = n

# dont print the output, it takes a long time
# this takes about 3 minutes for 40 repetitions, 8 hours for 50
#print(n)
print(len(stri))
print('Complete @ ', time.time() - st)