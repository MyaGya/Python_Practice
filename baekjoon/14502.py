import copy
n, k = map(int,input().split())
ret = 0
area = []
for i in range(n):
    tmp = list(map(int,input().split()))
    area.append(tmp)


def spread_virus():
    global n, k, area
    copy_area = copy.deepcopy(area)
    stack = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(n):
        for j in range(k):
            if copy_area[i][j] == 2:
                stack.append((i, j))

    while stack:
        default_y, default_x = stack.pop()
        for i in range(4):
            y = default_y + dy[i]
            x = default_x + dx[i]
            if x >= k or x < 0 or y >= n or y < 0:
                continue
            if copy_area[y][x] == 0:
                copy_area[y][x] = 2
                stack.append((y,x))

    tmp = 0
    for i in range(n):
        for j in range(k):
            if copy_area[i][j] == 0:
                tmp += 1
    global ret
    ret = max(ret,tmp)

def make_wall(x, row, col):
    global n, k, area
    if x == 3:
        spread_virus()
        return
    for i in range(row, n):
        for j in range(col, k):
            if area[i][j] == 0: # WALL
                area[i][j] = 1
                make_wall(x+1, i, j+1)
                area[i][j] = 0
        col = 0


make_wall(0, 0, 0)

print(ret)