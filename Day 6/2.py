input = open('input').read().splitlines()

for i in range(len(input)):
    line = input[i]
    x = line.split(' ')
    for c in range(len(line)):
        s = set([c for c in line[c:c+14]])
        if len(s) == 14:
            print(c+14)
            break
