from collections import defaultdict


def solution(n, results):
    wins = defaultdict(set)
    loses = defaultdict(set)

    for L in results:
        wins[L[0]].add(L[1])  # i가 이긴 사람들
        loses[L[1]].add(L[0])  # i가 진 사람들

    for i in range(1, n + 1):
        for winner in loses[i]:  # i보다 높은 랭크는
            wins[winner].update(wins[i])  # i보다 낮은 랭크를 다 가진다(이김)
        for loser in wins[i]:  # i보다 낮은 랭크는
            loses[loser].update(loses[i])  # i보다 높은 랭크를 다 가진다(짐)
    ret = 0
    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) == n - 1: # 본인 제외
            ret += 1
    return ret

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))