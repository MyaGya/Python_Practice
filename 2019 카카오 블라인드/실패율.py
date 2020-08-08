# 실패율 : 스테이지에 도달했으나 클리어못한 플레이어 수 / 스테이지에 도달한 플레이어 수
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    tmp = sorted(result)
    tmp = sorted(result, key=lambda x : result[x], reverse=True)
    return tmp

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))