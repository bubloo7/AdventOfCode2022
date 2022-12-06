input = open('input').read().splitlines()

for i in range(len(input)):
    line = input[i]
    x = line.split(' ')
    for c in range(len(line)):
        s = set([c for c in line[c:c+4]])
        if len(s) == 4:
            print(c+4)
            break
