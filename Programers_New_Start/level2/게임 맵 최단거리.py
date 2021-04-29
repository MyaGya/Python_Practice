from collections import deque


def solution(maps):
    visited = {}
    direction_x = [1, 0, -1, 0]
    direction_y = [0, -1, 0, 1]
    waiting = deque()
    waiting.append((0, 0, 0))

    number = 0
    while waiting:
        pos_x, pos_y, number = waiting.popleft()

        if (pos_x, pos_y) in visited:
            continue
        if pos_x < 0 or pos_x >= len(maps[0]):
            continue
        if pos_y < 0 or pos_y >= len(maps):
            continue
        if maps[pos_y][pos_x] == 0:
            continue

        if pos_x == len(maps[0]) - 1 and pos_y == len(maps) - 1:
            break
        visited[(pos_x, pos_y)] = True
        for i in range(4):
            waiting.append((pos_x + direction_x[i], pos_y + direction_y[i], number + 1))
    else:
        return -1
    return number + 1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
