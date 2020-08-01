tmp = input().split(';')

def findZero(x,y):
    global data
    if x<0 or y<0:
        return 1
    try:
        if data[x][y] == 0:
            return 1
    except:
        return 1
    return 0

def init(x,y):
    ret = 0
    ret += findZero(x+1,y)
    ret += findZero(x -1, y)
    ret += findZero(x , y+1)
    ret += findZero(x , y-1)
    return ret

data = []
for s in tmp:
    data.append(list(map(int,s.split(' '))))

ans = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 1:
            ans += init(i, j)
print(ans)