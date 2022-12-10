# if d == 'R':
#     heads[0][0] += 1
# elif d== 'L':
#     heads[0][0] -= 1
# elif d== 'U':
#     heads[0][1] += 1
# else:
#     heads[0][1] -= 1  
# for j in range(1,10):
#     diffx, diffy = heads[j-1][0] - heads[j][0], heads[j-1][1] - heads[j][1]
#     heads[j][0] += diffx//2
#     heads[j][1] += diffy//2
# s.add((heads[n][0],heads[n][1]))  