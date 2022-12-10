input = open('input').read().splitlines()

i = 0
t = 1
c = 0

while i < len(input):
    line = input[i]
    x = line.split(' ')
    if abs(t-c) <=1:
            print("#",end="")
    else:
        print(".",end="")
    if (c-0) % 40 == 0:
            print()
    if x[0] == "addx":
        c += 1
        c %= 40
        if abs(t-c) <=1:
            print("#",end="")
        else:
            print(".",end="")
        if (c-0) % 40 == 0:
            print()
        c += 1
        c %= 40
        t += int(x[1])
    else:
        c += 1
        c %= 40
        
    i += 1
