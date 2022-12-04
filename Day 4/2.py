input = open('input').read().splitlines()

ans = 0

for i in range(len(input)):
    line = input[i]
    x = line.split(',')
    e1 = x[0].split('-')
    e2 = x[1].split('-')
    n1 = int(e1[0])
    n2 = int(e1[1]) 
    n3 = int(e2[0])
    n4 = int(e2[1])
    if (n1 <= n3 and n2 >= n3) or (n3 <= n1 and n4 >= n1) or  (int(e2[0]) <= int(e1[0]) and int(e2[1]) >= int(e1[1])) or (int(e2[0]) >= int(e1[0]) and int(e2[1]) <= int(e1[1])):
        ans += 1 


print(ans)