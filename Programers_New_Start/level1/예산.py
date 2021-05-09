def solution(d, budget):
    d.sort()

    sum_d = 0
    for i in range(len(d)):
        sum_d += d[i]
        if sum_d > budget:
            return i
    return len(d)
