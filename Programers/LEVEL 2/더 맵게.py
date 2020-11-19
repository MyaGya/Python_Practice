import heapq
'''
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
'''
def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0
    while scoville[0] < K and len(scoville) >= 2:
        food1, food2 = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + food2 * 2)
        ans += 1
    return ans if scoville[0] >= K else -1


print(solution([1, 2], 7))
