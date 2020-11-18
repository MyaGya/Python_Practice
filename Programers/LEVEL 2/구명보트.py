'''from collections import deque
def solution(people, limit):
    data = deque()
    people.sort()
    [data.append(i) for i in people]
    cnt = 0
    while 0 < len(data):
        if data[0] + data[len(data)-1] <= limit and 1 < len(data):
            data.pop()
            data.popleft()
        else:
            data.pop()
        cnt += 1
    return cnt
'''


def solution(people, limit):
    L, R = 0, len(people) - 1
    people.sort()
    cnt = 0
    while L < R:
        if people[L] + people[R] <= limit:
            cnt += 1
            L += 1
            R -= 1
        else:
            R -= 1
    return len(people) - cnt


print(solution([10,20,30,40,50,60,70,80,90]	,100))