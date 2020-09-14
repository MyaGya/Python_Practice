import heapq


def solution(n, cores):
    ready = []

    for core_number, core in enumerate(cores):
        heapq.heappush(ready, [0, core_number])  # 수행 시간, 코어 번호
    time = 0
    while n > 0:
        time, core_number = heapq.heappop(ready)
        heapq.heappush(ready, [time + cores[core_number], core_number])  # 다음 수행 시간, 코어 번호
        n -= 1
    return core_number + 1

print(solution(6,[1,2,3]))