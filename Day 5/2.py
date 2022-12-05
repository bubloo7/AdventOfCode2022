input = open('input').read().splitlines()

stacks = [[] for i in range(9)]
for i in range(0,8):
    line = input[i]
    for j in range(9):
        if line[j*4 + 1] != " ":
            stacks[j].append(line[j*4 + 1])

for i in range(10, len(input)):
    line = input[i].split(' ')  
    n = int(line[1])
    stk1 = int(line[3])
    stk2 = int(line[5])
    for  j in range(n):
        temp = stacks[stk1-1].pop(0)
        stacks[stk2-1].insert(j,temp)

for s in stacks:
    print(s[0],end='')
