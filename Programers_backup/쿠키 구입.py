# 1. 모든 경우의 수를 고려?
'''
길이가 2000이라 안될 것 같다.
sliding window로?
값이 전체적으로 부족하지 않을까?
조건이 l~m,m+1부터 r까지니까
중간값을 하나 잡고
계속 늘려가면서 확인하면 되지 않을까?
왼쪽 오른쪽중 어느쪽을 먼저 늘리냐에 따라 영향을 받는가?
1 1 1 2 3 일경우
영향을 받지 않는다
값이 같으면 어느쪽으로든 움직이지 않으니 개선 필요'''


def solution(cookie):
    ret = 0

    # 중간값 계산
    for i in range(len(cookie) - 1):
        L = i                # L 의 시작점
        R = i + 1            # R 의 시작점
        L_value = cookie[L]  # L의 값
        R_value = cookie[R]  # R의 값

        while True:

            if L_value == R_value:                              # 값이 같을경우 무조건 비교
                ret = max(ret, L_value)
            if L_value < R_value and 0 < L:                     # 왼쪽이 더 작은 경우의 수
                L -= 1
                L_value += cookie[L]
            elif L_value >= R_value and R < len(cookie) - 1:    # 오른쪽이 더 작은 경우의 수
                R += 1
                R_value += cookie[R]
            else:                                               # 종료조건
                break

    return ret

print(solution([1,1,2,3]))