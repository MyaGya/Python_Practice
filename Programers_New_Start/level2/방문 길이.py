def solution(dirs):
    direction = {}
    direction['U'] = [0, 1]
    direction['D'] = [0, -1]
    direction['L'] = [-1, 0]
    direction['R'] = [1, 0]

    visited = {}
    x, y = 0, 0
    answer = 0
    for move in dirs:
        next_x = direction[move][0] + x
        next_y = direction[move][1] + y
        if not -5 <= next_x <= 5 or not -5 <= next_y <= 5:
            continue
        if not (min(x, next_x), max(x, next_x), min(y, next_y), max(y, next_y)) in visited:
            visited[(min(x, next_x), max(x, next_x), min(y, next_y), max(y, next_y))] = True
            answer += 1
        x, y = next_x, next_y
    return answer


print(solution("LULLLLLLU"))
