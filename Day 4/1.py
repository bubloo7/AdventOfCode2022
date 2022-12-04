input = open('input').read().splitlines()

ans = 0

for i in range(len(input)):
    line = input[i]
    x = line.split(',')
    e1 = x[0].split('-')
    e2 = x[1].split('-')
    ans += 1 if (int(e2[0]) <= int(e1[0]) and int(e2[1]) >= int(e1[1])) or (int(e2[0]) >= int(e1[0]) and int(e2[1]) <= int(e1[1])) else 0 


print(ans)