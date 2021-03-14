import sys
from typing import List, Tuple

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def is_meet_duck(start: Tuple, goal: Tuple, lake: List):
    visited = {}
    y, x = start
    dfs_stack = []
    dfs_stack.append((x, y))
    while dfs_stack:
        x, y = dfs_stack.pop()
        visited[(x, y)] = True
        if (y, x) == goal:
            return True
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= col or next_y >= row or \
                    lake[next_y][next_x] == 'X' or \
                    (next_x, next_y) in visited:
                continue
            dfs_stack.append((next_x, next_y))
    return False


def next_day(lake: List):
    visited = {}
    dot_position = []
    for i in range(row):
        for j in range(col):
            if lake[i][j] == ".":
                visited[(i, j)] = True
                dot_position.append((i, j))

    expected_melting_position = set()
    while dot_position:
        y, x = dot_position.pop()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_y < 0 or next_x >= col or next_y >= row or \
                    lake[next_y][next_x] != "X" or (next_y, next_x) in visited:
                continue

            visited[(next_y, next_x)] = True
            expected_melting_position.add((next_y, next_x))

    while expected_melting_position:
        y, x = expected_melting_position.pop()
        lake[y][x] = "."


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
    day = 0

    start, goal = duck_position

    while not is_meet_duck(start, goal, lake):
        day += 1
        next_day(lake)
    print(day)
