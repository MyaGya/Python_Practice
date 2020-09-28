from collections import deque


def solution(maps):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    bfs = deque()
    bfs.append([0, 0, 1])  # x, y, deepth
    visited = [[False for _ in range(101)] for _ in range(101)]

    while bfs:
        data = bfs.popleft()
        if data[0] < 0 or data[0] >= len(maps[0]) or data[1] < 0 or data[1] >= len(maps):
            continue
        if visited[data[0]][data[1]]:
            continue
        if maps[data[1]][data[0]] == 0:
            continue
        if data[0] == len(maps[0])-1 and data[1] == len(maps)-1:            # end
            break
        visited[data[0]][data[1]] = True

        for i in range(4):
            bfs.append([data[0]+dx[i], data[1]+dy[i], data[2] + 1])
    else:
        return -1

    return data[2]

print(solution([[1,1,1,],[1,1,1,],[1,1,1],[1,1,1],[1,1,1]]))