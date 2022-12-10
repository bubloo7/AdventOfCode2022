input = open('input').read().splitlines()

l = []
i = 0
t = 1
c = 0
while i < len(input):
    line = input[i]
    x = line.split(' ')
    if x[0] == "addx":
        c += 1
        if (c-20) % 40 == 0:
            l.append(t*c)
        c += 1
        if (c-20) % 40 == 0:
            l.append(t*c)
        t += int(x[1])
    else:
        c += 1
        if (c-20) % 40 == 0:
            l.append(t*c)
    
    i += 1
print(sum(l))