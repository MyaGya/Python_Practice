def solution(n):
    top = [[], list(range(1, n + 1)), [], []]
    global check_top_3
    check_top_3 = n
    ret = []

    def bfs(number):
        global check_top_3
        if len(top[3]) == n or (top[3] and top[3][-1] == check_top_3):
            check_top_3 -= 1
            return True

        for i in range(1, 4):
            if not top[i] or top[number][-1] < top[i][-1]:
                top[i].append(top[number].pop())
                ret.append([number, i])
                if bfs(i):          # 값을 찾을 경우
                    if len(top[3]) == n:
                        return
                else:               # 찾지 못할 경우
                    ret.pop()
                    top[number].append(top[i].pop())
    bfs(1)
    return ret


print(solution(2))