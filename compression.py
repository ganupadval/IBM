st = "a2a1b2c2c4"
i = 0
l = len(st)
new = {}
for i in range(1, l, 2):
    if st[i-1] not in new:
        new[st[i-1]] = int(st[i])
    else:
        b = new.get(st[i-1])
        new[st[i-1]] = int(st[i])+b
    i += 1
print(new)
