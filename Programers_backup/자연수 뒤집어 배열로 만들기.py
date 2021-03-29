def solution(n):
    return list(map(int,reversed(list(str(n)))))


print(solution(12345))