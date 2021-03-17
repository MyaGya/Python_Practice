def solution(dirs: str):
    history = dict()
    pos = [5, 5]

    for move in dirs:
        if move == 'L':
            pos[1] -= 1
            if pos[1] < 0 or pos[1] > 10:
                pos[1] += 1
                continue
            history[(pos[0],pos[1], pos[0], pos[1] + 1)] = True
            history[( pos[0], pos[1] + 1, pos[0], pos[1])] = True

        elif move == 'U':
            pos[0] -= 1
            if pos[0] < 0 or pos[0] > 10:
                pos[0] += 1
                continue
            history[(pos[0],pos[1], pos[0] + 1, pos[1])] = True
            history[( pos[0] + 1, pos[1], pos[0], pos[1])] = True
        elif move == 'R':
            pos[1] += 1
            if pos[1] < 0 or pos[1] > 10:
                pos[1] -= 1
                continue
            history[(pos[0],pos[1], pos[0], pos[1] - 1)] = True
            history[( pos[0], pos[1] - 1, pos[0], pos[1])] = True
        elif move == 'D':
            pos[0] += 1
            if pos[0] < 0 or pos[0] > 10:
                pos[0] -= 1
                continue
            history[(pos[0],pos[1], pos[0] - 1, pos[1])] = True
            history[( pos[0] - 1, pos[1], pos[0], pos[1])] = True
    return len(history) // 2

print(solution("ULURRDLLU"))