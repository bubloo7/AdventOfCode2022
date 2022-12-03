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
for i in range(0,len(input),3):
    x = input[i]
    y = input[i+1]
    z = input[i+2]

    s = set([c for c in x])
    s2 = set([c for c in y])
    for c in z:
        if c in s and c in s2:
            ans += d[c]
            break
    ind += 1

print(ans)