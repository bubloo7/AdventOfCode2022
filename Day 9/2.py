import string
input = open('input').read().splitlines()

l = []
l1 = []
l2 = []
d = {}
d1 = {}
d2 = {}
s = set()
s1 = set()
s2 = set()
lo = string.ascii_lowercase
u = string.ascii_uppercase


ans = 0
i = 0
heads = [[0,0] for i in range((10))]

n = 9
while i < len(input):
    line = input[i]
    x = line.split(' ')
    l = int(x[1])
    d = x[0]
    for k in range(l):
        if d == 'R':
            heads[0][0] += 1
        elif d== 'L':
            heads[0][0] -= 1
        elif d== 'U':
            heads[0][1] += 1
        else:
            heads[0][1] -= 1  
        for j in range(1,10):
            diffx, diffy = heads[j-1][0] - heads[j][0], heads[j-1][1] - heads[j][1]
            if diffx == 2 and diffy == 2:
                heads[j][0] = heads[j-1][0] -1
                heads[j][1] = heads[j-1][1] - 1
            elif diffx == 2 and diffy == -2:
                heads[j][0] = heads[j-1][0] -1
                heads[j][1] = heads[j-1][1] + 1
            elif diffx == -2 and diffy == 2:
                heads[j][0] = heads[j-1][0] + 1
                heads[j][1] = heads[j-1][1] - 1
            elif diffx == -2 and diffy == -2:
                heads[j][0] = heads[j-1][0] + 1
                heads[j][1] = heads[j-1][1] + 1

            elif diffx == 2:
                heads[j][0] = heads[j-1][0] -1
                heads[j][1] = heads[j-1][1]
            elif diffx == -2:
                heads[j][0] = heads[j-1][0] + 1
                heads[j][1] = heads[j-1][1]
            elif diffy == 2:
                heads[j][0] = heads[j-1][0] 
                heads[j][1] = heads[j-1][1] - 1
            elif diffy == -2:
                heads[j][0] = heads[j-1][0] 
                heads[j][1] = heads[j-1][1] + 1
        s.add((heads[n][0],heads[n][1]))   


    i += 1

print(s,"\n",len(s))
