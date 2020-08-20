# 최악 O(3n)
def solution(n, lost, reserve):
    user = [1 for _ in range(n)]
    for i in lost: # lost 처리
        user[i-1] -= 1
    for i in reserve: # reserve 처리
        user[i-1] += 1
    # 계산
    for i in range(n):
        if user[i] == 2:
            if i != 0 and user[i-1] == 0:
                user[i-1] += 1 # 자기자신값은 생략 가능(연산되지 않는다)
            elif i != n-1 and user[i+1] == 0:
                user[i+1] += 1
    return len([True for i in user if 0 < i])

print(solution(5,[2,4],[1,3,5]))