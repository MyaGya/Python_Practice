# 나중에 수정하기, deque를 사용하면 전체 크기를 아는데 set을 사용해야함

from collections import deque
def solution(gems):
    # 전체 크기
    size = len(set(gems))
    ans_section = [0, len(gems)]

    L = 0
    R = 0
    box = deque()
    while R < len(gems)+1:
        # 크기를 만족 할 경우
        if len(set(box)) == size:
            # 반영한다
            if R-1 - L < ans_section[1] - ans_section[0]:
                ans_section = [L, R-1]
            L += 1
            box.popleft()
        # 실질적 탈출 if
        elif R == len(gems):
            break
        # 만족하지 못 할 경우 범위를 늘린다
        else:
            box.append(gems[R])
            R += 1

    return [ans_section[0]+1, ans_section[1]+1]


data = (input().split())

print(solution(data))