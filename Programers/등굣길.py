# 아직 미결, BFS로 풀어야함, 특정 케이스에서의 예외 처리가 되어있지 않음
from collections import defaultdict


def check(i, j, route, water_hole):
    if water_hole[(i,j)]:
        return 0
    else:
        return route[i][j]


def solution(m, n, puddles):
    route = [[0 for _ in range(m)] for _ in range(n)]
    water_hole = defaultdict(int)
    for L in puddles:
        water_hole[(L[1]-1,L[0]-1)] = True
    for i in range(m):
        if water_hole[(0,i)]:
            break
        route [0][i] = 1
    for i in range(n):
        if water_hole[(i,0)]:
            break
        route [i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            route[i][j] = (check(i-1,j,route,water_hole) + check(i,j-1,route,water_hole)) % 1000000007
    return route[i][j]


print(solution(5, 4, [[2, 1], [2, 2], [2, 3], [4, 4], [4, 3], [4, 2]]))
