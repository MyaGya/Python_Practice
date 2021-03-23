import heapq


def solution(prices: list):
    waiting = []
    answer = [possible_max_value for possible_max_value in range(len(prices) - 1, -1, -1)]
    for i in range(len(prices)):
        price = prices[i]
        if not waiting:
            heapq.heappush(waiting, (-price, i))
            continue
        while (waiting and -waiting[0][0] > price):
            answer[waiting[0][1]] = i - waiting[0][1]
            heapq.heappop(waiting)
        heapq.heappush(waiting, (-price, i))
    else:
        for _, index in waiting:
            answer[index] = len(prices) - 1 - index
    return answer
