def solution(d, budget):
    d.sort()
    sum = 0
    for i in range(len(d)):
        sum += d[i]
        if sum > budget:
            return i
    return len(d)


"""
from itertools import accumulate
def solution(d, budget):
    data_set = list(accumulate(sorted(d)))
    print(data_set)
    for i in range(len(data_set)):
        if data_set[i] > budget:
            return i
    return i+1
"""