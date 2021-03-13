import heapq
import sys

n = int(sys.stdin.readline())
max_heap = []
min_heap = []
for i in range(n):
    value = int(sys.stdin.readline())

    if len(max_heap) == 0 or len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -1 * value)
    else:
        heapq.heappush(min_heap, value)

    # Swap to balance
    if min_heap and max_heap and min_heap[0] < (-1 * max_heap[0]):
        tmp_min = heapq.heappop(min_heap)
        tmp_max = heapq.heappop(max_heap) * - 1

        heapq.heappush(max_heap, -1 * tmp_min)
        heapq.heappush(min_heap, tmp_max)

    print(-1 * max_heap[0])
