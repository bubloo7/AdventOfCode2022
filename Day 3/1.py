import string
input = open('input').read().splitlines()

d = {}
ans = 0

curr = 1
for x in  string.ascii_lowercase:
    d[x] = curr
    curr += 1
for x in  string.ascii_uppercase:
    d[x] = curr
    curr += 1

ind = 0
for line in input:
    x = line[:len(line)//2]
    y = line[len(line)//2:]
    s = None
    s = set([c for c in x])
    for c in y:
        if c in s:
            ans += d[c]
            break
    ind += 1

print(ans)
