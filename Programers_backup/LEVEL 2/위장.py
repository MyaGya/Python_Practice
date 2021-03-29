from collections import defaultdict


def solution(clothes):
    ans = 1
    data = defaultdict(int)
    for L in clothes: # diction에 입력
        data[L[1]] += 1
    for value in data.values(): # 경우의 수 계산
        ans *= value + 1
    return ans - 1 # 모두 입지 않는 경우 제외


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))