def solution(A, B):
    A.sort(), B.sort()
    i,j = 0,0
    ret = 0
    while j < len(B):
        if A[i] < B[j]:
            i += 1
            j += 1
            ret += 1
        else:
            j += 1
    return ret


print(solution([5,1,3,7],[2,2,6,8]))