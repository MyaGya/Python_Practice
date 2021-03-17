import heapq

def solution(prices):
    ans = [0] * len(prices)
    que = []
    for pos, price in enumerate(prices):
        while 0 < len(que):
            queMaxPrice = que[0][0] * -1
            # 가격 하락이 발생하는 경우
            if price < queMaxPrice:
                ans[que[0][1]] = pos - que[0][1]
                heapq.heappop(que)
            else:
                break

        heapq.heappush(que, (price * -1, pos))
    while 0 < len(que):
        ans[que[0][1]] = pos - que[0][1]
        heapq.heappop(que)
    return ans



print(solution([1, 2, 3, 2, 3]))