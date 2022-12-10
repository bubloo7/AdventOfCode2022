input = open('input').read().splitlines()

l = []
s = set()

ans = 0
i = 0
hx,hy = 0,0
tx,ty = 0,0

while i < len(input):
    line = input[i]
    x = line.split(' ')
    l = int(x[1])
    d = x[0]
    idk = []
    for k in range(l):
        if d == 'R':
            hx += 1
            diffx, diffy = abs(hx - tx), abs(hy - ty)
            if diffx == 0:
                1
            elif diffx == 1:
                1
            else:
                tx = hx -1
                ty = hy
            s.add((tx,ty))        
            idk.append((tx,ty))
        if d == 'L':
            hx -= 1
            diffx, diffy = abs(hx - tx), abs(hy - ty)
            if diffx == 0:
                1
            elif diffx == 1:
                1
            else:
                tx = hx + 1
                ty = hy
            s.add((tx,ty))        
            idk.append((tx,ty))

        if d == 'U':
            hy += 1
            diffx, diffy = abs(hx - tx), abs(hy - ty)
            if diffy == 0:
                1
            elif diffy == 1:
                1
            else:
                tx = hx 
                ty = hy -1
            s.add((tx,ty))        
            idk.append((tx,ty))

        if d == 'D':
            hy -= 1
            diffx, diffy = abs(hx - tx), abs(hy - ty)
     
            if diffy == 0:
                1
            elif diffy == 1:
                1
            else:
                tx = hx 
                ty = hy +1
            s.add((tx,ty))
            idk.append((tx,ty))


    i += 1

print(len(s))