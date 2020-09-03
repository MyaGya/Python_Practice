import heapq
from collections import deque


def solution(jobs):
    division = len(jobs)
    ret = 0
    time = 0
    jobs = deque([i for i in sorted(jobs)])
    waiting = []
    while not (len(jobs) == 0 and len(waiting) == 0):
        if waiting:
            tmp = heapq.heappop(waiting)
            time += tmp[0]
            ret += time - tmp[1]
        else:
            time = jobs[0][0]

        while jobs and jobs[0][0] <= time:  # 삽입
            heapq.heappush(waiting, [jobs[0][1], jobs[0][0]])  # [사용시간 , 요청 시간]
            jobs.popleft()

    return int(ret // division)


print(solution([[10000,3],[0,10]]))
