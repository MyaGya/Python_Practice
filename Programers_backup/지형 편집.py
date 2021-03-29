def b_search(mid, land, P, Q):
    cost = 0
    n = len(land)
    for i in range(n):
        for j in range(n):
            cost += (land[i][j] - mid) * Q if land[i][j] > mid else (mid - land[i][j]) * P
    return cost


def solution(land, P, Q):
    # binary search init
    L, R = 0, max(map(max, land))

    while L < R:
        mid = (L + R) // 2
        mid_value = b_search(mid, land, P, Q)
        mid_plus_one_value = b_search(mid + 1, land, P, Q)
        if mid_value < mid_plus_one_value:
            R = mid
        else:
            L = mid + 1
    return min(mid_value, mid_plus_one_value)


print(solution([[100]], 5, 3))
