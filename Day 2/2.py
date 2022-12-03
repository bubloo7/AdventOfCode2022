input = open('input').read().splitlines()

ans  = 0

for line in input:
    x,y = line.split(' ')
    if x == 'A':
        if y == 'X':
            ans += 3
        elif y == 'Y':
            ans += 4
        else: ans += 8
    elif x == 'B':
        if y == 'X':
            ans += 1
        elif y == 'Y':
            ans += 5
        else: ans += 9
    elif x == 'C':
        if y == 'X':
            ans += 2
        elif y == 'Y':
            ans += 6
        else: ans += 7
    
    
print(ans)
