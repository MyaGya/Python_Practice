from collections import defaultdict


def solution(clothes):
    data = defaultdict(int)

    for _, kind in clothes:
        data[kind] += 1

    answer = 1
    for value in data.values():
        answer *= value + 1

    return answer - 1
