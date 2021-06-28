def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum(map(lambda x, y: x * y, A, B))


print(solution([1, 4, 2], [5, 4, 4]))
