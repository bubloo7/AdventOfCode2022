input = open('input').read().splitlines()

l = []
curr = []
for line in input:
    if line == '':
        l.append(curr)
        curr = []
        continue
    curr.append(int(line))

print(sum(sorted([sum(ll) for ll in l],reverse=True)[:3]))