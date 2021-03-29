import heapq
def solution(operations):
    # time_complixity : O(n)
    maxHeap = []
    minHeap = []
    delete_number = dict()
    for i, s in enumerate(operations):
        identifier, value = s.split(" ")
        if identifier == 'I': # 삽입 연산
            heapq.heappush(maxHeap,(-int(value), i))
            heapq.heappush(minHeap,(int(value), i))
        else: # 삭제 연산
            if value == '1':
                while len(maxHeap):
                    data = heapq.heappop(maxHeap)[1]
                    if data in delete_number:
                        continue
                    delete_number[data] = True
                    break

            else:
                while len(minHeap):
                    data = heapq.heappop(minHeap)[1]
                    if data in delete_number:
                        continue
                    delete_number[data] = True
                    break
    while len(minHeap): # heap lazy 적용
        if minHeap[0][1] in delete_number:
            heapq.heappop(minHeap)
        break
    while len(maxHeap): # heap lazy 적용
        if maxHeap[0][1] in delete_number:
            heapq.heappop(maxHeap)
        break
    if len(minHeap):
        return [-maxHeap[0][0], minHeap[0][0]]
    return [0,0]

print(solution(["D 1"]))