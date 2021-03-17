# check함수의 경우의 수를 줄여주어야 한다.
# 현재는 n이 12일 경우 12!만큼 계산해야 하므로 시간초과가 발생한다
ret = 0
def dfs(n, y, col, cmp_refer_1, cmp_refer_2):
    global ret
    if y == n:
        ret += 1
        return

    for x in range(n):
        if x in col or (x + y) in cmp_refer_1 or (x - y) in cmp_refer_2:
            continue
        col.add(x)
        cmp_refer_1.add(x + y)
        cmp_refer_2.add(x - y)
        dfs(n, y + 1, col, cmp_refer_1, cmp_refer_2)
        col.remove(x)
        cmp_refer_1.remove(x + y)
        cmp_refer_2.remove(x - y)


def solution(n):
    col, cmp_refer_1, cmp_refer_2 = set(), set(), set()
    dfs(n, 0, col, cmp_refer_1, cmp_refer_2)
    return ret


print(solution(12))
