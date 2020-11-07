import random
f = open("input.txt", 'w')

data = [[0 for _ in range(10)] for _ in range(10)]


number = 100
for i in range(10):
    for j in range(10):
        data[i][j] = number
        number -= 1


#for i in range(100):
#    a = random.randint(0, 9)
#    b = random.randint(0, 9)
#    data[a][b], data[b][a] = data[b][a], data[a][b]

for s in data:
    f.write(str(s) + ',')

f.close()