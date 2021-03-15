import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

if __name__ == "__main__":

    row, col = map(int, sys.stdin.readline().split())

    lake = []
    for _ in range(row):
        lake.append(list(sys.stdin.readline()))

    duck_position = []

    for i in range(row):
        for j in range(col):
            if lake[i][j] == 'L':
                duck_position.append((i, j))

    start, goal = duck_position

    day = 0

    visited = {}

    stack = []
    next_stack = []
    next_stack.append(start)
    meet = False
    while not meet:
        stack = next_stack
        next_stack = []
        while stack:
            y, x = stack.pop()
            if y < 0 or x < 0 or x >= col or y >= row or (y, x) in visited:
                continue
            elif lake[y][x] == "X":
                lake[y][x] = day
                # visited[(y, x)] = True
                next_stack.append((y, x))
            elif lake[y][x] == "L" and (y, x) != start:
                print(day) if day == 0 else print(day - 1)
                meet = True
                break
            else:
                visited[(y, x)] = True
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    stack.append((next_y, next_x))
        day += 1
