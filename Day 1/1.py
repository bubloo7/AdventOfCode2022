input = open('input').read().splitlines()

l = []
curr = []
for line in input:
    if line == '':
        l.append(curr)
        curr = []
        continue
    curr.append(int(line))

print(max([sum(ll) for ll in l]))
