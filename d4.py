import hashlib


ki = 'bgvyzdsv'
found = False
c = 1

while not found:
    m = hashlib.md5()
    m.update(ki.encode('utf-8'))
    m.update(str(c).encode('utf-8'))

    check = m.hexdigest()[:6]

    if check.count('0') == 6:
        break
    c = c + 1

print(c)


