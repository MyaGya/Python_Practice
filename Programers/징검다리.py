def solution(distance, rocks, n):
    ### init ###
    L = 0
    R = distance
    rocks = [0] + rocks
    rocks.append(distance)
    rocks.sort()
    MIN = distance
    while L <= R:
        prev = 0
        MIN = distance
        delete_rock = 0

        mid = (L+R)//2
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[prev] < mid:
                delete_rock += 1
            else:
                MIN = min(MIN, rocks[i] - rocks[prev])
                prev = i
        if delete_rock > n:
            R = mid - 1
        else:
            ret = MIN
            L = mid + 1
    return ret
print(solution(25,[2, 14, 11, 21, 17],2))


