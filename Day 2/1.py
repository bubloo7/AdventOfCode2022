input = open('input').read().splitlines()

ans  = 0

for line in input:
    x,y = line.split(' ')
    if x == 'A':
        if y == 'X':
            ans += 4
        elif y == 'Y':
            ans += 8
        else: ans += 3
    elif x == 'B':
        if y == 'X':
            ans += 1
        elif y == 'Y':
            ans += 5
        else: ans += 9
    elif x == 'C':
        if y == 'X':
            ans += 7
        elif y == 'Y':
            ans += 2
        else: ans += 6
    

print(ans)
