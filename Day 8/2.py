input = open('input').read().splitlines()

ans = 0
i = 0
trees  = []

for line in input:
    curr = []
    for c in line:
        curr.append(int(c))
    trees.append(curr)
i = 0

def up(i,j,k):
    i -= 1
    a = 0
    while i >= 0:
        if trees[i][j] >= k:
            return a + 1
        i -= 1
        a += 1
    return a

def down(i,j,k):
    i += 1
    a = 0
    while i < len(trees):
        if trees[i][j] >= k:
            return a + 1
        i += 1
        a += 1
    return a

def left(i,j,k):
    j -= 1
    a = 0
    while j >= 0:
        if trees[i][j] >= k:
            return a + 1
        j -= 1
        a += 1
    return a

def right(i,j,k):
    j += 1
    a = 0
    while j < len(trees[0]):
        if trees[i][j] >= k:
            return a + 1
        j += 1
        a += 1
    return a

for i in range(len(trees)):
    for j in range(len(trees[0])):
        k = trees[i][j]
        t = up(i,j,k) * down(i,j,k) * left(i,j,k) * right(i,j,k)
        if t > ans:
            ans = t
print(ans)
