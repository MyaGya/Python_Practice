def solution(v):
    point_X, point_Y = list(zip(*v))
    point_X = sorted(point_X)
    point_Y = sorted(point_Y)
    x = point_X[0] if point_X[1] == point_X[2] else point_X[2]
    y = point_Y[0] if point_Y[1] == point_Y[2] else point_Y[2]
    return ([x,y])

print(solution([[1, 4], [3, 4], [3, 10]]))