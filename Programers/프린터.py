from collections import deque
# 대기목록에 자신보다 큰 수가 있는지 확인
def find(waiting, value):
    for i in range(waiting.__len__()):
        if waiting[i][0] > value:
            return True
    return False

def solution(priorities, location):
    waiting = deque()
    ret = 1
    for i, data in enumerate(priorities):
        waiting.append((data,i))

    while True:
        # 큰 수가 있을 경우
        if find(waiting, waiting[0][0]):
            waiting.append(waiting.popleft())
        # 큰 수가 없을 경우
        else:
            if waiting[0][1] == location:
                return ret
            else:
                waiting.popleft()
                ret += 1
print(solution([1, 1, 9, 1, 1, 1], 0))