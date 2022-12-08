input = open('input').read().splitlines()

ans = 0
i = 0
rows = len(input)
cols = len(input[i])
see = [[False for j in range(cols)] for k in range(rows)]
ans += rows*2 + (cols-2)*2

trees  = []
for line in input:
    curr = []
    for c in line:
        curr.append(int(c))
    trees.append(curr)

for i in range(rows):
    see[i][0] = True
    see[i][cols-1] = True

for i in range(cols):
    see[0][i] = True
    see[rows-1][i] = True

i = 0

for i in range(1,len(trees)-1):
    for j in range(1,len(trees[0])-1):
        if trees[i][j] > trees[i-1][j]:
            see[i][j] = True
            ans += 1
        else:
            trees[i][j] = trees[i-1][j]

trees  = []
for line in input:
    curr = []
    for c in line:
        curr.append(int(c))
    trees.append(curr)

for i in range(1,len(trees)-1):
    for j in range(1,len(trees[0])-1):
      
        if trees[i][j] > trees[i][j-1]:
            see[i][j] = True
            ans += 1
        else:
            trees[i][j] = trees[i][j-1]

trees  = []
for line in input:
    curr = []
    for c in line:
        curr.append(int(c))
    trees.append(curr)

for i in range(len(trees) -2, 0,-1):
    for j in range(len(trees[0])-2,0,-1):
        if trees[i][j] > trees[i+1][j]:
            see[i][j] = True
            ans += 1
        else:
            trees[i][j] = trees[i+1][j]

trees  = []
for line in input:
    curr = []
    for c in line:
        curr.append(int(c))
    trees.append(curr)

for i in range(len(trees) -2, 0,-1):
    for j in range(len(trees[0])-2,0,-1):
        if trees[i][j] > trees[i][j+1]:
            see[i][j] = True
            ans += 1
        else:
            trees[i][j] = trees[i][j+1]
            
a = 0
for thing in see:
    for x in thing:
        if x:
            a += 1
print(a)
