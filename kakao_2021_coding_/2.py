from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    ret = []
    data = defaultdict(int)
    orders = list(map(lambda x: sorted(x), orders))  # orders의 순서를 차례대로 정렬
    # 1. course에 따른 orders의 경우의 수를 계산
    for i in course:
        for order in orders:
            tmp = list(combinations(order, i))  # 경우의 수
            for L in tmp:
                data[L] += 1

        if not data:  # course 순서로 뽑을 수 없는 경우
            continue
        MAX = max(data.values())  # 가장 많이 선택된 수
        if MAX == 1:  # 2번 이상 선택되어야 한다
            continue
        for L in data:
            if data[L] == MAX :  # 가장 많이 선택된 수를 리턴배열에 담는다
                ret.append("".join(L))
        data = defaultdict(int)
    return sorted(ret)



print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))