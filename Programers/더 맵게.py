import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    ret = 0
    while 2 <= len(scoville):
        if K < scoville[0]: # 종료조건 (모든 조건이 만족하는 경우)
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        ret += 1
    if K < scoville[0]:
        return ret
    return -1




k = int(input())
scoville = list(map(int, input().split()))
print(solution(scoville, k))
