input = open('input').read().splitlines()

l = []
d = {}
d1 = {}

ans = 0
l.append("")
i = 0 

while i < len(input):
    line = input[i]
    if "ls" in line:
       
        i += 1
        line = input[i]

        while "$" not in line and i < len(input):
            if "dir" in line:
                l2 = d1.get("".join(l),[])
                l2.append("".join(l) + "/" + line.split(" ")[1])
                d1["".join(l)] = l2
                d["".join(l) + "/" + line.split(" ")[1]] = d.get("".join(l) + "/" + line.split(" ")[1],0)
            else:
                d["".join(l)] = d.get("".join(l), 0) +  int(line.split(" ")[0]) 
            i += 1
            if i == len(input):
                break
            line = input[i]

    if "cd" in line:
        if "/" in line: 
            l = [""]
        elif ".." in line:
            l.pop()
        else:
            l.append("/" + line.split(" ")[2])
        
    i += 1

def calculate(path, d,d1):
    for i in d1.get(path,[]):
        calculate(i,d,d1)
    for i in d1.get(path,[]):
        temp = d[i]
        d[path] += temp
    d1[path] = []

space =  70000000
for k in d:
    space -= d[k]
calculate("",d,d1)
m = []
for k in d:
    if space + d[k] >= 30000000:
        m.append(d[k])

print(min(m))